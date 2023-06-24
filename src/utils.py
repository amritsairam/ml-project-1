#this will contain everything commonly required in code
import os
import sys
import pandas as pd
import numpy as np
from src.exception import CustomException
import dill #dill is a extension of pickle used to handle more complex python functions and objects, and it is used to make pickle files

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_path)

    except Exception as e:
        raise CustomException(e,sys)
