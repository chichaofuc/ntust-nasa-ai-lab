# M4 FD001 Startup and URL

## Verified environment

- Workspace: `C:\Users\as555\Desktop\20261123_AI\20261123_AI`
- Python: 3.13.14
- Frontend: static HTML/CSS/JavaScript; no npm packages or external assets required.
- API: existing `M3_FD001_api.py`; do not change it for M4.
- Browser UAT dependency: Selenium 4.35.0, already available in the verified Python environment.
- Browser used for UAT: Brave (Chromium) 158.0.8127.92.

## Start the application

Open two PowerShell terminals.

Terminal 1 — start the existing M3 API:

```powershell
Set-Location 'C:\Users\as555\Desktop\20261123_AI\20261123_AI'
$env:FD001_API_PORT = '18766'
python M3_FD001_api.py
```

Terminal 2 — start the M4 UI host and same-origin API proxy:

```powershell
Set-Location 'C:\Users\as555\Desktop\20261123_AI\20261123_AI'
python M4_FD001_web_server.py --host 127.0.0.1 --port 18767 --api-base http://127.0.0.1:18766
```

Open the actual local URL:

- Frontend: http://127.0.0.1:18767/
- API through the M4 host: http://127.0.0.1:18767/api/health
- Direct local M3 API: http://127.0.0.1:18766/api/health

These ports and URL were exercised by the actual Brave/Selenium UAT on 2026-11-27; see `M4_FD001_BROWSER_UAT.md` and `M4_UAT_EVIDENCE/browser_uat_trace.json`.

## Stop

Press `Ctrl+C` in each terminal running the API and M4 host. The UAT automation starts and stops its own child processes and browser when it exits.

## Re-run checks

```powershell
Set-Location 'C:\Users\as555\Desktop\20261123_AI\20261123_AI'
python -m unittest -v test_M4_frontend
python M4_FD001_browser_uat.py
```

The browser UAT opens the installed Brave browser and requires Selenium 4.35.0. The production web UI itself has no Python package dependency beyond the existing M3 API runtime and Python standard library.
