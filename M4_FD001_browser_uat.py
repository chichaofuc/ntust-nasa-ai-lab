"""Run real-browser M4 UAT against local M3 API and reconcile displayed rows."""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from urllib.request import urlopen

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

ROOT = Path(__file__).resolve().parent
EVIDENCE = ROOT / "M4_UAT_EVIDENCE"
API_PORT = 18766
WEB_PORT = 18767
API_BASE = f"http://127.0.0.1:{API_PORT}"
WEB_URL = f"http://127.0.0.1:{WEB_PORT}/"
BRAVE = Path(r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe")
SOURCE_SPECS = {
    "train": ("train_FD001.txt", 3515356, "963B5E22825B34D8B21C69E1AEB4AF3E647050EB672EE8834BA4B5D91D2DE0F8"),
    "test": ("test_FD001.txt", 2228855, "3CDA7109CE17BAFB5443F2AC926CFCF88154B941B8C4CF95EB55D1DDD6F52851"),
    "rul": ("RUL_FD001.txt", 429, "A19C8EC94931949D0485BDC35118206E9C81C4547B422EFB9CF86F4CEDDBCECA"),
}
INSTRUMENTATION = r"""
(() => {
  const nativeFetch = window.fetch.bind(window);
  window.__m4ApiTrace = [];
  window.fetch = async (...args) => {
    const response = await nativeFetch(...args);
    const url = new URL(typeof args[0] === "string" ? args[0] : args[0].url, location.href);
    if (url.pathname.startsWith("/api/")) {
      let body = null;
      try { body = await response.clone().json(); } catch {}
      window.__m4ApiTrace.push({url: url.pathname + url.search, status: response.status, body, timestamp: new Date().toISOString()});
      await new Promise(resolve => setTimeout(resolve, 250));
    }
    return response;
  };
})();
"""


def stamp() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def verify_sources() -> dict:
    result = {}
    for split, (filename, expected_bytes, expected_sha) in SOURCE_SPECS.items():
        path = ROOT / "data" / "FD001" / filename
        raw = path.read_bytes()
        digest = hashlib.sha256(raw).hexdigest().upper()
        physical_lines = len(raw.decode("ascii").splitlines())
        if len(raw) != expected_bytes or digest != expected_sha:
            raise RuntimeError(f"Source validation failed: {filename}")
        result[split] = {"path": f"data/FD001/{filename}", "bytes": len(raw), "physical_lines": physical_lines, "sha256": digest}
    return result


def start_server(script: str, args: list[str], stdout_path: Path, stderr_path: Path, extra_env: dict[str, str] | None = None):
    stdout = stdout_path.open("w", encoding="utf-8")
    stderr = stderr_path.open("w", encoding="utf-8")
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)
    process = subprocess.Popen([sys.executable, str(ROOT / script), *args], cwd=ROOT, env=env,
                               stdout=stdout, stderr=stderr, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    return process, stdout, stderr


def wait_url(url: str, process: subprocess.Popen, timeout: float = 20):
    end = time.time() + timeout
    last_error = None
    while time.time() < end:
        if process.poll() is not None:
            raise RuntimeError(f"Server exited unexpectedly ({process.returncode}): {last_error}")
        try:
            with urlopen(url, timeout=1) as response:
                if response.status < 500:
                    return response.status
        except Exception as exc:
            last_error = str(exc)
            time.sleep(0.2)
    raise RuntimeError(f"Timed out waiting for {url}: {last_error}")


def check(condition: bool, message: str):
    if not condition:
        raise AssertionError(message)


def ui_records(driver) -> list[list[str]]:
    return driver.execute_script("return Array.from(document.querySelectorAll('#records-body tr')).map(tr => Array.from(tr.cells).map(td => td.textContent.trim()));")


def api_trace(driver) -> list[dict]:
    return driver.execute_script("return window.__m4ApiTrace || [];")


def query_state(driver) -> str:
    return driver.find_element(By.ID, "query-state").text.strip()


def wait_state(driver, expected: str, timeout: int = 20):
    WebDriverWait(driver, timeout).until(lambda d: query_state(d) == expected)


def set_range(driver, start: int, end: int):
    start_el = driver.find_element(By.ID, "start-input")
    end_el = driver.find_element(By.ID, "end-input")
    start_el.clear(); start_el.send_keys(str(start))
    end_el.clear(); end_el.send_keys(str(end))


def click_update(driver):
    driver.find_element(By.ID, "apply-button").click()


def run_query(driver, split: str, unit: int, sensor: int, start: int, end: int, label: str, steps: list[dict], evidence_file: str | None = None):
    trace_start = len(api_trace(driver))
    set_range(driver, start, end)
    click_update(driver)
    wait_state(driver, "View ready")
    rows = ui_records(driver)
    points = len(driver.find_elements(By.CSS_SELECTOR, ".trend-point"))
    check(len(rows) == end - start + 1, f"{label}: table count differs from requested inclusive range")
    check(points == len(rows), f"{label}: chart and table counts differ")
    captured = [item for item in api_trace(driver)[trace_start:] if item["url"].startswith("/api/history?")]
    check(bool(captured), f"{label}: no actual browser history response was captured")
    latest = captured[-1]
    check(latest["status"] == 200 and latest["body"]["ok"] is True, f"{label}: history API request did not succeed")
    data = latest["body"]["data"]
    check((data["split"], data["unit_id"], data["sensor"]["sensor_id"], data["range"]["start"], data["range"]["end"]) == (split, unit, sensor, start, end), f"{label}: API query parameters do not match UI controls")
    check(data["actual_count"] == len(rows) == len(data["records"]), f"{label}: API/UI row counts differ")
    check(driver.find_element(By.ID, "count-value").text == str(len(rows)), f"{label}: observation summary count differs")
    check(driver.find_element(By.ID, "chart-caption").text.endswith(f"{len(rows)} points"), f"{label}: chart point summary differs")
    for row, record in zip(rows, data["records"]):
        expected = [str(record["cycle"]), str(record["unit_id"]), str(record["sensor_id"]), record["sensor_field"], str(record["raw_column_index"]), str(record["value"]), record["source_file"], str(record["source_line"])]
        check(row == expected, f"{label}: UI row does not equal actual Browser API JSON record at Cycle {record['cycle']}: {row} != {expected}")
    step = {"time": stamp(), "name": label, "expected": f"{split} Unit {unit}, Sensor {sensor}, inclusive Cycle {start}–{end}; chart, table and captured browser API JSON agree", "actual": f"API {latest['status']}; {len(rows)} table rows; {points} SVG points; fields/provenance matched record-by-record", "status": "PASS", "request": latest["url"], "api_count": data["actual_count"], "chart_points": points, "table_rows": len(rows)}
    steps.append(step)
    if evidence_file:
        driver.execute_script("window.scrollTo(0,0)")
        driver.save_screenshot(str(EVIDENCE / evidence_file))
    return {"label": label, "split": split, "unit_id": unit, "sensor_id": sensor, "start": start, "end": end, "ui_rows": rows, "api_body": latest["body"]}


def reconcile(samples: list[dict]) -> tuple[list[dict], str]:
    comparisons = []
    source_cache = {}
    for sample in samples:
        split = sample["split"]
        filename = SOURCE_SPECS[split][0]
        if split not in source_cache:
            source_cache[split] = (ROOT / "data" / "FD001" / filename).read_text(encoding="ascii").splitlines()
        physical_lines = source_cache[split]
        sensor_id = sample["sensor_id"]
        raw_index = 5 + sensor_id - 1
        for ui_row, record in zip(sample["ui_rows"], sample["api_body"]["data"]["records"]):
            source_line = record["source_line"]
            tokens = physical_lines[source_line - 1].split()
            raw_value = float(tokens[raw_index])
            api_value = record["value"]
            ui_value = float(ui_row[5])
            fields_match = (
                int(float(tokens[0])) == record["unit_id"] == int(ui_row[1])
                and int(float(tokens[1])) == record["cycle"] == int(ui_row[0])
                and record["sensor_id"] == sensor_id == int(ui_row[2])
                and record["sensor_field"] == f"sensor_{sensor_id:02d}" == ui_row[3]
                and record["raw_column_index"] == raw_index == int(ui_row[4])
                and record["source_file"] == f"data/FD001/{filename}" == ui_row[6]
                and source_line == int(ui_row[7])
            )
            passed = fields_match and raw_value == api_value == ui_value
            if not passed:
                raise AssertionError(f"Raw/API/UI reconciliation failed: {sample['label']} Cycle {record['cycle']}")
            comparisons.append({
                "scenario": sample["label"], "split": split, "unit_id": record["unit_id"], "cycle": record["cycle"],
                "sensor_id": sensor_id, "sensor_field": record["sensor_field"], "raw_column_index": raw_index,
                "source_file": record["source_file"], "source_line": source_line,
                "raw_token": tokens[raw_index], "raw_value": raw_value, "api_value": api_value,
                "ui_value": ui_row[5], "match": "PASS",
            })
    return comparisons, ""


def main() -> int:
    EVIDENCE.mkdir(exist_ok=True)
    source_before = verify_sources()
    start_time = stamp()
    steps: list[dict] = []
    samples: list[dict] = []
    process_logs = {}
    api_proc = web_proc = None
    driver = None
    api_stdout = api_stderr = web_stdout = web_stderr = None
    result = {"work_item": "M4_FD001_INTERACTIVE_WEB_UI_001", "started": start_time, "workspace": str(ROOT), "source_before": source_before, "steps": steps}
    try:
        api_proc, api_stdout, api_stderr = start_server("M3_FD001_api.py", [], EVIDENCE / "m3-api.stdout.log", EVIDENCE / "m3-api.stderr.log", {"FD001_API_PORT": str(API_PORT)})
        health_status = wait_url(f"{API_BASE}/api/health", api_proc)
        result["api_start"] = {"command": f"python M3_FD001_api.py (FD001_API_PORT={API_PORT})", "status": health_status, "stdout": str(EVIDENCE / "m3-api.stdout.log"), "stderr": str(EVIDENCE / "m3-api.stderr.log")}
        web_proc, web_stdout, web_stderr = start_server("M4_FD001_web_server.py", ["--port", str(WEB_PORT), "--api-base", API_BASE], EVIDENCE / "m4-web.stdout.log", EVIDENCE / "m4-web.stderr.log")
        page_status = wait_url(WEB_URL, web_proc)
        result["web_start"] = {"command": f"python M4_FD001_web_server.py --port {WEB_PORT} --api-base {API_BASE}", "status": page_status, "url": WEB_URL, "stdout": str(EVIDENCE / "m4-web.stdout.log"), "stderr": str(EVIDENCE / "m4-web.stderr.log")}

        options = webdriver.ChromeOptions()
        options.binary_location = str(BRAVE)
        options.add_argument("--window-size=1440,1180")
        options.add_argument("--no-first-run")
        options.add_argument("--disable-background-networking")
        options.set_capability("goog:loggingPrefs", {"browser": "ALL", "performance": "ALL"})
        driver = webdriver.Chrome(options=options)
        driver.set_window_size(1440, 1180)
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": INSTRUMENTATION})
        driver.get(WEB_URL)
        wait = WebDriverWait(driver, 30)
        wait.until(EC.text_to_be_present_in_element((By.ID, "health-label"), "Verified FD001 sources connected"))
        wait_state(driver, "View ready")
        check(driver.title == "FD001 Engine Health Analysis", "Unexpected page title")
        check(len(Select(driver.find_element(By.ID, "unit-select")).options) == 100, "Unit options were not loaded from the API")
        check(len(Select(driver.find_element(By.ID, "sensor-select")).options) == 21, "Sensor options were not loaded from the API catalog")
        initial_rows = ui_records(driver)
        check(len(initial_rows) == len(driver.find_elements(By.CSS_SELECTOR, ".trend-point")) > 0, "Initial chart and table are empty or inconsistent")
        driver.save_screenshot(str(EVIDENCE / "uat-01-initial-load.png"))
        steps.append({"time": stamp(), "name": "UAT-01 Initial load", "expected": "Real page loads; health, catalog, Train Units and Sensors come from M3; chart/table show actual records", "actual": f"{driver.title}; {driver.find_element(By.ID, 'health-label').text}; {len(initial_rows)} rows/{len(driver.find_elements(By.CSS_SELECTOR, '.trend-point'))} points; 100 Units and 21 Sensors", "status": "PASS"})

        # Switching Unit clears old data synchronously before the delayed real API response is applied.
        Select(driver.find_element(By.ID, "unit-select")).select_by_value("2")
        wait.until(lambda d: query_state(d) == "Loading observations")
        switch_rows = ui_records(driver)
        switch_points = driver.find_elements(By.CSS_SELECTOR, ".trend-point")
        check(len(switch_rows) == 0 and len(switch_points) == 0, "Old Unit data remained visible while the new Unit request was pending")
        wait_state(driver, "View ready")
        unit2 = driver.find_element(By.ID, "unit-select").find_element(By.CSS_SELECTOR, "option:checked").text
        bounds = driver.find_element(By.ID, "cycle-bounds").text
        check("Unit 2" in unit2 and "–" in bounds, "Unit selector or actual Cycle bounds did not update")
        driver.save_screenshot(str(EVIDENCE / "uat-02-unit-switch.png"))
        steps.append({"time": stamp(), "name": "UAT-02 Unit switching / stale data", "expected": "Switch Unit 1→2, clear old view while loading, reload Unit 2 and its API-derived Cycle bounds", "actual": f"{unit2}; bounds {bounds}; old chart/table cleared before response", "status": "PASS"})

        # Sensor 7 is selected from API Catalog; selected Cycle window is inclusive.
        Select(driver.find_element(By.ID, "sensor-select")).select_by_value("7")
        wait_state(driver, "View ready")
        train_u2_s7 = run_query(driver, "train", 2, 7, 1, 20, "Train Unit 2 Sensor 7 Cycle 1–20", steps, "uat-03-train-u2-s7-range.png")
        samples.append(train_u2_s7)

        Select(driver.find_element(By.ID, "sensor-select")).select_by_value("11")
        wait_state(driver, "View ready")
        train_u2_s11 = run_query(driver, "train", 2, 11, 3, 14, "Train Unit 2 Sensor 11 Cycle 3–14", steps, "uat-04-sensor-switch.png")
        samples.append(train_u2_s11)

        Select(driver.find_element(By.ID, "unit-select")).select_by_value("1")
        wait_state(driver, "View ready")
        stale_rows = ui_records(driver)
        check(all(row[1] == "1" for row in stale_rows), "Unit 2 records remained after switching to Unit 1")
        Select(driver.find_element(By.ID, "sensor-select")).select_by_value("7")
        wait_state(driver, "View ready")
        train_u1_s7 = run_query(driver, "train", 1, 7, 1, 20, "Train Unit 1 Sensor 7 Cycle 1–20", steps, "uat-05-train-u1-s7.png")
        samples.append(train_u1_s7)

        Select(driver.find_element(By.ID, "split-select")).select_by_value("test")
        wait_state(driver, "View ready")
        check("TEST" in driver.find_element(By.ID, "count-detail").text, "Test split did not replace Train data")
        Select(driver.find_element(By.ID, "unit-select")).select_by_value("2")
        wait_state(driver, "View ready")
        check(all(row[6] == "data/FD001/test_FD001.txt" for row in ui_records(driver)), "Test Unit query used non-Test source rows")
        test_u2_s7 = run_query(driver, "test", 2, 7, 1, 10, "Test Unit 2 Sensor 7 Cycle 1–10", steps, "uat-06-test-u2-s7.png")
        samples.append(test_u2_s7)

        set_range(driver, 11, 10)
        click_update(driver)
        wait_state(driver, "Check range")
        check(len(ui_records(driver)) == 0 and len(driver.find_elements(By.CSS_SELECTOR, ".trend-point")) == 0, "Invalid range retained old observations")
        invalid_notice = driver.find_element(By.ID, "notice").text
        check("less than or equal" in invalid_notice, "Invalid range did not display a clear validation message")
        driver.save_screenshot(str(EVIDENCE / "uat-07-invalid-range.png"))
        steps.append({"time": stamp(), "name": "UAT-07 Invalid Cycle range", "expected": "Reject Start 11 > End 10 and clear previous data", "actual": f"{query_state(driver)}; validation message: Start Cycle must be less than or equal to End Cycle; 0 rows and 0 points", "status": "PASS"})

        # Safely stop only this script's M3 child to verify the API-unavailable UI state.
        set_range(driver, 1, 10)
        click_update(driver); wait_state(driver, "View ready")
        api_proc.terminate(); api_proc.wait(timeout=10)
        api_stdout.close(); api_stderr.close()
        unavailable_trace_start = len(api_trace(driver))
        click_update(driver)
        wait_state(driver, "API unavailable", timeout=20)
        check(len(ui_records(driver)) == 0 and len(driver.find_elements(By.CSS_SELECTOR, ".trend-point")) == 0, "API error retained previous chart/table data")
        unavailable_capture = [item for item in api_trace(driver)[unavailable_trace_start:] if item["url"].startswith("/api/history?")]
        check(bool(unavailable_capture) and unavailable_capture[-1]["status"] == 503, "API unavailable response was not observed in browser Network capture")
        driver.save_screenshot(str(EVIDENCE / "uat-08-api-unavailable.png"))
        steps.append({"time": stamp(), "name": "UAT-08 API unavailable", "expected": "With M3 stopped, show 503 error and clear old data", "actual": f"{query_state(driver)}; HTTP {unavailable_capture[-1]['status']}; 0 rows and 0 points", "status": "PASS"})

        api_proc, api_stdout, api_stderr = start_server("M3_FD001_api.py", [], EVIDENCE / "m3-api-restart.stdout.log", EVIDENCE / "m3-api-restart.stderr.log", {"FD001_API_PORT": str(API_PORT)})
        wait_url(f"{API_BASE}/api/health", api_proc)
        click_update(driver); wait_state(driver, "View ready")
        check(len(ui_records(driver)) == 10, "UI did not recover after M3 API restart")
        driver.save_screenshot(str(EVIDENCE / "uat-09-api-recovered.png"))
        steps.append({"time": stamp(), "name": "UAT-09 Recovery", "expected": "Restart M3 and restore the current valid query", "actual": f"{query_state(driver)}; {len(ui_records(driver))} rows and {len(driver.find_elements(By.CSS_SELECTOR, '.trend-point'))} points", "status": "PASS"})

        comparisons, _ = reconcile(samples)
        (EVIDENCE / "ui-api-csv-comparisons.json").write_text(json.dumps(comparisons, indent=2), encoding="utf-8")
        lines = [
            "# M4 FD001 UI / API / Raw CSV Reconciliation", "",
            "Values below came from real browser UI table rows, captured JSON responses to the UI's actual M3 API fetches, and the original read-only FD001 physical source lines.",
            "Sensor IDs are 1-based; raw data columns are 0-based. Physical source lines are 1-based.", "",
            "| Scenario | Split | Unit | Cycle | Sensor ID / field | Raw index | UI value | Browser API value | Source file | Source line | Raw CSV token | Match |",
            "|---|---|---:|---:|---|---:|---:|---:|---|---:|---:|---|",
        ]
        for row in comparisons:
            lines.append(f"| {row['scenario']} | {row['split']} | {row['unit_id']} | {row['cycle']} | {row['sensor_id']} / `{row['sensor_field']}` | {row['raw_column_index']} | {row['ui_value']} | {row['api_value']} | `{row['source_file']}` | {row['source_line']} | {row['raw_token']} | {row['match']} |")
        lines.extend(["", f"Compared {len(comparisons)} actual displayed rows across Train and Test; {len(comparisons)}/{len(comparisons)} passed exact parsed numeric and provenance comparisons.", ""])
        (ROOT / "M4_FD001_API_CSV_UI_RECONCILIATION.md").write_text("\n".join(lines), encoding="utf-8")

        perf = []
        for item in driver.get_log("performance"):
            message = json.loads(item["message"])["message"]
            if message.get("method") == "Network.responseReceived":
                response = message["params"]["response"]
                if "/api/" in response.get("url", ""):
                    perf.append({"url": response["url"], "status": response["status"], "mimeType": response.get("mimeType")})
        browser_errors = [entry for entry in driver.get_log("browser") if entry.get("level") == "SEVERE"]
        # The explicit API-unavailable UAT intentionally generates one Chromium
        # network SEVERE entry for the expected HTTP 503. Keep it in the record,
        # but distinguish it from unexpected browser errors.
        expected_browser_errors = [
            entry for entry in browser_errors
            if "/api/history?" in entry.get("message", "")
            and "503 (Service Unavailable)" in entry.get("message", "")
        ]
        unexpected_browser_errors = [entry for entry in browser_errors if entry not in expected_browser_errors]
        result.update({
            "finished": stamp(),
            "browser": {"name": "Brave (Chromium)", "version": driver.capabilities.get("browserVersion"), "capabilities": driver.capabilities.get("browserName")},
            "url": WEB_URL,
            "api_base_url": API_BASE,
            "browser_console_severe_errors": browser_errors,
            "browser_console_expected_errors": expected_browser_errors,
            "browser_console_unexpected_errors": unexpected_browser_errors,
            "browser_network_api_responses": perf,
            "csv_comparison_count": len(comparisons),
            "csv_comparison_failures": 0,
            "source_after": verify_sources(),
        })
        if unexpected_browser_errors:
            raise AssertionError(f"Unresolved browser Console errors: {unexpected_browser_errors}")
        if result["source_before"] != result["source_after"]:
            raise AssertionError("Original FD001 sources changed during UAT")
        result["status"] = "PASS_WITH_EVIDENCE"
    except Exception as exc:
        result["finished"] = stamp()
        result["status"] = "FAILED"
        result["failure"] = f"{type(exc).__name__}: {exc}"
        raise
    finally:
        if driver:
            try:
                perf_logs = driver.get_log("performance")
                browser_logs = driver.get_log("browser")
                result.setdefault("performance_log_entries_remaining", len(perf_logs))
                result.setdefault("browser_log_entries_remaining", len(browser_logs))
            except Exception:
                pass
            driver.quit()
        for process in (web_proc, api_proc):
            if process and process.poll() is None:
                process.terminate()
                try:
                    process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    process.kill(); process.wait(timeout=5)
        for handle in (api_stdout, api_stderr, web_stdout, web_stderr):
            if handle:
                handle.close()
        if api_stdout:
            process_logs["m3_stdout"] = (EVIDENCE / "m3-api.stdout.log").read_text(encoding="utf-8", errors="replace")
        if web_stdout:
            process_logs["m4_stdout"] = (EVIDENCE / "m4-web.stdout.log").read_text(encoding="utf-8", errors="replace")
        result["process_logs"] = process_logs
        (EVIDENCE / "browser_uat_trace.json").write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
        lines = ["# M4 FD001 Browser UAT", "", f"- Status: `{result.get('status', 'FAILED')}`", f"- Started: `{result.get('started')}`", f"- Finished: `{result.get('finished')}`", f"- Browser: `{(result.get('browser') or {}).get('name', 'Brave (Chromium)')}` version `{(result.get('browser') or {}).get('version', 'unavailable')}`", f"- Actual URL: `{WEB_URL}`", f"- API Base URL: `{API_BASE}`", "- Browser automation: Selenium WebDriver on the installed Brave browser; actual visible browser window.", "- Network evidence: Selenium Chrome performance log plus non-transforming response capture of actual browser `fetch` calls.", "- Screenshots: `M4_UAT_EVIDENCE/uat-*.png`.", f"- Console severe entries: {len(result.get('browser_console_severe_errors', [])) if 'browser_console_severe_errors' in result else 'see trace/failure'}; expected API-unavailable 503: {len(result.get('browser_console_expected_errors', []))}; unexpected: {len(result.get('browser_console_unexpected_errors', []))}.", f"- UI/API/raw comparisons: {result.get('csv_comparison_count', 0)}; failed: {result.get('csv_comparison_failures', 'not completed')}.", "", "## Browser operation trace", "", "| Time | Step | Expected | Actual | Status |", "|---|---|---|---|---|"]
        for step in steps:
            lines.append(f"| {step['time']} | {step['name']} | {step['expected']} | {step['actual']} | {step['status']} |")
        lines.extend(["", "Detailed API responses, Network statuses, source hashes, and runtime metadata: `M4_UAT_EVIDENCE/browser_uat_trace.json`.", ""])
        (ROOT / "M4_FD001_BROWSER_UAT.md").write_text("\n".join(lines), encoding="utf-8")

    print(json.dumps({"status": result["status"], "url": WEB_URL, "browser": result["browser"], "steps": len(steps), "comparisons": result["csv_comparison_count"], "screenshots": len(list(EVIDENCE.glob("uat-*.png"))), "console_errors": len(result["browser_console_severe_errors"])}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
