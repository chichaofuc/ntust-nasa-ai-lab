import csv, hashlib, json, math, statistics, sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parent
DATA=ROOT/'data'/'FD001'
NAMES=('train_FD001.txt','test_FD001.txt','RUL_FD001.txt')
OUT=('M2_FD001_FILE_INVENTORY.md','M2_FD001_RAW_DATA_PROFILE.md','M2_FD001_DATA_QUALITY.md','M2_FD001_TREND_ANALYSIS.md','M2_FD001_DATA_CONTRACT.md')
START=datetime.now().astimezone().isoformat(timespec='seconds')
def digest(b): return hashlib.sha256(b).hexdigest().upper()
def read(name,width):
 p=(DATA/name).resolve(strict=True); raw=p.read_bytes(); txt=raw.decode('ascii'); lines=txt.splitlines(); rows=[]; errors=[]
 for no,line in enumerate(lines,1):
  if not line.strip(): continue
  tok=line.split()
  if len(tok)!=width: errors.append((no,'width',len(tok))); continue
  try:
   row=[float(x) for x in tok]
   if not all(math.isfinite(x) for x in row): raise ValueError('nonfinite')
   rows.append(row)
  except ValueError as e: errors.append((no,str(e)))
 m={'path':str(p),'bytes':len(raw),'sha_before':digest(raw),'encoding':'ASCII','format':'whitespace-delimited numeric text','physical':len(lines),'blank':sum(not x.strip() for x in lines),'nonblank':sum(bool(x.strip()) for x in lines),'parsed':len(rows),'widths':sorted(set(map(len,rows))),'errors':errors,'empty':not raw,'final_newline':raw.endswith((b'\n',b'\r'))}
 if errors or m['widths']!=[width] or not rows: raise RuntimeError(f'PHASE_A_BLOCKED {name}: {m}')
 return p,rows,m
def integer(x,label):
 if not float(x).is_integer(): raise RuntimeError(f'PHASE_A_BLOCKED noninteger {label}: {x}')
 return int(x)
def groups(rows):
 d=defaultdict(list)
 for r in rows: d[integer(r[0],'unit')].append((integer(r[1],'cycle'),r))
 return dict(d)
def audit(g):
 out=[]
 for u,items in g.items():
  c=[x for x,_ in items]; s=sorted(set(c))
  out.append({'u':u,'first':c[0],'last':c[-1],'n':len(c),'ordered':all(a<b for a,b in zip(c,c[1:])),'contig':s==list(range(1,max(s)+1)),'dup':len(c)-len(s),'missing':max(s)-min(s)+1-len(s)})
 return out
def summary(v):
 v=list(v); return {'n':len(v),'min':min(v),'max':max(v),'mean':statistics.fmean(v),'median':statistics.median(v),'sd':statistics.stdev(v) if len(v)>1 else 0,'unique':len(set(v)),'constant':min(v)==max(v)}
def q(v,p):
 v=sorted(v); z=(len(v)-1)*p; lo=int(z); hi=math.ceil(z); return v[lo] if lo==hi else v[lo]+(v[hi]-v[lo])*(z-lo)
def slope(pairs,i):
 x=[c for c,_ in pairs]; y=[r[i] for _,r in pairs]; mx=statistics.fmean(x); my=statistics.fmean(y); d=sum((a-mx)**2 for a in x)
 return sum((a-mx)*(b-my) for a,b in zip(x,y))/d if d else 0.0
def table(head,rows):
 return '| '+' | '.join(head)+' |\n|'+'|'.join(['---']*len(head))+'|\n'+'\n'.join('| '+' | '.join(str(x).replace('|','\\|') for x in r)+' |' for r in rows)
def f(x): return f'{x:.6g}'
paths={}; data={}; meta={}
for name,width in ((NAMES[0],26),(NAMES[1],26),(NAMES[2],1)):
 paths[name],data[name],meta[name]=read(name,width)
train,test,rulrows=data[NAMES[0]],data[NAMES[1]],data[NAMES[2]]
tg,xg=groups(train),groups(test); ta,xa=audit(tg),audit(xg); order=list(xg); rul=[integer(r[0],'RUL') for r in rulrows]
if set(tg)!=set(range(1,len(tg)+1)) or set(xg)!=set(range(1,len(xg)+1)): raise RuntimeError('PHASE_A_BLOCKED unit IDs')
if not all(a['ordered'] and a['contig'] and not a['dup'] for a in ta+xa): raise RuntimeError('PHASE_A_BLOCKED unit cycles')
if len(rul)!=len(xg) or order!=sorted(order): raise RuntimeError('PHASE_A_BLOCKED RUL positional counts/order')# Sensor summaries use pooled raw observations for distribution and per-Unit regression for trends.
sensors=[]; quality_rows=[]; trend_rows=[]; sensor_lines=[]
for sn in range(1,22):
 idx=4+sn; name=f'sensor_{sn:02d}'; split={}; outliers={}
 for label,rows in (('Train',train),('Test',test)):
  vals=[r[idx] for r in rows]; split[label]=summary(vals); lo=q(vals,.25); hi=q(vals,.75); iqr=hi-lo
  flagged=[(integer(r[0],'unit'),integer(r[1],'cycle'),r[idx]) for r in rows if r[idx]<lo-1.5*iqr or r[idx]>hi+1.5*iqr]
  outliers[label]={'q1':lo,'q3':hi,'low':lo-1.5*iqr,'high':hi+1.5*iqr,'n':len(flagged),'examples':flagged[:5]}
 unit=[]
 for u,pairs in tg.items(): unit.append({'unit':u,'first':pairs[0][0],'last':pairs[-1][0],'n':len(pairs),'mean':statistics.fmean(r[idx] for _,r in pairs),'slope':slope(pairs,idx)})
 sl=[a['slope'] for a in unit]; asc=sum(z>0 for z in sl); desc=sum(z<0 for z in sl); zero=sum(z==0 for z in sl)
 terc=[]
 for groupset in (tg,xg):
  parts=[[],[],[]]
  for pairs in groupset.values():
   pairs=sorted(pairs); n=len(pairs); bounds=(0,n//3,2*n//3,n)
   for j in range(3):
    sub=pairs[bounds[j]:bounds[j+1]]
    if sub: parts[j].append(statistics.fmean(r[idx] for _,r in sub))
  terc.append([statistics.fmean(z) for z in parts])
 rank=sorted(unit,key=lambda a:a['slope'])
 d={'name':name,'idx':idx,'train':split['Train'],'test':split['Test'],'out':outliers,'positive':asc,'negative':desc,'zero_slope':zero,'slope_mean':statistics.fmean(sl),'slope_median':statistics.median(sl),'terc_train':terc[0],'terc_test':terc[1],'low_units':rank[:3],'high_units':rank[-3:],'unit_mean_range':[min(a['mean'] for a in unit),max(a['mean'] for a in unit)]}
 sensors.append(d)
 quality_rows.append([name,idx,f(split['Train']['min']),f(split['Train']['max']),f(split['Train']['mean']),f(split['Train']['sd']),split['Train']['unique'],split['Train']['constant'],outliers['Train']['n'],split['Test']['unique'],split['Test']['constant'],outliers['Test']['n']])
 trend_rows.append([name,idx,*[f(split[z][k]) for z in ('Train','Test') for k in ('min','max','mean','sd')],asc,desc,zero,f(d['slope_median']),f(d['unit_mean_range'][0])+' to '+f(d['unit_mean_range'][1]),*[f(v) for v in terc[0]],*[f(v) for v in terc[1]]])
 for trend_type,selected in (('decrease',[a for a in rank if a['slope']<0][:2]),('increase',[a for a in reversed(rank) if a['slope']>0][:2])):
  for a in selected: sensor_lines.append([name,idx,trend_type,a['unit'],f"{a['first']}–{a['last']}",a['n'],f(a['slope'])])
# Integrity check before any report output.
for name in NAMES:
 meta[name]['sha_after']=digest(paths[name].read_bytes())
 if meta[name]['sha_after']!=meta[name]['sha_before']: raise RuntimeError(f'STOP source hash changed: {name}')
phase_a='PASS_WITH_NOTES'
phase_note='RUL has 100 values and Test first-occurrence Unit order is 1..100, so positional coverage is one-to-one. RUL rows have no Unit ID key; semantic row identity is not cross-key-verifiable from these files.'
train_counts=[a['n'] for a in ta]; test_counts=[a['n'] for a in xa]
cycle_rows=[[label,len(aud),min(a['n'] for a in aud),statistics.median(a['n'] for a in aud),statistics.fmean(a['n'] for a in aud),max(a['n'] for a in aud),min(a['last'] for a in aud),max(a['last'] for a in aud)] for label,aud in (('Train',ta),('Test',xa))]
fieldmap=[(0,'unit_id','identifier','integer','VERIFIED','Integral IDs group trajectories; identity is split-local.'),(1,'cycle','index','integer','VERIFIED','Integral, contiguous sequence from 1 within each observed Unit.')]
for i in range(3): fieldmap.append((2+i,f'operating_setting_{i+1}','operating setting','numeric','INFERRED','Position/layout only; physical definition and unit unknown.'))
for i in range(21): fieldmap.append((5+i,f'sensor_{i+1:02d}','sensor slot','numeric','UNKNOWN','Raw slot verified; physical meaning and unit not supplied.'))# 0-based field mapping table
maprows=[[i,n,c,t,s,e] for i,n,c,t,s,e in fieldmap]
# Inventory report
invrows=[]
for n in NAMES:
 m=meta[n]; invrows.append([n,m['path'],m['bytes'],m['sha_before'],m['sha_after'],m['encoding'],m['format'],m['physical'],m['blank'],m['nonblank'],m['parsed'],m['widths'][0],'YES','YES'])
inventory='# M2 FD001 File Inventory\n\nWork Item: `M2_FD001_LOCAL_DATA_VALIDATION_001`\nPhase A: `'+phase_a+'`\n\n'
inventory+=table(['File','Absolute path','Bytes','SHA-256 before','SHA-256 after','Encoding','Format','Physical lines','Blank lines','Nonblank lines','Parsed rows','Columns','Readable','Unchanged'],invrows)
inventory+='\n\nAll source files were read only. ASCII decode and finite numeric parsing succeeded. No source bytes were changed.\n'
# Raw profile
rp='# M2 FD001 Raw Data Profile\n\nPhase A: `'+phase_a+'`\nNote: '+phase_note+'\n\n'
rp+='## Raw row and column counts\n\n'+table(['File','Physical lines','Blank','Nonblank','Parsed rows','Parsed columns','Bad lines'],[[n,meta[n]['physical'],meta[n]['blank'],meta[n]['nonblank'],meta[n]['parsed'],meta[n]['widths'][0],len(meta[n]['errors'])] for n in NAMES])
rp+='\n\nParsing: strict ASCII; each nonblank physical line is one record; whitespace tokenization; each value must parse to a finite float; widths must be 26/26/1. Raw physical lines are distinct from parsed rows. No line was silently skipped except blank lines (none found).\n\n'
rp+='## Unit and Cycle checks\n\nUnit IDs are split-local trajectory identifiers. Train/Test IDs each span 1–100 and first occur in ascending order. Every Unit Cycle begins at 1, increases strictly, and is contiguous. IDs in separate splits do not establish the same physical engine. Test final observed Cycle is not a failure Cycle.\n\n'+table(['Split','Units','Rows','Cycles per Unit min','median','mean','max','Last Cycle min','Last Cycle max'],[[l,len(aud),len(data[NAMES[0] if l=='Train' else NAMES[1]]),*[(min(c) if j==0 else c) for j,c in enumerate([ [a['n'] for a in aud],statistics.median(a['n'] for a in aud),statistics.fmean(a['n'] for a in aud),max(a['n'] for a in aud),min(a['last'] for a in aud),max(a['last'] for a in aud)])]] for l,aud in (('Train',ta),('Test',xa))])
rp+='\n\n### Train Unit ranges\n\n'+table(['Unit','First Cycle','Last Cycle','Rows'],[[a['u'],a['first'],a['last'],a['n']] for a in ta])
rp+='\n\n### Test last observed Cycle and RUL positional mapping\n\nRUL has no Unit ID. Pairing below uses row index against Test Unit first-occurrence order; count and order match, but semantic ID cannot be independently cross-keyed from RUL.\n\n'+table(['Test Unit','Last observed Cycle','Rows','RUL row 1-based','RUL value'],[[a['u'],a['last'],a['n'],i+1,rul[i]] for i,a in enumerate(xa)])
rp+='\n\nRUL rows: '+str(len(rul))+'. Integer value range: '+str(min(rul))+'–'+str(max(rul))+'. It provides one value per Test Unit by positional rule, not a separate value for each Test Cycle and not a fault-class label.\n\n## Raw column index (0-based)\n\nFiles have no header; canonical names are positional labels, not proof of physical meaning.\n\n'+table(['Index','Canonical field','Category','Type','Semantic status','Evidence / limitation'],maprows)
rp+="\n\n## Label semantics\n\nTrain/Test contain no explicit fault class. Train has observed trajectories through each Unit\'s last supplied Cycle; files alone do not prove a physical failure at the last row. `last_observed_cycle - cycle` is computable but is true failure RUL only under that endpoint assumption. Test has no per-Cycle label. RUL_FD001 has 100 values; positional coverage is one-to-one with Test Unit first-occurrence order 1..100. The RUL file has no Unit key, so semantic row association remains a positional-contract limitation.\n"
# Quality report
quality="# M2 FD001 Data Quality\n\nPhase A: `"+phase_a+"`; no source values were changed, dropped, or filled.\n\n"
trdup=sum(v-1 for v in Counter(tuple(r) for r in train).values() if v>1); tedup=sum(v-1 for v in Counter(tuple(r) for r in test).values() if v>1)
truc=sum(v-1 for v in Counter((integer(r[0],'u'),integer(r[1],'c')) for r in train).values() if v>1); teuc=sum(v-1 for v in Counter((integer(r[0],'u'),integer(r[1],'c')) for r in test).values() if v>1)
repeated_rul_values=sum(v-1 for v in Counter(r[0] for r in rulrows).values() if v>1)
quality+=table(['Check','Train','Test','RUL','Method'],[
 ['Records',len(train),len(test),len(rul),'One record per nonblank physical line.'],['Malformed width',0,0,0,'Expected 26/26/1 tokens.'],['Unparseable/nonfinite',0,0,0,'All tokens finite numeric values.'],['Blank lines',meta[NAMES[0]]['blank'],meta[NAMES[1]]['blank'],meta[NAMES[2]]['blank'],'Whitespace-only physical lines.'],['Exact duplicate rows',trdup,tedup,'N/A','RUL has one scalar per row, so duplicate row comparison is not applicable across distinct Units.'],['Repeated RUL scalar values','N/A','N/A',repeated_rul_values,'Repeated values across RUL records; expected and not classified as duplicate records or a quality defect.'],['Duplicate Unit-Cycle',truc,teuc,'N/A','Exact (Unit ID, Cycle) pair.'],['Missing cells',0,0,0,'Fixed-width whitespace records have no null tokens.']])
quality+='\n\n## Unit-cycle integrity\n\n'+table(['Split','Units','Strict order','Contiguous from 1','Duplicate keys','Missing internal cycles'],[['Train',len(tg),'YES','YES',truc,0],['Test',len(xg),'YES','YES',teuc,0]])
quality+='\n\n## Sensor statistics and statistical flags\n\n'+table(['Sensor','Index','Train min','Train max','Train mean','Train SD','Train unique','Train constant','Train Tukey flags','Test unique','Test constant','Test Tukey flags'],quality_rows)
quality+='\n\nTukey flags use pooled-split Q1/Q3 with linear interpolation at (n−1)p and the descriptive 1.5×IQR rule, computed separately for Train and Test. These are statistical flags only, not physical anomalies, alarm thresholds, or fault diagnoses. Counts are exact; the five first file-order examples per sensor/split are printed below where any flags occur. No rows were deleted. Constant means exact min=max. No near-constant threshold was invented.\n\n'
examples=[]
for s in sensors:
 for split in ('Train','Test'):
  for u,c,v in s['out'][split]['examples']: examples.append([split,s['name'],s['idx'],u,c,f(v)])
quality+=table(['Split','Sensor','Index','Unit','Cycle','Flagged value'],examples or [['N/A','None','N/A','N/A','N/A','N/A']])
quality+='\n\nThe table gives up to five traceable examples for every Sensor/Split with statistical flags; counts above include all flagged observations. Statistical flags do not establish physical abnormality.\n'
# Trend report
trend='# M2 FD001 Sensor Trend Evidence\n\nPhase A: `'+phase_a+'`. Phase B: `COMPLETED_AFTER_PHASE_A_PASS_WITH_NOTES`.\n\n'
trend+='## Unit / Cycle observations\n\nTrain has 100 split-local Units, 20,631 rows; cycle count per Unit '+str(min(train_counts))+'–'+str(max(train_counts))+' (median '+f(statistics.median(train_counts))+', mean '+f(statistics.fmean(train_counts))+'). Test has 100 Units, 13,096 rows; cycle counts '+str(min(test_counts))+'–'+str(max(test_counts))+' (median '+f(statistics.median(test_counts))+', mean '+f(statistics.fmean(test_counts))+'). Cycles are assessed within each Unit, not concatenated. Test last observed Cycle is an observation boundary, not failure Cycle.\n\n'
trend+='## Per-Sensor distribution and cycle trend\n\nOLS slopes are computed independently per Train Unit as raw sensor value regressed on Cycle. Direction counts use strict slope signs (> 0 positive; < 0 negative; == 0 zero), with no tolerance threshold. Early/Middle/Late are equal-weight means of per-Unit means after splitting each Unit\'s ordered cycles into three near-equal contiguous sections. No smoothing or normalization.\n\n'+table(['Sensor','Index','Train min','Train max','Train mean','Train SD','Test min','Test max','Test mean','Test SD','Units + slope','Units - slope','Units ZERO_SLOPE','Median Unit slope','Train Unit mean min to max','Train Early','Train Mid','Train Late','Test Early','Test Mid','Test Late'],trend_rows)
trend+='\n\n## Unit-specific trend evidence\n\nFor each sensor, these are up to the two most negative (strictly < 0) and two most positive (strictly > 0) Train per-Unit slopes. Exact zero slopes are excluded from directional extremes and counted as `ZERO_SLOPE` above. No arbitrary slope threshold is applied. They are descriptive extremes, not diagnoses.\n\n'+table(['Sensor','Index','Selection','Unit','Cycle range','N','OLS slope/cycle'],sensor_lines)
trend+='\n\n**OBSERVATION:** Tables contain source-derived values, split-level distributions, per-Unit slope direction counts, and cycle-segment summaries. **INFERENCE:** Repeated directional trends may motivate follow-up study, with uncertainty about sensor meaning and operating conditions. **UNKNOWN:** Physical failure mechanism, fault class, manufacturer limits, healthy baseline, causal relationship, maintenance history, and safety state. `BASELINE_STATUS: NOT_ESTABLISHED`. Trend direction or statistical flags are not fault diagnoses. Train has no explicit fault labels. Test has no per-Cycle RUL label; RUL is one positional value per Test Unit and not a fault class.\n'
contract='# M2 FD001 Data Contract\n\n## Source and file mapping\n\nUse only local `data/FD001/train_FD001.txt`, `test_FD001.txt`, and `RUL_FD001.txt`; identities and hashes are in `M2_FD001_FILE_INVENTORY.md`. Inputs are ASCII, headerless, whitespace-delimited finite numeric rows. Raw files are read-only and never enter Git.\n\n## Canonical positional schema (0-based)\n\n'+table(['Raw index','Canonical name','Category','Type','Semantic status','Evidence / limitation'],maprows)
contract+='\n\nUnit IDs and Cycle are integer-valued; settings and sensor slots are numeric. Sensor field names are position-based aliases only. Physical identities/units are UNKNOWN.\n\n## Unit and Cycle semantics\n\nUnit IDs index trajectories within each split; equal Train/Test IDs do not prove same physical asset. Cycle is the integer per-Unit observation index. Do not merge Unit timelines. Train\'s last supplied Cycle is an observed endpoint, not file-level proof of failure.\n\n## Train / Test / RUL relationship\n\nTrain has no explicit fault class or RUL column. A value `last_cycle(unit)-cycle` is derivable to the observed endpoint, but true failure RUL depends on an unverified endpoint assumption. Test has no per-Cycle labels. RUL has one integer per Test Unit by row position: Test first-occurrence order is 1..100 and row count is 100. RUL has no Unit ID, so its semantic pairing is a positional contract with a limitation, not an in-file foreign key. RUL is not a fault label.\n\n## Missing policy and validation rules\n\nRequire 26 tokens per Train/Test line and one per RUL line; finite numeric conversion; integer-valued Unit/Cycle/RUL; split-local Unit IDs; contiguous increasing per-Unit cycles for this validated input. Reject/report invalid lines; never silently drop or impute. These constraints describe the observed source and parser contract.\n\n## API-ready schema (definition only)\n\n```json\n{\n  \"split\": \"train|test\",\n  \"unit_id\": 1,\n  \"cycle\": 1,\n  \"operating_settings\": [0.0, 0.0, 0.0],\n  \"sensors\": {\"sensor_01\": 0.0, \"sensor_21\": 0.0},\n  \"rul_at_last_observation\": null\n}\n```\n\nA Test RUL may be attached to the trajectory endpoint by positional index with the stated caveat. Do not replicate it as ground truth for each Test Cycle. No website/API is implemented here.\n\n## Known limitations\n\n`BASELINE_STATUS: NOT_ESTABLISHED`. No fault-class labels, verified physical sensor meanings, validated units, maintenance/failure records, healthy ranges, or fault thresholds are provided. Statistical distributions and Tukey flags are descriptive. No trend or correlation is a fault diagnosis. M3–M5 are not authorized.\n'
reports={OUT[0]:inventory,OUT[1]:rp,OUT[2]:quality,OUT[3]:trend,OUT[4]:contract}
for name,content in reports.items(): (ROOT/name).write_text(content.rstrip()+'\n',encoding='utf-8',newline='\n')
summary_out={'execution_started':START,'execution_finished':datetime.now().astimezone().isoformat(timespec='seconds'),'python':sys.version.split()[0],'phase_a_status':phase_a,'phase_a_note':phase_note,'phase_b_status':'COMPLETED_AFTER_PHASE_A_PASS_WITH_NOTES','files':{n:{'path':meta[n]['path'],'bytes':meta[n]['bytes'],'sha256_before':meta[n]['sha_before'],'sha256_after':meta[n]['sha_after'],'physical_lines':meta[n]['physical'],'blank_lines':meta[n]['blank'],'parsed_rows':meta[n]['parsed'],'columns':meta[n]['widths'][0],'parse_errors':len(meta[n]['errors'])} for n in NAMES},'train':{'rows':len(train),'units':len(tg),'unit_ids':[min(tg),max(tg)],'cycle_count':[min(train_counts),max(train_counts)],'last_cycle':[min(a['last'] for a in ta),max(a['last'] for a in ta)],'cycles_contiguous':all(a['contig'] and a['ordered'] for a in ta),'duplicate_rows':trdup,'duplicate_unit_cycle':truc},'test':{'rows':len(test),'units':len(xg),'unit_ids':[min(xg),max(xg)],'cycle_count':[min(test_counts),max(test_counts)],'last_cycle':[min(a['last'] for a in xa),max(a['last'] for a in xa)],'cycles_contiguous':all(a['contig'] and a['ordered'] for a in xa),'duplicate_rows':tedup,'duplicate_unit_cycle':teuc},'rul':{'rows':len(rul),'range':[min(rul),max(rul)],'positional_test_alignment':len(rul)==len(xg) and order==sorted(order),'has_unit_key':False},'sensors':{'count':len(sensors),'train_exact_constants':[x['name'] for x in sensors if x['train']['constant']],'test_exact_constants':[x['name'] for x in sensors if x['test']['constant']],'train_tukey_flags_total':sum(x['out']['Train']['n'] for x in sensors),'test_tukey_flags_total':sum(x['out']['Test']['n'] for x in sensors)},'reports':list(reports)}
print(json.dumps(summary_out,ensure_ascii=False,indent=2))
