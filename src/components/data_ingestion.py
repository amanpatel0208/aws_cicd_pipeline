import os
import sys
from src.exceptions import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# when we use dataclass we don't need to
# define init method and we can directly define
# our class variables
@dataclass
class DataIngestionConfig:
    # we can define a config entity directly but we define here
    train_data_path:str = os.path.join('artifact','train.csv')
    # we give this path for the data ingestion output 
    # to store the train data output in this path
    # we will create a artifacts dir for storing all the outputs
    test_data_path:str = os.path.join('artifact','test.csv')
    raw_data_path:str = os.path.join('artifact','raw.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        # if my data in some databases 
        # the code to read the data will be here
        logging.info('eneterd the data ingestion component')
        try:
            df=pd.read_csv('/Users/amanarifpatel/Documents/ml_project/notebook/data/stud.csv')
            logging.info('read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info('train_test_split initiated')
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('ingestion of data complete')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        # now my. data transformation part weill take this directly from dataingestion class
        # and perform transformtion
        except Exception as e:
            raise CustomException(e,sys)
            

if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()