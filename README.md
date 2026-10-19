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
1. Pengguna menjalankan program melalui terminal dan memberikan input parameter awal.
2. Sistem merepresentasikan jaringan peta dalam bentuk struktur data *graph* (node dan bobot edge).
3. Algoritma penelusuran memproses jalur terbaik menuju target dengan menghindari titik hambatan.
4. Hasil keluaran pencarian diteruskan ke mesin sistem pakar.
5. Sistem menerbitkan status operasional (AMAN / WASPADA / BAHAYA) beserta saran tindakan di layar konsol.

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

git clone [https://github.com/RoyalRamliwisjtra/AI-TE-1303.git](https://github.com/RoyalRamliwisjtra/AI-TE-1303.git)
cd AI-TE-1303

python search_algorithm/astar.py
python search_algorithm/greedy_best_first.py
python expert_system/expert_system.py

## 9.AI-TE-1303
```bash
├── expert_system/        # Modul aturan sistem pakar
│   └── expert_system.py
├── search_algorithm/     # Modul algoritma pencarian jalur
│   ├── astar.py
│   └── greedy_best_first.py
├── main.py               # Berkas utama aplikasi
└── README.md             # Dokumentasi proyek




