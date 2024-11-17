import spacy
from fastapi import FastAPI
from pydantic import BaseModel
from constants import REPLACEMENT_DICT, RETURN_DICT
from loguru import logger
from utils import perform_NER

from spacy.pipeline import EntityRuler

nlp = spacy.load("en_core_web_sm")

ruler = nlp.add_pipe("entity_ruler", before="ner")

patterns = [
    {"label": "NAME", "pattern": [{"POS": "PROPN"}]},  # Example for proper nouns
    {"label": "MOBILE", "pattern": [{"TEXT": {"REGEX": r"^\+?\d{10,15}$"}}]},  # Mobile number pattern
    {"label": "EMAIL", "pattern": [{"TEXT": {"REGEX": r"^[\w\.-]+@[\w\.-]+\.\w{2,4}$"}}]},  # Email pattern
]

ruler.add_patterns(patterns)

class TagAndReplace(BaseModel):
    raw_text: str

app = FastAPI()

@app.get("/")
def read_api():
    return {
        "message": "#############Group-20#############"
    }


@app.post("/api/pipeline/")
def api_ner(arguments: TagAndReplace):
    logger.info(f"RAW TEXT RECEIVED IS | {arguments.raw_text[:100]}")

    modified_text, return_ = perform_NER(
        raw_text=arguments.raw_text, 
        nlp=nlp, 
        replacement_dict=REPLACEMENT_DICT,
        return_dict=RETURN_DICT.copy()
    )

    return {
        "text" : modified_text,
        "tags": return_
    }

