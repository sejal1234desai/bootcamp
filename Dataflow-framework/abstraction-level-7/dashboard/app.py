# dashboard/app.py

# dashboard/app.py
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

app = None  # Global placeholder
metrics_store = None
trace_store = None

def init_dashboard(metrics, traces):
    global app, metrics_store, trace_store
    metrics_store = metrics
    trace_store = traces

    app = FastAPI()

    @app.get("/")
    async def read_root():
        return {"message": "Welcome to the dashboard!"}

    @app.get("/stats")
    async def get_stats():
        return JSONResponse(content=metrics_store.get_metrics())

    @app.get("/trace")
    async def get_trace():
        return JSONResponse(content=trace_store.get_traces())

    @app.get("/errors")
    async def get_errors():
        return JSONResponse(content={
            processor: m["errors"] for processor, m in metrics_store.get_metrics().items()
        })

def run_dashboard():
    uvicorn.run(app, host="127.0.0.1", port=8000)
