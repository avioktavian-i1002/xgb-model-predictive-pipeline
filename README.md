# 🚀 End-to-End ML Predictive Pipeline & REST API Services

Proyek portofolio *Machine Learning* dan *MLOps* end-to-end yang mengintegrasikan pemodelan prediktif berbasis **XGBoost**, REST API berperforma tinggi dengan **FastAPI**, serta *containerization* menggunakan **Docker**.

## 🛠️ Tech Stack
* **Language:** Python 3.10
* **ML Library:** Scikit-Learn, XGBoost, Imbalanced-Learn (SMOTE)
* **Backend / MLOps:** FastAPI, Uvicorn, Pydantic, Docker
* **Deployment Ready:** REST API Endpoint & Swagger UI Documentation

## 📂 Project Architecture
1. **Data Pipeline (`pipeline.py`):** Pembersihan data otomatis, *feature scaling*, dan penanganan *imbalanced data* menggunakan SMOTE.
2. **Model Training (`train.py`):** Pelatihan model klasifikasi XGBoost dengan *Hyperparameter Tuning* (GridSearchCV).
3. **API Service (`main.py`):** Pembungkusan model (.pkl) ke dalam REST API dengan validasi skema input Pydantic.
4. **Containerization (`Dockerfile`):** Konfigurasi *container* Docker siap *deploy* ke cloud.

## 🚀 Cara Menjalankan Secara Lokal
1. Clone repositori ini:
   ```bash
   git clone [https://github.com/USERNAME_KAMU/nama-repo.git](https://github.com/USERNAME_KAMU/nama-repo.git)
   cd nama-repo