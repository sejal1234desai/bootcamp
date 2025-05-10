from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.metrics import MetricsStore
from app.trace import TraceStore
from app.processor_engine import ProcessorEngine

app = FastAPI()

metrics_store = MetricsStore()
trace_store = TraceStore()

processor_engine = ProcessorEngine(metrics_store, trace_store)

@app.get("/stats")
async def get_stats():
    return JSONResponse(content=metrics_store.get_metrics())

@app.get("/trace")
async def get_trace():
    return JSONResponse(content=trace_store.get_traces())

@app.get("/errors")
async def get_errors():
    return JSONResponse(content={
        processor: metrics["errors"] for processor, metrics in metrics_store.get_metrics().items()
    })

@app.get("/run-test")
async def run_test():
    # This is just for testing your dashboard
    processor_engine.process_lines(["hello", "world"])
    return {"message": "Processed test data"}
