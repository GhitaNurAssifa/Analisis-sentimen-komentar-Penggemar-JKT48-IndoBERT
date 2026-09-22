**Analisis Sentimen Komentar YouTube JKT48 Era JKT48 FIGHT! Menggunakan IndoBERT**

Proyek ini adalah implementasi _Deep Learning dan Natural Language Processing_ (NLP) untuk menganalisis sentimen opini penggemar terhadap konten era baru **JKT48 FIGHT!** pada kanal YouTube resmi JKT48. 

Aplikasi ini dibangun menggunakan arsitektur modern yang memisahkan antara proses komputasi data (Python lokal), pelatihan model AI (Google Colab), dan antarmuka pengguna berbasis web (Laravel Dashboard).

## 🏗️ Alur Kerja & Arsitektur Sistem

Proyek ini diselesaikan melalui 4 tahapan utama yang terintegrasi:

1. **Data Scraping (Lokal - VS Code & CMD):**
   Membangun skrip Python di Visual Studio Code menggunakan **YouTube Data API v3**. Skrip dijalankan melalui Command Prompt (CMD) untuk menarik **39.000+ komentar mentah** secara massal dari 13 video JKT48, yang kemudian disimpan dalam format file **CSV**.

2. **Text Preprocessing (Lokal - VS Code & Python):**
   Melakukan pembersihan data mentah di VS Code menggunakan Python. Tahapan ini berhasil menyaring dan menormalisasi data menjadi **34.000+ baris data bersih**, termasuk menangani singkatan, bahasa gaul/slang internet wota, serta kata tidak baku lainnya.

3. **Model Training & Fine-Tuning (Cloud - Google Colab):**
   Proses pelatihan arsitektur *Deep Learning* **IndoBERT** dilakukan di Google Colab untuk memanfaatkan akselerasi hardware GPU. Proses ini menghasilkan performa klasifikasi sentimen (Positif, Netral, Negatif) yang sangat andal.

4. **Web Dashboard & User Interface (Lokal - Laravel & PHP):**
   Hasil akhir analisis data dan prediksi sentimen diintegrasikan ke dalam *framework* Laravel (PHP). Menyediakan dasbor interaktif bagi pengguna untuk melihat grafik visualisasi sentimen, halaman simulasi *preprocessing*, serta menu pengujian prediksi teks secara langsung.

## 📊 Performa Model IndoBERT
Proses *fine-tuning* pada model Transformer IndoBERT menghasilkan nilai metrik evaluasi sebagai berikut:
- **Accuracy:** 88,14%
- **Precision:** 83,42%
- **Recall:** 88,14%
- **F1-Score:** 85,23%

## 🛠️ Teknologi & Tools yang Digunakan
- **Code Editor & CLI:** Visual Studio Code, Command Prompt (CMD)
- **AI & Data Science:** Python, Hugging Face Transformers (IndoBERT Base), PyTorch, Pandas, Scikit-Learn
- **Web Development:** PHP, Laravel Framework, MySQL / PostgreSQL
- **Sumber Data:** YouTube Data API v3 (Format Output: CSV)
