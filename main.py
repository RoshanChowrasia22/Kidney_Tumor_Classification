from src.cnnClassifier import logger
from src.cnnClassifier.components.data_ingestion import *
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline


STAGE_NAME="Data Ingestion stage"
try:
    logger.info(f"Stage {STAGE_NAME} started")
    obj=DataIngestionPipeline()
    obj.main()
    logger.info(f"Stage {STAGE_NAME} completed" )
except Exception as e:
    logger.exception(e)
    raise e