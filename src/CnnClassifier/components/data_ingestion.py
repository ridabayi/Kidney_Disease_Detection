import kaggle
import os
import zipfile
import gdown
from CnnClassifier import logger
from CnnClassifier.utils.common import get_size
from CnnClassifier.entity.config_entity import (DataIngestionConfig)



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self) -> str:
        '''
        Fetch data from Kaggle
        '''
        try: 
            dataset_name = self.config.source_URL  # should be in the format "owner/dataset-name"
            zip_download_dir = self.config.local_data_file
            os.makedirs(os.path.dirname(zip_download_dir), exist_ok=True)
            logger.info(f"Downloading dataset {dataset_name} into file {zip_download_dir}")

            kaggle.api.dataset_download_files(
            'nazmul0087/ct-kidney-dataset-normal-cyst-tumor-and-stone',
            path='artifacts/data_ingestion/',
            unzip=True)

            logger.info(f"Downloaded dataset {dataset_name} into {zip_download_dir}")

        except Exception as e:
            raise e

    def extract_zip_file(self):
        """
        Extracts the zip file into the data directory
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)