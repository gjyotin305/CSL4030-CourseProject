import argparse
from loguru import logger
from fastapi import FastAPI
from utils import ingest_from_web

app = FastAPI()

@app.get("/api/data-ingestor/{url}")
def api_ingestion(url: str):
    bool_v = ingest_from_web(url=url)
    return {
        "message": f"Status: {bool_v}"
    }