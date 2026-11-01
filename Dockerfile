# 1. Gunakan base image Python resmi
FROM python:3.10-slim

# 2. Set direktori kerja di dalam kontainer
WORKDIR /app

# 3. Salin file requirements & install dependensi
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Salin semua file proyek ke dalam kontainer
COPY . .

# 5. Expose port FastAPI
EXPOSE 8000

# 6. Perintah untuk menjalankan aplikasi
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
