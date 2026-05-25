import logging
from pathlib import Path

from etl.extract import extract_sources
from etl.transform import build_model
from etl.validation import validate_model
from etl.load import save_model
from etl.notifications import notify_error

logging.basicCondifig(
    filename="logs/etl.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)

INPUT_DIR = "data/input"
OUTPUT_DIR = "data/output"

def run():
    logger = logging.getLogger("main_etl")
    try:
        logger.info("Start ETL")
        sources = extract_sources(INPUT_DIR)
        model = build_model(
            sources["sales"],
            sources["reseller"],
            sources["region"],
            sources["products"]
        )
        validate_model(model)
        save_model(model, OUTPUT_DIR)
        logger.info("ETL completed successfully")
    except Exception as e:
        msg = f"ETL failed: {e}"
        logger.exception(msg)
        notify_error(msg)
        raise

if __name__ == "__main__":
    run()