import requests
import tiktoken
import spacy
from datasets import Dataset
from utils import text_splitter
from DataIngestor.utils import ingest_from_web
from PIID_preserve.utils import perform_NER
from typing import AnyStr


def pipeline_populate_db(url: AnyStr) -> bool:
    enc = tiktoken.get_encoding("o200k_base")

    status, raw_data = ingest_from_web(
        url=url
    )

    chunks, _ = text_splitter(
        raw_text=raw_data
    )

    

