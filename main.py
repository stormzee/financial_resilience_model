from typing import Optional
from fastapi import FastAPI
import joblib
import numpy as np
import warnings
warnings.filterwarnings("ignore")

app = FastAPI()

def load_utils():
    load_model = joblib
    model = load_model.load('financial_resilience_predictor.joblib')
    return model


@app.get("/")
def index():
    model =  load_utils()
    final_prediction = model.predict(np.array([1,2,1,4,1,4,1,1]).reshape(1,-1))[0]
    explanations = "financially resilient"
    
    
    if not final_prediction :
        explanations = "You're not Financially Resilient"
        
    return {"final_prediction" : int(final_prediction), "Interpretation":explanations}
    

        