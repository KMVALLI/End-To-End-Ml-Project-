# this contain  relateded to reading the data  from other scorcese like reading the data from data base or n  files or etc...
#this is importent role to perform a eda 


import os 
import sys # for using exeception handeling 
from src.exception import CoustomException
from src.logger import logging
import pandas as pd 
from sklearn.model_selection import train_test_split



from dataclasses import dataclass

# hear we are creating crating a folder structure for artifacts in current folder directrey 
@dataclass 
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts',"train.csv")
    test_data_path: str = os.path.join('artifats',"test.csv")
    rew_data_path: str = os.path.join('artifacts',"data.csv")

class DataIngestion: 
    def __init__(self):
        self.ingestion_congif = DataIngestionConfig()   # hear we are calling DataIngestionConfig class and 
    def  initiate_data_ingestion(self): # from hear we are taking the data  imput data  from anyb where actually hear we will call the data 
        logging.info("enterded the data igention method or components ")
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info("read the data set in the as data frame ")

            os.makedirs(os.path.dirname(self.ingestion_congif.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_congif.rew_data_path,index=False,header=True)
            logging.info("train test is initiateded ")

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_congif.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_congif.test_data_path,index=False,header=True)

            return(
                self.ingestion_congif.train_data_path,
                self.ingestion_congif.test_data_path
            )

        except Exception as e:
            raise CoustomException(e,sys)
           
if __name__=="__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()

