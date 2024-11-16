from typing import AnyStr, Union
from loguru import logger
import validators
import random
import os
import requests

def ingest_from_web(url: AnyStr) -> Union[bool, str]:
    if isinstance(validators.url(url), validators.ValidationError):
        logger.error(f"URL IS NOT VALID {url}")
        return False
    else:
        logger.info(f"URL IS VALID {url}")
    
    prefix = "https://r.jina.ai/"

    final_url = prefix + url
    headers = {'Authorization': f'Bearer {os.getenv("JINAI_API_KEY")}'}

    logger.debug(f"FINAL URL {final_url}")

    response = requests.get(final_url, headers=headers)
    filename = f"logs/scraped_{random.randint(696, 6969)}.log"

    with open(filename, "w") as f:
        f.write(response.text)
        logger.info(f"WRITING SCRAPED LOGS IN {filename}")
        f.close()

    return True, response.text
