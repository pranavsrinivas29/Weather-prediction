from fastapi import FastAPI
from pydantic import BaseModel
from data_preprocessing import preprocess
app = FastAPI()

class WeatherRequest(BaseModel):
    prediction_date : str
    min_temp: float
    max_temp: float
    precipitation: float
    wind: float
    
@app.get('/')
def root():
    return {'message': 'Weather Prediction App'}

@app.post('/predict')
def predict(request: WeatherRequest):
    
    X_list = [request.precipitation, request.max_temp, request.min_temp, request.wind]
    pred_label = preprocess(request.prediction_date, X_list)
    
    return {'Prediction':pred_label}
    # return{"max temp": request.max_temp,
    #        "min temp": request.min_temp,
    #        "precipitation": request.precipitation,
    #        "wind": request.wind}