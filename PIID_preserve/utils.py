import spacy
from loguru import logger
from .constants import RETURN_DICT, REPLACEMENT_DICT
from typing import List, Dict


def perform_NER(
    raw_text: str, 
    nlp, 
    replacement_dict: Dict, 
    return_dict: Dict
) -> str:
    docs = nlp(raw_text)

    modified_text = raw_text

    for ents in docs.ents:
        logger.debug(f"Entity Detected {ents.text} | {ents.label_}")
        if ents.label_ in replacement_dict.keys():

            modified_text = modified_text.replace(
                ents.text, 
                replacement_dict[ents.label_]
            )

            return_dict[ents.label_].append(ents.text)

    logger.info(f"NEW TEXT | {modified_text}")

    return modified_text, return_dict