# Kelompok AI-TE1303: Sistem Navigasi & Sistem Pakar

Proyek kolaboratif mata kuliah Kecerdasan Buatan yang berfokus pada implementasi Sistem Pakar berbasis aturan (*rule-based*) serta algoritma pencarian jalur (*pathfinding*) berbasis teks/konsol.

## 👥 Tim Pengembang
* **Royal Ramli Wisjtra** (Manager / `main`)
* **Dwi Zarfa K** (Dev 1 / `dev1`)
* **Abimanyu Aziz** (Dev 2 / `dev2`)

---

## 1. Latar Belakang & Deskripsi
Sistem Navigasi Rute Pengiriman Barang ini adalah program berbasis konsol yang membantu menghitung dan menentukan jalur pengiriman optimal dari titik awal menuju lokasi tujuan. Pengguna dapat memasukkan parameter hambatan atau blokade rute, dan sistem akan memproses jalur alternatif serta memberikan diagnosis status keselamatan pengiriman secara tekstual di terminal.

## 2. Tujuan Pengerjaan
* Mengimplementasikan algoritma pencarian (*search*) pada studi kasus nyata.
* Membandingkan performa antara metode *uninformed* (BFS, Dijkstra) dan *informed* (A*).
* Menerapkan sistem pakar berbasis aturan (*rule-based*) untuk menafsirkan hasil keluaran pencarian rute.

## 3. Spesifikasi Teknologi
* **Bahasa Pemrograman:** Python 3.x
* **Pustaka Standar:** Menggunakan pustaka bawaan Python (seperti `heapq`, `collections`, dll.) tanpa memerlukan instalasi pustaka grafis tambahan.
* **Core Algoritma:** BFS, Dijkstra, A*.
* **Sistem Pakar:** Logika inferensi berbasis aturan kondisional (IF-THEN rules).


## 4. Alur Kerja Sistem
Berdasarkan implementasi kode program, alur kerja sistem pakar ini berjalan melalui tahapan berikut:
1. **Inisialisasi Basis Aturan (*Rule Base*):** Sistem memuat daftar aturan (`R1` hingga `R8`) yang masing-masing berisi kondisi spesifik dan kesimpulan rekomendasi.
2. **Pengumpulan Fakta (*Fact Gathering*):** Program meminta pengguna untuk memasukkan data awal melalui terminal, yang mencakup berat barang (`berat`), jarak pengiriman (`jarak`), serta tiga kondisi boolean (perlu suhu dingin, barang mudah pecah, dan pengiriman mendesak).
3. **Proses Mesin Inferensi (*Forward Chaining*):** 
   * Sistem mengevaluasi fakta-fakta yang dimasukkan pengguna terhadap kondisi pada setiap aturan secara berurutan.
   * Jika kondisi suatu aturan bernilai benar (`True`), maka aturan tersebut aktif dan kesimpulannya dicatat.
4. **Menampilkan Hasil Diagnosis:** Program mencetak daftar rekomendasi akhir ke layar terminal berdasarkan aturan-aturan yang aktif (mencakup jenis kendaraan, penanganan tambahan, dan jenis layanan).

### Perbandingan Karakteristik Algoritma
| Algoritma | Kategori | Karakteristik Output | Tingkat Keoptimalan |
| :--- | :--- | :--- | :--- |
| **BFS** | Uninformed | Meminimalkan jumlah langkah lompatan | Optimal untuk jumlah langkah |
| **Dijkstra** | Uninformed | Menemukan jarak metrik terpendek | Optimal |
| **A\*** | Informed | Jarak terpendek berpandu fungsi heuristik | Optimal |

## 5. Sudut Pandang Kecerdasan Buatan (AI Perspective)
* **Search Module:** Berfungsi sebagai motor utama perhitungan jalur navigasi.
* **Expert System Module:** Berfungsi mengevaluasi fakta hasil pencarian untuk menghasilkan rekomendasi keputusan.
* Proyek ini murni dibangun menggunakan pendekatan algoritmik dan aturan logika, tanpa melibatkan *Machine Learning*.

## 6. Keterbatasan Sistem
* Pemetaan jaringan menggunakan model simulasi statis di dalam sistem.
* Seluruh input hambatan bersifat manual dari pengguna (*user input*).
* Faktor eksternal seperti cuaca riil atau dinamika lalu lintas nyata tidak diperhitungkan.

## 7. Panduan Penggunaan
1. Buka terminal atau Command Prompt pada direktori proyek.
2. Jalankan skrip program yang diinginkan.
3. Ikuti instruksi interaktif yang muncul di layar terminal untuk memasukkan data atau pilihan parameter.


## 8. Instruksi Eksekusi Program

- git clone [https://github.com/RoyalRamliwisjtra/AI-TE-1303.git](https://github.com/RoyalRamliwisjtra/AI-TE-1303.git)
- cd AI-TE-1303

- python search_algorithm/astar.py
- python search_algorithm/greedy_best_first.py
- python expert_system/expert_system.py

## 9.Arsitektur direktori
```bash
AI-TE-1303/
├── expert_system/        # Modul aturan sistem pakar
│   └── expert_system.py
├── search_algorithm/     # Modul algoritma pencarian jalur
│   ├── astar.py
│   └── greedy_best_first.py
├── main.py               # Berkas utama aplikasi
└── README.md             # Dokumentasi proyek




