# Prediksi Harga Mobil dengan Regresi Linier Sederhana

Tugas Praktikum Aplikasi Web – Modul 4 (Simple Linear Regression)

Proyek ini memprediksi **harga mobil (`price`)** berdasarkan **ukuran mesin (`enginesize`)** menggunakan regresi linier sederhana, lalu menerapkannya dalam aplikasi web **Streamlit**.

## Dataset
- Sumber: [Car Price Prediction – Kaggle](https://www.kaggle.com/datasets/hellbuoy/car-price-prediction) (`CarPrice_Assignment.csv`)
- Dari 26 kolom, hanya 2 kolom yang digunakan dan disimpan sebagai `car_price.csv`:
  - `enginesize` → variabel bebas (X), ukuran mesin (cubic inch)
  - `price` → variabel terikat (y), harga mobil (USD)
- Jumlah data: 205 baris

## Hasil Model
| Metrik | Nilai |
|---|---|
| Korelasi (r) | 0,874 (kuat) |
| Persamaan | price = −9116,72 + 178,33 × enginesize |
| R² (data uji) | 0,77 |
| RMSE | ≈ $3.515 |

Contoh: ukuran mesin 130 → perkiraan harga ≈ $14.066,60

