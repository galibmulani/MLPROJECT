import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainer
from src.components.model_trainer import ModelTrainerConfig

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join("artifacts","train.csv")
    test_data_path: str=os.path.join("artifacts","test.csv")
    raw_data_path: str=os.path.join("artifacts","data.csv")

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Enter the data ingestion")
        os.chdir(r"C:\Users\galib\AI\Projects\MLPROJECT\src")
        try:
            df=pd.read_csv("notebooks\data\stud.csv")
            logging.info("reading the csv file")

            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.data_ingestion_config.raw_data_path,index=False,header=True)

            logging.info("train test split initiated..")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            
            train_set.to_csv(self.data_ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.data_ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed..")


            return (
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
            )

        except Exception  as e:
            raise CustomException(e,sys)
        

if __name__ == "__main__":
    obj=DataIngestion()
    train_path,test_path = obj.initiate_data_ingestion()
    obj_transformation=DataTransformation()
    train_arr,test_arr,_ = obj_transformation.initiate_data_transformation(train_path,test_path)
    modeltrainer=ModelTrainer()    
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))