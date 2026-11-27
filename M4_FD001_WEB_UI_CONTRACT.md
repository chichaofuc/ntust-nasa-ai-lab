# M4 FD001 Interactive Web UI Contract

## Page and data flow

The local page is `web/index.html`, with behavior in `web/app.js` and presentation in `web/styles.css`. It presents source selection, a trend chart, and a provenance table. Production data flows only from the accepted M3 API. The UI does not read the FD001 text files, store static API responses, mock values, or derive data independently.

The M4 host serves static assets and acts as a transparent same-origin transport proxy for `/api/*` to the configured M3 API base URL. It forwards GET path/query and the upstream response status, content type, and body unchanged. It does not read datasets, calculate values, or introduce data endpoints. This is required because the accepted M3 API does not set browser CORS headers; modifying M3 is outside M4 scope. If the upstream is unavailable, the host returns a transport-level `DATA_SOURCE_UNAVAILABLE` response with HTTP 503.

```text
Browser controls → GET /api/* on local M4 host → unchanged forwarding to M3 API
       ↑                                                  ↓
Chart and table ← same returned history JSON ← M3 validated FD001 sources
```

## Controls and behavior

- **Split:** Train/Test. On change, prior chart/table results clear, then `/api/units?split=...` supplies Unit options.
- **Engine Unit:** options and per-Unit first/last Cycle bounds come from the selected split's Units response. A Unit change resets the inputs to that Unit's actual range and clears old observations.
- **Cycle start/end:** integer inputs with actual Unit bounds. Client rejects malformed, reversed, or out-of-range values and clears old rows. The request range is inclusive; the M3 API also validates it.
- **Sensor:** options come from `/api/catalog`. Labels show API's 1-based Sensor ID, canonical field, and 0-based raw column index. For example, Sensor 7 → `sensor_07` → index 11.
- **Update view:** requests the exact current split/Unit/Sensor/range. A new request clears previous results first. Generation tokens discard late responses from older selections.
- **Loading, empty and error states:** appear in the status area; failures clear chart, table, and summary so previous data cannot be mistaken for current results. A valid empty API response shows an explicit empty state. The verified FD001 source is contiguous, so no empty source range was available in this UAT.

## API endpoints and parameters

- Startup health/catalog: `GET /api/health`, `GET /api/catalog`.
- Unit options: `GET /api/units?split=train|test`.
- Observations: `GET /api/history?split={train|test}&unit={unit_id}&sensor={sensor_id}&start={cycle}&end={cycle}`.
- The page uses only GET and calls the M3 API through the transparent host proxy. No frontend CSV reads or independent data calculations are permitted.

## Chart and table

The chart's x-axis is Cycle; y-axis is the actual Sensor value, labeled `unit unknown`. Each plotted point corresponds one-to-one, in the same order, with a record in the current API response and a table row. Hover/focus shows a quick read; clicking a point or row pins its provenance.

The table displays Cycle, Unit ID, Sensor ID, canonical Sensor field, value, relative source file, and original 1-based physical source line. Chart and table both derive from the same `data.records` array without smoothing, normalization, filtering, or imputation. The API returned no null sensor values; JSON null remains supported by response handling and is not replaced with zero.

## Provenance and semantic limits

Each displayed record uses M3 response fields: `split`, `unit_id`, `cycle`, `sensor_id`, `sensor_field`, `raw_column_index`, `value`, `source_file`, and `source_line`. The UI does not claim sensor physical meaning or units. It does not diagnose faults, infer RUL, or assert that the last Train Cycle is a physical failure.

RUL is not returned or attached to per-Cycle data. The API catalog states its positional Test Unit relationship and lack of an in-file Unit ID key.

## Configuration

`M4_FD001_web_server.py` defaults to browser host `127.0.0.1`, port `4173`, and upstream M3 base URL `http://127.0.0.1:8000`. Configure via `--host`, `--port`, `--api-base`, or environment variables `M4_WEB_HOST`, `M4_WEB_PORT`, and `M3_API_BASE_URL`. It only accepts loopback M3 API URLs. Do not expose the service on a public network.
