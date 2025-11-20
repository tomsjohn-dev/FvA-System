```markdown
# FvA-System

Forecast automation system for reading forecast data and exposing a small HTTP API.

This repository provides a minimal FastAPI application that includes:
- a system healthcheck router (from `routes.healthcheck`)
- a forecast input / parsing router (from `routes.forecastRoute`, mounted under `/api`)
- a simple root endpoint (`GET /`) that returns a basic success payload

## Contents / Project Structure

- `main.py`        — FastAPI app, includes routers and root endpoint
- `server.py`      — small runner that starts uvicorn on port 5000
- `requirements.txt` — runtime dependencies
- `.gitignore`     — ignored files (e.g. `__pycache__`, `.env`)
- `routes/`        — HTTP route modules (e.g. `healthcheck`, `forecastRoute`)
- `controllers/`   — (empty/placeholder) controller modules
- `services/`      — (empty/placeholder) service modules

Inspect the `routes/` directory for more details about available endpoints and expected request payloads.

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`:
  - fastapi
  - uvicorn
  - psutil
  - pandas

## Install

1. Create and activate a virtual environment (recommended)

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .venv\Scripts\activate      # Windows (PowerShell)
   ```

2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

## Run (development)

Option 1 — use the provided runner:

```bash
python server.py
# This will run uvicorn with: uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
```

Option 2 — run uvicorn directly:

```bash
uvicorn main:app --host 0.0.0.0 --port 5000 --reload
```

By default the app listens on port 5000.

## Available endpoints (overview)

- `GET /`  
  Returns a small JSON payload showing the application is alive. From `main.py`:
  ```json
  {"status":200,"success":true}
  ```

- Healthcheck router: the health routes are registered from `routes.healthcheck`. Check that file for the exact path(s) (for example, `/health` or similar).

- Forecast input / parse routes: routes from `routes.forecastRoute` are included with prefix `/api`. Check `routes/forecastRoute.py` for the exact endpoint paths, request body schema, and response format.

Example (root health check):

```bash
curl -i http://localhost:5000/
```

Example (forecast route — replace `<path>` with the real endpoint from `routes/forecastRoute.py`):

```bash
curl -X POST http://localhost:5000/api/<forecast-endpoint> \
  -H "Content-Type: application/json" \
  -d '{"example":"payload"}'
```

## Notes for contributors / maintainers

- The app is intentionally minimal. Business logic likely lives in `routes/`, `controllers/`, and `services/`. Add unit tests and type hints as needed.
- `.env` is ignored by `.gitignore`. If environment configuration is required, add a `.env.example` and document required variables.
- The server runs with `reload=True` (development). For production, use a proper ASGI server setup (gunicorn + uvicorn workers, or a process manager).

## Troubleshooting

- If you see import errors for local modules, ensure the working directory is the repository root and the virtual environment is active.
- If ports are in use, change the `--port` or the value in `server.py`.

## License

Add a LICENSE file appropriate to your project. If you don't have one yet, consider `MIT`, `Apache-2.0`, or another permissive license.

```
