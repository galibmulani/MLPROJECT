import pickle
import os
import sys 

from src.exception import CustomException

def save_object(filepath,obj):
    try:
        dir_path=os.path.dirname(filepath)

        os.makedirs(dir_path,exist_ok=True)

        with open(filepath,"wb") as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)