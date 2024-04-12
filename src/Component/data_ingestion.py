import os
import sys
import pandas as pd
sys.path.insert(0, os.curdir)
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path : str=os.path.join('artifacts','train.csv')
    test_data_path : str=os.path.join('artifacts','test.csv')
    raw_data_path : str=os.path.join('artifacts','Data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info('Entered the data Ingestion or component')
        try:
            df=pd.read_csv('Notebook\data\Stud.csv')
            logging.info('read dataset as a dataframe')
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info('Train Test Split Initited')

            train_data,test_data =train_test_split(df,test_size=0.2,random_state=42)

            train_data.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_data.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Ingestion of data is completed')

        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=='__main__':
    obj=DataIngestion()
    obj.initiate_data_ingestion()