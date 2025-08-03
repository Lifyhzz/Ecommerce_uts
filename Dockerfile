FROM python:3.10-slim

# Buat direktori kerja di dalam container
WORKDIR /app

# Salin file dependensi
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua file ke container
COPY . .

# Tentukan environment variable
ENV FLASK_APP=app.py

# Jalankan Flask server
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
