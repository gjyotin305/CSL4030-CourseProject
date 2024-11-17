import tiktoken
import spacy
import os
from loguru import logger
from datasets import Dataset
from .utils import text_splitter
from DataIngestor.utils import ingest_from_web
from PIID_preserve.utils import perform_NER
from PIID_preserve.constants import REPLACEMENT_DICT, RETURN_DICT
from typing import AnyStr
from spacy.pipeline import EntityRuler


def pipeline_populate_db(url: AnyStr, name_dataset: str) -> bool:
    logger.info("STEP 1 OF PIPELINE - DATA INGESTION")

    status, raw_data = ingest_from_web(
        url=url
    )

    logger.info("STEP 2 OF PIPELINE - TEXT SPLITTING")

    chunks, _ = text_splitter(
        raw_text=raw_data
    )

    logger.info("STEP 3 OF PIPELINE - PERFORMING NER FOR PIID REPLACEMENT")

    nlp = spacy.load("en_core_web_sm")
    ruler = nlp.add_pipe("entity_ruler", before="ner")
    patterns = [
        {"label": "NAME", "pattern": [{"POS": "PROPN"}]},  # Example for proper nouns
        {"label": "MOBILE", "pattern": [{"TEXT": {"REGEX": r"^\+?\d{10,15}$"}}]},  # Mobile number pattern
        {"label": "EMAIL", "pattern": [{"TEXT": {"REGEX": r"^[\w\.-]+@[\w\.-]+\.\w{2,4}$"}}]},  # Email pattern
    ]
    ruler.add_patterns(patterns)

    hidden_chunks = []
    for chunk in chunks:
        modified_chunk, _ = perform_NER(
            raw_text=chunk, 
            nlp=nlp, 
            replacement_dict=REPLACEMENT_DICT, 
            return_dict=RETURN_DICT.copy()
        )
        
        logger.info(f"MODIFIED CHUNK | {modified_chunk}")
        
        hidden_chunks.append(modified_chunk)

    logger.info(f"NUMBER OF MODIFIED CHUNKS | {len(hidden_chunks)}")

    token_length = [200 for i in range(0, len(hidden_chunks))]

    logger.info(f"STEP 5 | UPLOAD TO HUGGING FACE WITH YOUR MODIFIED DATA")

    dataset__ = {
        "text": hidden_chunks,
        "token_length": token_length
    }

    dataset_hf = Dataset.from_dict(dataset__)

    dataset_hf.push_to_hub(
        f"gjyotin305/{name_dataset}", 
        token=os.getenv("HF_API_KEY")
    )



