from typing import Optional
from fastapi import FastAPI, status, HTTPException, Request
from fastapi.exception_handlers import http_exception_handler, request_validation_exception_handler
from starlette.exceptions import HTTPException as starletteHTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import joblib
import numpy as np
import warnings
warnings.filterwarnings("ignore")

app = FastAPI()

# for you to perform custom exception handling, 
# use the starlette or fastapi exception_handler and plaintextresponses
# to override the built-in fastapi exception handler

@app.exception_handler(starletteHTTPException)
async def custom_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=422)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request:Request, exc: RequestValidationError):
    return JSONResponse(
        status_code= status.HTTP_422_UNPROCESSABLE_ENTITY,
        content = jsonable_encoder({
            "detail":str(exc.errors),
            "body": exc.body
            
        }),
    )
    
    
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
    
    
    if not input_data:
        raise HTTPException(status_code=500, detail="Input not acceptable, please provide the correct input")


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
   # response = {"message":"No results for your input","status":status.HTTP_406_NOT_ACCEPTABLE, "Error":type(error)}
    
    
    return response


 