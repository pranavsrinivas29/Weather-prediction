import pandas as pd
import joblib
import numpy as np
from tensorflow.keras.models import load_model

def preprocess(date, X_list):
    date = pd.to_datetime(date)
    day = date.day
    month = date.month
    year = date.year
    X_list.append(year)
    X_list.append(month)
    X_list.append(day)
    
    scaler = joblib.load("minmax_scaler.pkl")
    

    X_list = np.array(X_list).reshape(1, -1)
    X_list = scaler.transform(X_list)
    
    model = load_model("weather_gru_model.h5")
    X_list = np.array(X_list).reshape(1, 1, -1)
    ypred = model.predict(X_list)
    
    le = joblib.load("label_encoder.pkl")
    pred_index = np.argmax(ypred)
    pred_label = le.inverse_transform([pred_index])[0]
    return pred_label

if __name__ == '__main__':
    Xlist = [0.0, 10, 2.8, 2]
    date = '2025-11-04'
    ypred = preprocess(date, Xlist)
    print(ypred)