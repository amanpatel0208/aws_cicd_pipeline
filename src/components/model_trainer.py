# we will train all the models here

import os
import sys
from catboost import CatBoostRegressor
from dataclasses import dataclass
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
    )

from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from src.exceptions import CustomException
from src.logger import logging

from src.utils import save_object,evaluate_model

@dataclass
class ModelTrainerConfig:
    train_model_file_path=os.path.join('artifact','model.pkl')


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_trainer(self,train_array,test_array):
        try:
                logging.info('splitting training and test input data')
                X_train,y_train,X_test,y_test=(
                    train_array[:,:-1],
                    train_array[:,-1],
                    test_array[:,:-1],
                    test_array[:,-1]
                )

                models = {
                "Linear Regression": LinearRegression(),
                "Lasso": Lasso(),
                "Ridge": Ridge(),
                "K-Neighbors Regressor": KNeighborsRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Random Forest Regressor": RandomForestRegressor(),
                # "XGBRegressor": XGBRegressor(), 
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor()

                }

                # evaluate model is in utils

                model_report:dict=evaluate_model(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,models=models)

                best_model_score=max(sorted(model_report.values()))

                best_model_name=list(model_report.keys())[
                    list((model_report.values())).index(best_model_score)
                ]
                best_model=models[best_model_name]

                if best_model_score<0.6:
                    raise CustomException('no best model found')

                logging.info(f'best found model on both training and. test data is :{best_model_name}')

                save_object(
                    file_path=self.model_trainer_config.train_model_file_path ,
                    obj='best_model'
                )

                predicted=best_model.predict(X_test)
                score=r2_score(y_test,predicted)

                return score

        except Exception as e:
                raise CustomException(e,sys)


