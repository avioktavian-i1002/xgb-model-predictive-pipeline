import requests

# Alamat endpoint API lokal kita
url = "http://127.0.0.1:8000/predict"

# Data contoh yang ingin diprediksi oleh model ML
payload = {
    "umur_bulan": 24.0,
    "berat_badan": 11.5,
    "tinggi_badan": 85.0,
    "lingkar_kepala": 47.0
}

# Kirim HTTP POST request ke server FastAPI
try:
    response = requests.post(url, json=payload)
    print("Status Code:", response.status_code)
    print("Output Respon dari API:")
    print(response.json())
except Exception as e:
    print("Gagal terhubung ke API. Pastikan server Uvicorn sudah menyala!", e)