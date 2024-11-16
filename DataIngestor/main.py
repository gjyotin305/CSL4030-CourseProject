import argparse
from loguru import logger
from fastapi import FastAPI
from pydantic import BaseModel
from utils import ingest_from_web

class UrlIngest(BaseModel):
    url: str

app = FastAPI()

@app.get("/")
def read_api():
    return {
        "message": "###############Group 20################"
    }


@app.post("/api/data-ingestor/")
def api_ingestion(url: UrlIngest):
    logger.info(f"URL RECEIVED IS {url.url}")
    
    bool_v, ingested = ingest_from_web(url=url.url)
    return {
        "message": f"Status: {bool_v}",
        "response": ingested
    }