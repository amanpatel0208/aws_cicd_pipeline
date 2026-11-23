# here we will make an web application which will work with the input data and give us predictions
# here we will load our pkl files and we will get the best prediction possible to any data

# the customdata will be created here

import sys
import pandas as pd
from src.exceptions import CustomException
from src.utils import Load_object

class PredictPipeline:
    def __init__(self):
        pass
    def predict(self,features):
        try:
            model_path='/Users/amanarifpatel/Documents/ml_project/artifact/model.pkl'
            preprocessor_path='/Users/amanarifpatel/Documents/ml_project/artifact/preprocessor.pkl'
            model=Load_object(file_path=model_path)
            preprocessor=Load_object(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        except Exception as e:
            CustomException(e,sys)


class CustomData:
    def __init__(self,gender:str,race_ethnicity:str,parental_level_of_education:str,lunch:str,
                 test_preparation_course: str, reading_score:int, writing_score:int):
        self.gender=gender
        self.race_ethnicity=race_ethnicity
        self.parental_level_of_eductaion=parental_level_of_education
        self.lunch=lunch
        self.test_preparation_course=test_preparation_course
        self.reading_score=reading_score
        self.writing_score=writing_score

    def get_data_as_frame(self):
        try:
            custom_data_input_dict={

                'gender':[self.gender],
                'race_ethnicity':[self.race_ethnicity],
                'parental_level_of_education':[self.parental_level_of_eductaion],
                'test_preparation_course':[self.test_preparation_course],
                'lunch':[self.lunch],
                'reading_score':[self.reading_score],
                'writing_score':[self.writing_score]

            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e,sys)
        