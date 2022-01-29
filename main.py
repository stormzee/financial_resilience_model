from typing import Optional
from fastapi import FastAPI, status
from pydantic import BaseModel
import joblib
import numpy as np
import warnings
warnings.filterwarnings("ignore")

app = FastAPI()


class UserInput(BaseModel):
    deposits : int
    withdrawals : int 
    savings : int 
    Delinqencies : int 
    received_salary : int 
    employed : int 
    available_pension_funds : int 
    business_profit : int 
    
   
def load_utils():
    load_model = joblib
    model = load_model.load('financial_resilience_predictor.joblib')
    return model



@app.post("/predict/", status_code = status.HTTP_200_OK)
def model_prediction(input_data:UserInput):
    model =  load_utils()
    try:
        final_prediction = model.predict(np.array(
            [input_data.deposits,
            input_data.withdrawals,
            input_data.savings,
            input_data.Delinqencies,
            input_data.received_salary,
            input_data.employed,
            input_data.available_pension_funds,
            input_data.business_profit]).reshape(1,-1))[0]
        explanations = "financially resilient"
        
        if not final_prediction :
            explanations = "You're not Financially Resilient"
            
        response = {"final_prediction" : int(final_prediction), "Interpretation":explanations}
   
    except ValueError:
        response = {"message":"No results for your input","status":status.HTTP_406_NOT_ACCEPTABLE, "Error":type(error)}
    return response


 