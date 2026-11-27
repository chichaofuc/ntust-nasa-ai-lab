# M4 FD001 Browser UAT

- Status: `PASS_WITH_EVIDENCE`
- Started: `2026-11-27T11:44:39+08:00`
- Finished: `2026-11-27T11:45:01+08:00`
- Browser: `Brave (Chromium)` version `158.0.8127.92`
- Actual URL: `http://127.0.0.1:18767/`
- API Base URL: `http://127.0.0.1:18766`
- Browser automation: Selenium WebDriver on the installed Brave browser; actual visible browser window.
- Network evidence: Selenium Chrome performance log plus non-transforming response capture of actual browser `fetch` calls.
- Screenshots: `M4_UAT_EVIDENCE/uat-*.png`.
- Console severe entries: 1; expected API-unavailable 503: 1; unexpected: 0.
- UI/API/raw comparisons: 62; failed: 0.

## Browser operation trace

| Time | Step | Expected | Actual | Status |
|---|---|---|---|---|
| 2026-11-27T11:44:44+08:00 | UAT-01 Initial load | Real page loads; health, catalog, Train Units and Sensors come from M3; chart/table show actual records | FD001 Engine Health Analysis; Verified FD001 sources connected; 192 rows/192 points; 100 Units and 21 Sensors | PASS |
| 2026-11-27T11:44:45+08:00 | UAT-02 Unit switching / stale data | Switch Unit 1→2, clear old view while loading, reload Unit 2 and its API-derived Cycle bounds | Unit 2 · 1–287 cycles; bounds 1–287; old chart/table cleared before response | PASS |
| 2026-11-27T11:44:46+08:00 | Train Unit 2 Sensor 7 Cycle 1–20 | train Unit 2, Sensor 7, inclusive Cycle 1–20; chart, table and captured browser API JSON agree | API 200; 20 table rows; 20 SVG points; fields/provenance matched record-by-record | PASS |
| 2026-11-27T11:44:48+08:00 | Train Unit 2 Sensor 11 Cycle 3–14 | train Unit 2, Sensor 11, inclusive Cycle 3–14; chart, table and captured browser API JSON agree | API 200; 12 table rows; 12 SVG points; fields/provenance matched record-by-record | PASS |
| 2026-11-27T11:44:50+08:00 | Train Unit 1 Sensor 7 Cycle 1–20 | train Unit 1, Sensor 7, inclusive Cycle 1–20; chart, table and captured browser API JSON agree | API 200; 20 table rows; 20 SVG points; fields/provenance matched record-by-record | PASS |
| 2026-11-27T11:44:55+08:00 | Test Unit 2 Sensor 7 Cycle 1–10 | test Unit 2, Sensor 7, inclusive Cycle 1–10; chart, table and captured browser API JSON agree | API 200; 10 table rows; 10 SVG points; fields/provenance matched record-by-record | PASS |
| 2026-11-27T11:44:55+08:00 | UAT-07 Invalid Cycle range | Reject Start 11 > End 10 and clear previous data | Check range; validation message: Start Cycle must be less than or equal to End Cycle; 0 rows and 0 points | PASS |
| 2026-11-27T11:44:59+08:00 | UAT-08 API unavailable | With M3 stopped, show 503 error and clear old data | API unavailable; HTTP 503; 0 rows and 0 points | PASS |
| 2026-11-27T11:45:01+08:00 | UAT-09 Recovery | Restart M3 and restore the current valid query | View ready; 10 rows and 10 points | PASS |

Detailed API responses, Network statuses, source hashes, and runtime metadata: `M4_UAT_EVIDENCE/browser_uat_trace.json`.
