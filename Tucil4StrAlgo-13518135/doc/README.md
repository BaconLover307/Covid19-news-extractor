# Tucil4-StrAlgo -- Ekstraksi Informasi dari Artikel Berita dengan Algoritma Pencocokan String
Program ini adalah contoh pengaplikasian strategi algoritma Knuth-Morris-Pratt (KMP), Boyer-Moore (BM) dan Regular Expression untuk mengektraksi informasi dari sebuah artikel berita berdasarkan keyword yang dimasukkan

## Instalasi Program
Program ini dibuat menggunakan bahasa pemrograman Python oleh karena itu dibutuhkan Python interpreter versi 3.7.4 atau lebih tinggi. Interpreter dapat diunduh melalui https://www.python.org/downloads/release/python-374/ Setelah Python diinstall, lakukan clone pada repository ini, atau download dalam file .zip dan extract ke folder yang diinginkan.

### Prerequisites

Sebelum menjalankan program, terdapat library yang harus diunduh dan diinstall melalui Command Prompt agar program bisa berjalan dengan benar. Berikut adalah daftar command untuk menginstall library-library ini dapat menggunakan pip.

```
pip install --upgrade pip
pip install virtualenv
```

### Cara Menjalankan Kode Program
Untuk mengompilasi program, buka terminal komputer Anda dan pergi ke directory di mana program disimpan. Kemudian silakan ketikkan perintah seperti di bawah ini:

#### Untuk sistem operasi Windows
```
C:\Users\<user>\Documents\Tucil4StrAlgo-13518135>
# cd src
C:\Users\<user>\Documents\Tucil4StrAlgo-13518135\src>
# venv\Scripts\activate
(venv) C:\Users\<user>\Documents\Tucil4StrAlgo-13518135\src>
# py app.py
atau
#python3 
```

#### Untuk sistem operasi Linux
```bash
home/Tucil4StrAlgo-13518135
$ cd src
home/Tucil4StrAlgo-13518135/src
$ source env/bin/activate
(venv) home/Tucil4StrAlgo-13518135/src
$ py app.py
atau
$ python3 app.py
```

Perintah di atas akan menjalankan sebuah virtual environment yang sudah memuat prerequisite untuk menjalankan program.

## Cara Menggunakan Program
Setelah program dijalankan dengan benar, akan muncul beberapa tulisan pada command prompt, contohnya sebagai berikut:
```
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 820-239-708
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Untuk menjalankan program, diperlukan juga web browser. Silakan mengcopy address localhost yang muncul pada command prompt ke address bar web browser. Kemudian program akan berjalan dan memunculkan tampilan sebagai berikut:

![Tampilan Utama]('tampilanutama.png' "Tampilan Utama")

Perlu diingat bahwa program hanya dapat membaca berita paling banyak 4 buah sekaligus karena limitasi program 

## Kontributor
Program ini dibuat untuk memenuhi salah satu Tugas Kecil IF2211 Strategi Algoritma Teknik Informatika ITB. Adapun pembuat dari program ini adalah:
- Gregorius Jovan Kresnadi - 13518135

