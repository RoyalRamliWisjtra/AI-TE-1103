# Kelompok AI-TE1303: Sistem Navigasi & Sistem Pakar

Proyek kolaboratif mata kuliah Kecerdasan Buatan yang berfokus pada implementasi Sistem Pakar berbasis aturan (*rule-based*) serta algoritma pencarian jalur (*pathfinding*) berbasis teks/konsol.

## 👥 Tim Pengembang
* **Royal Ramli Wisjtra** (Manager / `main`)
* **Dwi Zarfa K** (Dev 1 / `dev1`)
* **Abimanyu Aziz** (Dev 2 / `dev2`)

---

## 1. Deskripsi Proyek
Aplikasi berbasis konsol (*terminal*) ini dirancang untuk menyelesaikan dua permasalahan utama dalam sistem logistik pengiriman barang:
1. **Sistem Pakar:** Merekomendasikan jenis kendaraan (motor, mobil kecil, mobil boks, truk, atau mobil berpendingin), bahan kemasan tambahan (seperti *bubble wrap*), serta jenis layanan (ekspres atau reguler) berdasarkan fakta spesifikasi barang.
2. **Search Algorithm:** Menentukan rute pencarian terpendek/teroptimal dari lokasi asal menuju lokasi tujuan pengiriman.

---

## 2. Tujuan
* Mengimplementasikan sistem pakar berbasis aturan (*rule-based*) menggunakan teknik *Forward Chaining*.
* Menerapkan algoritma *Informed Search* (A* dan Greedy Best-First Search) pada model pencarian rute.
* Menyediakan program yang interaktif, efisien, dan ringan dijalankan langsung melalui terminal/Command Prompt tanpa kebergantungan pada library grafis (*GUI*).

---

## 3. Spesifikasi Teknologi & Library
* **Bahasa Pemrograman:** Python 3.x
* **Library / Pustaka:** Menggunakan pustaka standar bawaan Python (seperti `heapq` dan `collections`) tanpa membutuhkan instalasi library grafis external (`pygame` / `tkinter`).

---

## 4. Cara Kerja Sistem

### A. Sistem Pakar (`expert_system/expert_system.py`)
Sistem berjalan menggunakan metode **Forward Chaining** mengevaluasi himpunan aturan `R1` hingga `R8`:
1. **Input Fakta (`fakta`):** Pengguna menginputkan data kuantitatif dan kualitatif:
   * `berat`: Berat barang dalam kg (float).
   * `jarak`: Jarak pengiriman dalam km (float).
   * `dingin`: Perlu suhu dingin? (y/n).
   * `mudah_pecah`: Barang mudah pecah? (y/n).
   * `mendesak`: Pengiriman mendesak? (y/n).
2. **Evaluasi Aturan (*Rule Evaluation*):**
   * **R1:** Jika `dingin` = True $\rightarrow$ Kendaraan: mobil berpendingin.
   * **R2:** Jika `not dingin` dan `berat` > 50 kg $\rightarrow$ Kendaraan: truk.
   * **R3:** Jika `not dingin` dan 10 kg < `berat` $\le$ 50 kg $\rightarrow$ Kendaraan: mobil boks.
   * **R4:** Jika `not dingin`, `berat` $\le$ 10 kg, dan `jarak` $\le$ 15 km $\rightarrow$ Kendaraan: motor.
   * **R5:** Jika `not dingin`, `berat` $\le$ 10 kg, dan `jarak` > 15 km $\rightarrow$ Kendaraan: mobil kecil.
   * **R6:** Jika `mudah_pecah` = True $\rightarrow$ Tambahan: gunakan bubble wrap dan kardus berlapis.
   * **R7:** Jika `mendesak` = True $\rightarrow$ Layanan: ekspres (sampai hari yang sama).
   * **R8:** Jika `not mendesak` = True $\rightarrow$ Layanan: reguler (1-3 hari).
3. **Inferensi & Output:** Mesin inferensi menelusuri aturan secara berurutan dan menampilkan seluruh kesimpulan yang kondisi (*lambda*)-nya bernilai `True`.

### B. Algoritma Pencarian Jalur (`search_algorithm/`)
* **A\* Search (`astar.py`):** Menggabungkan jarak riil ($g(n)$) dan fungsi heuristik ($h(n)$) jarak garis lurus menuju target untuk menemukan rute paling optimal.
* **Greedy Best-First Search (`greedy_best_first.py`):** Fokus mengevaluasi node berdasarkan nilai heuristik terdekat $h(n)$ ke titik tujuan.

---

## 5. Peran Kecerdasan Buatan (AI Perspective)
* **Rule-Based Expert System:** Menerapkan rantai inferensi *forward chaining* untuk mengevaluasi parameter barang menjadi keputusan operasional.
* **Search Algorithm:** Menerapkan fungsi heuristik pada pencarian rute terarah (*informed search*).
* Proyek ini berbasis logika terprogram dan algoritma klasik, tidak mengimplementasikan *Machine Learning*.

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




