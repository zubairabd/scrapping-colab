 🌧️ Scraping Data Curah Hujan Bulanan

## 📌 Deskripsi
Repository ini berisi kode untuk melakukan **web scraping data curah hujan bulanan** dari website [hidrologi.net](https://hidrologi.net/).  
Terdapat beberapa jenis file:
- **`.py`** → script Python utama untuk scraping.
- **`.ipynb`** → notebook Google Colab untuk eksplorasi & dokumentasi proses.
- **`.txt`** → file data hasil scraping atau pendukung lainnya.

## 📂 Struktur Repo
├── SCRAPPING_DATA_BULANAN.ipynb # Notebook Colab untuk scraping
├── scraper.py # Script scraping versi Python
├── hasil_scraping.txt # Data hasil scraping (opsional)
├── requirements.txt # Library yang diperlukan
└── README.md # Dokumentasi project

## ⚙️ Instalasi

Clone repository ini ke komputer lokal:

```bash
git clone https://github.com/zubairabd/scrapping-colab.git
cd scrapping-colab
```
install dependency
```
pip install -r requirements.txt
```
---
## Cara Menjalankan
- Di Google Colab
Upload file scraping.ipynb ke Google Colab
Jalankan semua cell, hasil akan otomatis disimpan ke file curah_hujan_rata2.csv dan bisa diunduh
- Di Python Lokal

Jalankan script **`.py`** langsung dengan:

```python scraping.py```

setelah clone repo dan instal dependency
