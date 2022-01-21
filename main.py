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
    final_prediction = model.predict(np.array([2,2,2,4,4,4,1,4]).reshape(1,-1))[0]
    explanations = str()
    if final_prediction == 0:
        explanations = "You're not Financially Resilient"
    explanations = "financially resilient"
    return {"final_prediction" : int(final_prediction), "Interpretation":explanations}
    

        