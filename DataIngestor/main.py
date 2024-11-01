import argparse
from loguru import logger
from utils import ingest_from_web


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str)

    args = parser.parse_args()
    logger.info(f"URL RECEIVED IS {args.url}")
    ingest_from_web(args.url)