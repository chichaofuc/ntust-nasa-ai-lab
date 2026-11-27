(() => {
  "use strict";

  const $ = (id) => document.getElementById(id);
  const nodes = {
    split: $("split-select"), unit: $("unit-select"), sensor: $("sensor-select"),
    start: $("start-input"), end: $("end-input"), form: $("query-form"), apply: $("apply-button"),
    notice: $("notice"), queryState: $("query-state"), healthLabel: $("health-label"),
    count: $("count-value"), countDetail: $("count-detail"), window: $("window-value"),
    windowDetail: $("window-detail"), source: $("source-value"), sourceDetail: $("source-detail"),
    trace: $("trace-value"), traceDetail: $("trace-detail"), bounds: $("cycle-bounds"),
    chartTitle: $("sensor-title"), chartCaption: $("chart-caption"), chart: $("trend-chart"),
    chartWrap: $("chart-wrap"), chartEmpty: $("chart-empty"), pointDetail: $("point-detail"),
    tableWrap: $("table-wrap"), tableEmpty: $("table-empty"), tableBody: $("records-body"),
    tableCount: $("table-count"), contract: $("contract-version"), liveDot: document.querySelector(".live-dot"),
  };
  const state = { catalog: null, units: [], records: [], selectedPoint: null, generation: 0 };
  const SVG = "http://www.w3.org/2000/svg";

  class APIError extends Error {
    constructor(status, code, message) { super(message); this.status = status; this.code = code; }
  }

  async function getJSON(path) {
    const response = await fetch(path, { method: "GET", headers: { Accept: "application/json" }, cache: "no-store" });
    let body;
    try { body = await response.json(); }
    catch { throw new APIError(response.status, "INVALID_RESPONSE", "API returned a response that was not valid JSON."); }
    if (!response.ok || body.ok !== true) {
      const error = body.error || {};
      throw new APIError(response.status, error.code || "API_ERROR", error.message || "The API request failed.");
    }
    return body;
  }

  function setNotice(message, kind = "") {
    nodes.notice.className = `notice${kind ? ` is-${kind}` : ""}`;
    nodes.notice.lastElementChild.textContent = message;
  }

  function setQueryState(message, kind) {
    nodes.queryState.textContent = message;
    nodes.queryState.className = `state-pill state-${kind}`;
  }

  function clearResults() {
    state.records = [];
    state.selectedPoint = null;
    nodes.chart.replaceChildren();
    nodes.chartWrap.hidden = true;
    nodes.chartEmpty.hidden = false;
    nodes.chartEmpty.querySelector("strong").textContent = "Choose a view to begin";
    nodes.chartEmpty.querySelector("span").textContent = "Chart points will come directly from the selected API response.";
    nodes.tableBody.replaceChildren();
    nodes.tableWrap.hidden = true;
    nodes.tableEmpty.hidden = false;
    nodes.tableEmpty.textContent = "No observations loaded. Apply a valid split, Unit, Sensor and Cycle range.";
    nodes.count.textContent = "—";
    nodes.countDetail.textContent = "Cycle rows returned";
    nodes.window.textContent = "—";
    nodes.windowDetail.textContent = "Inclusive range";
    nodes.source.textContent = "—";
    nodes.sourceDetail.textContent = "Original source";
    nodes.trace.textContent = "Awaiting query";
    nodes.traceDetail.textContent = "Physical line mapping";
    nodes.tableCount.textContent = "0 rows";
    nodes.chartTitle.textContent = "";
    nodes.chartCaption.textContent = "—";
    nodes.pointDetail.className = "point-detail";
    nodes.pointDetail.innerHTML = "<span class=\"detail-kicker\">POINT INSPECTION</span><strong>Select a plotted point</strong><span>Hover for a quick read; click a point to pin its source row.</span>";
  }

  function appendOption(select, value, label) {
    const option = document.createElement("option");
    option.value = String(value);
    option.textContent = label;
    select.append(option);
  }

  function currentUnit() {
    return state.units.find((unit) => unit.unit_id === Number(nodes.unit.value));
  }

  function setCycleBounds(unit, reset = true) {
    if (!unit) return;
    nodes.start.min = String(unit.first_cycle);
    nodes.start.max = String(unit.last_cycle);
    nodes.end.min = String(unit.first_cycle);
    nodes.end.max = String(unit.last_cycle);
    nodes.bounds.textContent = `${unit.first_cycle}–${unit.last_cycle}`;
    if (reset) {
      nodes.start.value = String(unit.first_cycle);
      nodes.end.value = String(unit.last_cycle);
    }
  }

  function formatValue(value) {
    if (value === null) return "null";
    return String(value);
  }

  function svgElement(tag, attrs = {}, text = null) {
    const element = document.createElementNS(SVG, tag);
    for (const [key, value] of Object.entries(attrs)) element.setAttribute(key, String(value));
    if (text !== null) element.textContent = text;
    return element;
  }

  function showPoint(record, pinned = false, index = null) {
    nodes.pointDetail.className = `point-detail${pinned ? " is-pinned" : ""}`;
    nodes.pointDetail.replaceChildren();
    const kicker = document.createElement("span"); kicker.className = "detail-kicker"; kicker.textContent = pinned ? "PINNED SOURCE ROW" : "POINT INSPECTION";
    const title = document.createElement("strong"); title.textContent = `Cycle ${record.cycle} · ${formatValue(record.value)}`;
    const provenance = document.createElement("span"); provenance.textContent = `${record.source_file} · physical line ${record.source_line}`;
    nodes.pointDetail.append(kicker, title, provenance);
    if (index !== null) state.selectedPoint = index;
  }

  function selectRow(index) {
    state.selectedPoint = index;
    const record = state.records[index];
    if (!record) return;
    nodes.chart.querySelectorAll(".trend-point").forEach((point) => point.classList.toggle("is-selected", Number(point.dataset.index) === index));
    nodes.tableBody.querySelectorAll("tr").forEach((row) => row.classList.toggle("is-selected", Number(row.dataset.index) === index));
    showPoint(record, true, index);
  }

  function renderChart(records) {
    nodes.chart.replaceChildren();
    if (!records.length) {
      nodes.chartWrap.hidden = true;
      nodes.chartEmpty.hidden = false;
      nodes.chartEmpty.querySelector("strong").textContent = "No observations in this response";
      nodes.chartEmpty.querySelector("span").textContent = "The API returned zero rows for this valid query.";
      return;
    }
    nodes.chartEmpty.hidden = true;
    nodes.chartWrap.hidden = false;
    const width = 1000, height = 350, left = 66, right = 22, top = 18, bottom = 52;
    const plotW = width - left - right, plotH = height - top - bottom;
    const cycles = records.map((r) => r.cycle);
    const values = records.map((r) => r.value).filter((v) => typeof v === "number" && Number.isFinite(v));
    if (values.length !== records.length) throw new APIError(500, "INVALID_RESPONSE", "API returned a missing or non-finite sensor value.");
    let minY = Math.min(...values), maxY = Math.max(...values);
    if (minY === maxY) { const padding = Math.abs(minY) * 0.02 || 1; minY -= padding; maxY += padding; }
    const minX = Math.min(...cycles), maxX = Math.max(...cycles);
    const x = (cycle) => left + (maxX === minX ? plotW / 2 : ((cycle - minX) / (maxX - minX)) * plotW);
    const y = (value) => top + ((maxY - value) / (maxY - minY)) * plotH;
    const defs = svgElement("defs");
    const gradient = svgElement("linearGradient", { id: "trend-fill", x1: "0", x2: "0", y1: "0", y2: "1" });
    gradient.append(svgElement("stop", { offset: "0%", "stop-color": "#76cbbb", "stop-opacity": ".31" }), svgElement("stop", { offset: "100%", "stop-color": "#76cbbb", "stop-opacity": "0" }));
    defs.append(gradient); nodes.chart.append(defs);
    for (let tick = 0; tick <= 4; tick++) {
      const fraction = tick / 4, py = top + fraction * plotH, value = maxY - fraction * (maxY - minY);
      nodes.chart.append(svgElement("line", { x1: left, x2: width - right, y1: py, y2: py, class: "grid-line" }));
      nodes.chart.append(svgElement("text", { x: left - 12, y: py + 4, "text-anchor": "end", class: "axis-text" }, formatValue(value)));
    }
    nodes.chart.append(svgElement("line", { x1: left, x2: width - right, y1: height - bottom, y2: height - bottom, class: "axis-line" }));
    const tickCount = Math.min(6, records.length);
    for (let tick = 0; tick < tickCount; tick++) {
      const itemIndex = tickCount === 1 ? 0 : Math.round((tick / (tickCount - 1)) * (records.length - 1));
      const px = x(records[itemIndex].cycle);
      nodes.chart.append(svgElement("line", { x1: px, x2: px, y1: height - bottom, y2: height - bottom + 5, class: "axis-line" }));
      nodes.chart.append(svgElement("text", { x: px, y: height - bottom + 21, "text-anchor": "middle", class: "axis-text" }, String(records[itemIndex].cycle)));
    }
    nodes.chart.append(svgElement("text", { x: left, y: 13, class: "axis-caption" }, "SENSOR VALUE · UNIT UNKNOWN"));
    nodes.chart.append(svgElement("text", { x: width - right, y: height - 9, "text-anchor": "end", class: "axis-caption" }, "CYCLE"));
    const points = records.map((record) => [x(record.cycle), y(record.value)]);
    const linePath = points.map(([px, py], index) => `${index ? "L" : "M"}${px.toFixed(2)},${py.toFixed(2)}`).join(" ");
    const areaPath = `${linePath} L${points.at(-1)[0].toFixed(2)},${(height - bottom).toFixed(2)} L${points[0][0].toFixed(2)},${(height - bottom).toFixed(2)} Z`;
    nodes.chart.append(svgElement("path", { d: areaPath, class: "trend-area" }), svgElement("path", { d: linePath, class: "trend-line" }));
    records.forEach((record, index) => {
      const point = svgElement("circle", { cx: points[index][0], cy: points[index][1], r: records.length > 180 ? 2.1 : 3.4, class: `trend-point${state.selectedPoint === index ? " is-selected" : ""}`, tabindex: "0", role: "button", "aria-label": `Cycle ${record.cycle}, value ${record.value}, source line ${record.source_line}`, "data-index": index });
      const title = svgElement("title", {}, `Cycle ${record.cycle} · ${record.value} · ${record.source_file} line ${record.source_line}`);
      point.append(title);
      point.addEventListener("mouseenter", () => showPoint(record, false));
      point.addEventListener("focus", () => showPoint(record, false));
      point.addEventListener("click", () => selectRow(index));
      point.addEventListener("keydown", (event) => { if (event.key === "Enter" || event.key === " ") { event.preventDefault(); selectRow(index); } });
      nodes.chart.append(point);
    });
  }

  function renderTable(records) {
    nodes.tableBody.replaceChildren();
    if (!records.length) {
      nodes.tableWrap.hidden = true;
      nodes.tableEmpty.hidden = false;
      nodes.tableEmpty.textContent = "No observations were returned for this query.";
      nodes.tableCount.textContent = "0 rows";
      return;
    }
    nodes.tableEmpty.hidden = true;
    nodes.tableWrap.hidden = false;
    const fragment = document.createDocumentFragment();
    records.forEach((record, index) => {
      const row = document.createElement("tr"); row.dataset.index = String(index); row.tabIndex = 0;
      const values = [record.cycle, record.unit_id, record.sensor_id, record.sensor_field, record.raw_column_index, formatValue(record.value), record.source_file, record.source_line];
      values.forEach((value, cellIndex) => { const cell = document.createElement("td"); cell.textContent = String(value); if (cellIndex === 6) cell.className = "source-cell"; row.append(cell); });
      row.addEventListener("click", () => selectRow(index));
      row.addEventListener("keydown", (event) => { if (event.key === "Enter" || event.key === " ") { event.preventDefault(); selectRow(index); } });
      fragment.append(row);
    });
    nodes.tableBody.append(fragment);
    nodes.tableCount.textContent = `${records.length} rows`;
  }

  function validateRange() {
    const unit = currentUnit();
    if (!unit) return "Select an available Engine Unit.";
    const rawStart = nodes.start.value.trim(), rawEnd = nodes.end.value.trim();
    if (!/^[+-]?\d+$/.test(rawStart) || !/^[+-]?\d+$/.test(rawEnd)) return "Cycle values must be whole numbers.";
    const start = Number(rawStart), end = Number(rawEnd);
    if (!Number.isSafeInteger(start) || !Number.isSafeInteger(end)) return "Cycle values are outside the supported integer range.";
    if (start > end) return "Start Cycle must be less than or equal to End Cycle.";
    if (start < unit.first_cycle || end > unit.last_cycle) return `Choose a range within this Unit's observed Cycles (${unit.first_cycle}–${unit.last_cycle}).`;
    return null;
  }

  async function loadView(token = ++state.generation) {
    clearResults();
    const problem = validateRange();
    if (problem) {
      setQueryState("Check range", "error"); setNotice(problem, "error");
      nodes.tableEmpty.textContent = "The range was rejected. No previous observations are retained.";
      return;
    }
    const split = nodes.split.value, unit = Number(nodes.unit.value), sensor = Number(nodes.sensor.value);
    const start = Number(nodes.start.value), end = Number(nodes.end.value);
    nodes.apply.disabled = true; setQueryState("Loading observations", "loading");
    setNotice("Requesting this exact inclusive range from the M3 read-only API…");
    try {
      const body = await getJSON(`/api/history?split=${encodeURIComponent(split)}&unit=${unit}&sensor=${sensor}&start=${start}&end=${end}`);
      if (token !== state.generation) return;
      const data = body.data;
      if (!Array.isArray(data.records) || data.actual_count !== data.records.length) throw new APIError(500, "INVALID_RESPONSE", "API record count did not match the response rows.");
      if (data.records.some((record) => record.split !== split || record.unit_id !== unit || record.sensor_id !== sensor || record.cycle < start || record.cycle > end)) throw new APIError(500, "INVALID_RESPONSE", "API records did not match the selected query.");
      state.records = data.records;
      renderChart(state.records); renderTable(state.records);
      nodes.count.textContent = String(data.actual_count);
      nodes.countDetail.textContent = `${split.toUpperCase()} · Unit ${unit} · ${data.sensor.sensor_field}`;
      nodes.window.textContent = `${start}–${end}`;
      nodes.windowDetail.textContent = "Inclusive Cycle range";
      nodes.source.textContent = data.records[0]?.source_file || "No rows";
      nodes.sourceDetail.textContent = "Source file returned by M3 API";
      nodes.trace.textContent = data.records.length ? "Available" : "No rows";
      nodes.traceDetail.textContent = data.records.length ? `${data.records[0].source_line}–${data.records.at(-1).source_line} physical lines` : "No source rows returned";
      nodes.chartTitle.textContent = `· ${data.sensor.sensor_field}`;
      nodes.chartCaption.textContent = `${split.toUpperCase()} / Unit ${unit} / Sensor ${sensor} / Cycles ${start}–${end} / ${data.actual_count} points`;
      nodes.tableEmpty.textContent = data.records.length ? "" : "The API returned no observations for this valid query.";
      if (data.records.length) { setQueryState("View ready", "ready"); setNotice("Chart and table use the same M3 API response. Select a point or row to inspect its original source line.", "success"); }
      else { setQueryState("No observations", "error"); setNotice("The API returned no records for this range. Previous results were cleared.", "error"); }
    } catch (error) {
      if (token !== state.generation) return;
      clearResults();
      setQueryState(error instanceof APIError && error.status === 400 ? "Check query" : "API unavailable", "error");
      setNotice(`${error.code || "NETWORK_ERROR"}: ${error.message || "Could not reach the M3 API."} Previous results were cleared.`, "error");
      nodes.tableEmpty.textContent = "No data shown because the current request failed. Previous observations are cleared.";
    } finally {
      if (token === state.generation) nodes.apply.disabled = false;
    }
  }

  async function loadSplit(split, token) {
    clearResults();
    nodes.unit.disabled = true; nodes.start.disabled = true; nodes.end.disabled = true; nodes.apply.disabled = true;
    setQueryState("Loading Units", "loading"); setNotice(`Loading ${split.toUpperCase()} Unit options from the M3 API…`);
    try {
      const body = await getJSON(`/api/units?split=${encodeURIComponent(split)}`);
      if (token !== state.generation) return;
      state.units = body.data.units;
      nodes.unit.replaceChildren();
      for (const item of state.units) appendOption(nodes.unit, item.unit_id, `Unit ${item.unit_id} · ${item.first_cycle}–${item.last_cycle} cycles`);
      nodes.unit.disabled = false;
      if (!state.units.length) throw new APIError(500, "INVALID_RESPONSE", "The API returned no Units for the selected split.");
      setCycleBounds(state.units[0], true);
      nodes.start.disabled = false; nodes.end.disabled = false; nodes.apply.disabled = false;
      await loadView(token);
    } catch (error) {
      if (token !== state.generation) return;
      clearResults(); setQueryState("API unavailable", "error");
      setNotice(`${error.code || "NETWORK_ERROR"}: ${error.message || "Could not load Units from the M3 API."}`, "error");
    }
  }

  async function initialize() {
    const token = ++state.generation;
    clearResults(); setQueryState("Validating sources", "loading"); setNotice("Checking API health and loading the verified catalog…");
    try {
      const [health, catalog] = await Promise.all([getJSON("/api/health"), getJSON("/api/catalog")]);
      if (token !== state.generation) return;
      if (health.data.data_loaded !== true || health.data.source_validation !== "PASS") throw new APIError(503, "DATA_SOURCE_UNAVAILABLE", "The API did not validate all source data.");
      state.catalog = catalog.data;
      nodes.healthLabel.textContent = "Verified FD001 sources connected"; nodes.liveDot.classList.add("is-live");
      nodes.contract.textContent = catalog.data.contract_version;
      nodes.sensor.replaceChildren();
      for (const sensor of catalog.data.sensors) appendOption(nodes.sensor, sensor.sensor_id, `Sensor ${sensor.sensor_id} · ${sensor.sensor_field} · raw ${sensor.raw_column_index}`);
      nodes.split.disabled = false; nodes.sensor.disabled = false;
      await loadSplit(nodes.split.value, token);
    } catch (error) {
      if (token !== state.generation) return;
      nodes.healthLabel.textContent = "FD001 API unavailable"; nodes.liveDot.classList.remove("is-live");
      clearResults(); setQueryState("API unavailable", "error");
      setNotice(`${error.code || "NETWORK_ERROR"}: ${error.message || "Could not connect to the M3 API."}`, "error");
    }
  }

  nodes.split.addEventListener("change", () => loadSplit(nodes.split.value, ++state.generation));
  nodes.unit.addEventListener("change", () => {
    const token = ++state.generation; clearResults(); setCycleBounds(currentUnit(), true);
    nodes.start.disabled = false; nodes.end.disabled = false; loadView(token);
  });
  nodes.sensor.addEventListener("change", () => loadView(++state.generation));
  nodes.form.addEventListener("submit", (event) => { event.preventDefault(); loadView(++state.generation); });
  initialize();
})();
