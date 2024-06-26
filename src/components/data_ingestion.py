import os 
import sys 
from src.exception import CustomException
from src.logger import logging
import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig


# .)By this blw decorator we will directly define our varbale in class insed of definng first constructor of __init__ .
@dataclass
class DataIngestionConfig:
  train_data_path:str = os.path.join('artifacts','train.csv')
  test_data_path:str = os.path.join('artifacts','test.csv')
  raw_data_path:str = os.path.join('artifacts','raw.csv')
  
  

class DataIngestion:
  def __init__(self):
    self.ingestion_config = DataIngestionConfig()
    
    # .)The blw fun will read the data , the data can e at any place like csv,api ,database .
  def initiate_data_ingestion(self):
    logging.info("Entered the data ingestion method or component")
    try:
      df = pd.read_csv('notebook\data\stud.csv')
      logging.info('Read the dataset as dataframe')
      
      os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
      
      df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
      
      logging.info("Train test split initiated")
      train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
      
      train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
      test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
      
      
      logging.info("Ingestion of the data is completed")
      
      return (
        self.ingestion_config.train_data_path,
        self.ingestion_config.test_data_path,
      )
    except Exception as e:
      raise CustomException(e,sys)
    
    

if __name__ == "__main__":
  obj = DataIngestion()
  train_data_path,test_data_path = obj.initiate_data_ingestion()
  data_transformation = DataTransformation()
  data_transformation.initiate_data_transformation(train_data_path,test_data_path)
  



# ----------------os.path.dirname--------   
# os.path.dirname is used in Python to obtain the directory name of a specified path. This function is part of the os.path module, which provides utilities for manipulating filesystem paths in a way that is platform-independent.

# Here's a simple example:

# python
# import os

# path = "/home/user/documents/file.txt"
# directory = os.path.dirname(path)

# print(directory)  # Output: /home/user/documents


# In this example, os.path.dirname(path) returns the directory portion of the path /home/user/documents/file.txt, which is /home/user/documents. This can be useful when you need to work with the directory of a file path, such as when creating new files in the same directory or when navigating the filesystem.