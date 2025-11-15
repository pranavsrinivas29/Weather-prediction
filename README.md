# 🌤️ Weather Prediction System  
**Streamlit UI + FastAPI Backend + Deep Learning Models (LSTM, GRU, GRU Encoder–Decoder)**

This project implements an end-to-end **Weather Prediction System** using a modular architecture.  
It combines:

- 🖥️ **Streamlit** — Interactive frontend for user input & visualization  
- ⚙️ **FastAPI** — Backend API for model inference  
- 🤖 **Deep Learning Models** — LSTM, GRU, and GRU Encoder–Decoder  
- 🔧 **Data Processing Pipeline** — Calendar-based features, MinMax scaling, Label Encoding  
- 📦 **Modular Code** — Clean separation of UI, API, and model logic  

---

## 🚀 Project Features

### 🌐 **1. Streamlit Frontend**
- User-friendly UI for predicting weather conditions  
- Validations for all inputs  
- Custom logo and theming  
- Sends user inputs to FastAPI via POST request  
- Displays prediction result in real-time  

### ⚡ **2. FastAPI Backend**
- Receives JSON input from Streamlit  
- Preprocesses input features  
- Loads scaler, label encoder, and trained DL model  
- Runs prediction and returns the decoded label  
- Fully modular and production-ready design  

### 🧠 **3. Deep Learning Models**
You can switch between three neural network architectures:
- ✔️ **LSTM** model  
- ✔️ **GRU** model  
- ✔️ **GRU Encoder–Decoder model** for sequence modeling  

All models:
- Output 5 weather classes  
- Use softmax classification  
- Are saved in `.h5` format  

### 📊 **4. Data Preprocessing**
Includes:

- **Calendar features**
  - `year`
  - `month`
  - `day`
  - `day of week`
  - `is_weekend`
- **MinMaxScaler**
  - Fitted on training data  
  - Saved as `minmax_scaler.pkl`  
  - Reused during prediction  
- **LabelEncoder**
  - Maps weather classes ↔ integers  
  - Saved as `label_encoder.pkl`  
- **Feature Order Standardization**
  - Ensures input shape matches model training shape  

---

## 🔄 End-to-End Flow

### 1️⃣ User enters inputs in Streamlit  
- Max Temp  
- Min Temp  
- Precipitation  
- Wind Speed  
- Date (YYYY-MM-DD)

### 2️⃣ Streamlit → FastAPI (JSON POST)
Example payload:

```json
{
  "prediction_date": "2025-11-14",
  "max_temp": 10,
  "min_temp": 2.8,
  "precipitation": 0,
  "wind": 2
}
```

### FastAPI returns JSON response
```json
{
  "prediction": "Rainy"
}
```

### Streamlit displays the result to the user

### Run the Application
```bash
uvicorn main:app --reload #FastAPI server

streamlit run app.py #Streamlit app
```

### Model Training (Short Summary)

#### The model training pipeline includes:
- Train-test split
- Calendar-based feature extraction
- MinMax normalization
- Label encoding
- Model building (LSTM/GRU/GRU Encoder-Decoder)
- Softmax output layer
- Saving artifacts:
- Model → .h5
- Scaler → .pkl
- Encoder → .pkl

### Technologies used
```text
| Component        | Tool             |
| ---------------- | ---------------- |
| Frontend         | Streamlit        |
| Backend          | FastAPI          |
| Deep Learning    | TensorFlow/Keras |
| Scaling          | MinMaxScaler     |
| Encoding         | LabelEncoder     |
| HTTP Client      | requests         |
| Deployment Ready | Modular Codebase |
```
