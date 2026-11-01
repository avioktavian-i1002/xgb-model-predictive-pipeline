from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import os

# 1. Inisialisasi Aplikasi FastAPI
app = FastAPI(
    title="ML Predictive API Service",
    description="REST API untuk Layanan Prediksi Machine Learning (XGBoost)",
    version="1.0.0"
)

# 2. Skema Input Data menggunakan Pydantic (Validasi Tipe Data)
class PredictionInput(BaseModel):
    # Contoh atribut variabel fitur (sesuaikan dengan fitur dataset kamu)
    umur_bulan: float
    berat_badan: float
    tinggi_badan: float
    lingkar_kepala: float

    class Config:
        json_schema_extra = {
            "example": {
                "umur_bulan": 24.0,
                "berat_badan": 11.5,
                "tinggi_badan": 85.0,
                "lingkar_kepala": 47.0
            }
        }

# Global Variables untuk Model & Scaler
model = None
scaler = None

# Load Model saat Aplikasi Pertama Kali Menyala
@app.on_event("startup")
def load_artifacts():
    global model, scaler
    model_path = "best_xgboost_model.pkl"
    scaler_path = "scaler.pkl"
    
    if os.path.exists(model_path) and os.path.exists(scaler_path):
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        print("[API] Model dan Scaler berhasil dimuat.")
    else:
        print("[API Warning] File model '.pkl' belum ditemukan. Jalankan train.py terlebih dahulu.")

# 3. Endpoint Kesehatan API (Health Check)
@app.get("/")
def home():
    return {
        "status": "online",
        "message": "Welcome to ML Predictive REST API",
        "documentation": "/docs"
    }

# 4. Endpoint Prediksi
@app.post("/predict")
def predict(data: PredictionInput):
    if model is None or scaler is None:
        raise HTTPException(status_code=500, detail="Model ML belum dilatih/di-load.")
    
    try:
        # Konversi Input JSON ke Array 2D
        input_data = np.array([[
            data.umur_bulan,
            data.berat_badan,
            data.tinggi_badan,
            data.lingkar_kepala
        ]])
        
        # Scaling Input Data
        scaled_data = scaler.transform(input_data)
        
        # Prediksi Klasifikasi
        prediction = model.predict(scaled_data)[0]
        probabilities = model.predict_proba(scaled_data)[0].tolist()
        
        return {
            "prediction_class": int(prediction),
            "confidence_probabilities": probabilities,
            "status": "success"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Terjadi kesalahan prediksi: {str(e)}")