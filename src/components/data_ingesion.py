#will have all the code related to reading the data
#doubt from line 11 to 15 and on line 24 
import os
import sys
from src.exception import CustomException
from logger import logging
from sklearn.preprocessing import train_test_split
import pandas as pd
from dataclasses import dataclass

@dataclass## if you only have variables inside the class the you can use dataclass as does not require you to create __init__
class DataIngesionConfig:
    train_data_path: str=os.path.join('artifacts','train.csv')
    test_data_path: str=os.path.join('artifacts','test.csv')
    raw_data_path: str=os.path.join('artifacts','data.csv')

class DataIngesion:  #in this we wont use dataclass as we would be having methods inside 
    def __init__(self): 
        self.ingesion_config=DataIngesionConfig()
    def initiate_data_ingesion(self):
        logging.info('entered the data ingesion method or component')
        try:
            df=pd.read_csv('notebook/data/stud.csv')
            logging.info('read the dataset as dataframe')
            os.makedirs(os.path.dirname(self.ingesion_config.train_data_path),exist_ok=True)#as we know the path of train data here we are making the folders as in the artifacts folder

            df.to_csv(self.ingesion_config.raw_data_path,index=False,header=True)

            logging.info("initiated train test split")

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingesion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingesion_config.test_data_path,index=False,header=True)

            logging.info("ingesion of data is completed")

            return(

                self.ingesion_config.train_data_path,
                self.ingesion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=='__main__':
    obj=DataIngesion()
    obj.initiate_data_ingesion()

