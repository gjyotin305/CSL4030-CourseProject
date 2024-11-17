from typing import List, Union
from loguru import logger
import tiktoken

def text_splitter(
    raw_text: str, 
    split_size: int = 200
) -> Union[List[str], int]:
    enc = tiktoken.get_encoding("cl100K_base")
    tokens = enc.encode(raw_text)
    logger.info(f"Number of Tokens {len(tokens)}")

    chunks = [tokens[i: i+split_size] for i in range(0, len(tokens), split_size)]
    text_chunks = [enc.decode(chunk) for chunk in chunks]

    logger.info(f"Number of Chunks made {len(text_chunks)}")

    return text_chunks, split_size

