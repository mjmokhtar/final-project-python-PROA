# final-project-python-PROA
project final project pyhton 
Nama: Muhammad Jumi'at Mokhtar
Nomor Peserta: 1987301840-578

# Analisis Data dari Database MySQL menggunakan Python

Kode ini merupakan contoh implementasi untuk melakukan analisis data dari database MySQL menggunakan Python. Dalam contoh ini, kita akan menghubungkan ke database MySQL, membaca data dari tabel tertentu, dan melakukan plot grafik menggunakan data yang telah diambil.

### Teknologi yang Digunakan
- Python
- MySQL
- Pandas
- Matplotlib

### Langkah-langkah

1. **Menghubungkan ke Database MySQL:**
    - Menggunakan `mysql.connector` untuk menghubungkan ke server MySQL dengan mengisi host, username, password, dan nama database.

2. **Membaca Data dari Tabel MySQL ke DataFrame Pandas:**
    - Menggunakan Pandas untuk membaca data dari tabel yang diinginkan dan menyimpannya ke dalam DataFrame.

3. **Plot Grafik Data Menggunakan Matplotlib:**
    - Menggunakan Matplotlib untuk membuat plot dari data yang telah diambil dari database. Plot terdiri dari tiga sumbu y dengan skala yang berbeda untuk masing-masing data suhu, kelembaban, dan data silang.

### Cara Menggunakan
1. Pastikan Anda memiliki Python dan MySQL terinstal di komputer Anda.
2. Instal library yang diperlukan dengan menjalankan `pip install mysql-connector-python pandas matplotlib`.
3. Ubah konfigurasi koneksi database pada bagian kode yang relevan dengan host, username, password, dan nama database Anda.
4. Jalankan kode Python, dan hasil plot grafik akan ditampilkan.

### Kontribusi
- Jika Anda menemukan masalah atau ingin meningkatkan kode ini, silakan buka pull request atau issue di repository ini.

### Lisensi
Proyek ini dilisensikan di bawah Lisensi MIT. Lihat `LICENSE` untuk detail lebih lanjut.

