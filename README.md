# Repository Tugas Besar AI-TE1303: Kombinasi Pathfinding & Sistem Pakar

Proyek kolaboratif mata kuliah Kecerdasan Buatan ini berfokus pada pengembangan sistem cerdas berbasis aturan (*rule-based*) serta visualisasi algoritma pencarian jalur (*pathfinding*) untuk optimasi jaringan logistik dan pengiriman.

## 👥 Tim Pengembang
* **Royal Ramli Wisjtra** (Manager / `main`)
* **Dwi Zarfa K** (Dev 1 / `dev1`)
* **Abimanyu Aziz** (Dev 2 / `dev2`)

---

## 1. Latar Belakang & Gambaran Umum
Sistem ini dirancang untuk mensimulasikan proses penentuan rute pengiriman logistik secara cerdas pada model peta jaringan. Pengguna dapat memberikan input berupa titik awal, opsi algoritma, hingga hambatan rute (seperti jalur yang diblokir atau macet), kemudian sistem secara otomatis akan mencari jalur alternatif terbaik sekaligus memberikan rekomendasi operasional keselamatan.

## 2. Target & Tujuan Pengerjaan
* Mengimplementasikan konsep dasar pencarian terarah maupun tidak terarah dalam studi kasus nyata.
* Melakukan komparasi performa antara algoritma *uninformed* (BFS, Dijkstra) dan *informed* (A*).
* Membangun modul sistem pakar sederhana yang mampu menerjemahkan keluaran algoritma pencarian menjadi keputusan tindakan.

## 3. Spesifikasi Teknis
* **Bahasa Pemrograman:** Python 3.x
* **Pustaka Antarmuka (GUI):** Pygame (untuk visualisasi grid peta interaktif).
* **Core Algoritma:** BFS, Dijkstra, A*.
* **Sistem Pakar:** Menggunakan pendekatan *rule-based* (logika kondisional IF-THEN) untuk menghasilkan saran penanganan.

## 4. Alur Kerja Aplikasi
1. Pengguna menentukan titik awal perjalanan beserta hambatan di peta.
2. Program merepresentasikan area tersebut dalam bentuk struktur data *graph* (node dan edge berbobot jarak).
3. Algoritma terpilih memproses pencarian rute menuju target tanpa menabrak area terhalang.
4. Data hasil pencarian rute dialirkan ke mesin sistem pakar untuk dievaluasi kondisinya.
5. Sistem menerbitkan status keselamatan (AMAN / WASPADA / BAHAYA) beserta saran tindakan.
6. Visualisasi rute digambarkan langsung pada antarmuka layar.

### Perbandingan Karakteristik Algoritma
| Algoritma | Kategori | Karakteristik Output | Tingkat Keoptimalan |
| :--- | :--- | :--- | :--- |
| **BFS** | Uninformed | Meminimalkan jumlah lompatan langkah | Hanya optimal untuk jumlah langkah |
| **Dijkstra** | Uninformed | Menemukan jarak metrik terpendek | Optimal |
| **A\*** | Informed | Jarak terpendek berbasis fungsi heuristik | Optimal |

*Catatan:* Berbeda dengan BFS dan Dijkstra yang melakukan eksplorasi secara meluas, A* memanfaatkan informasi heuristik (perhitungan garis lurus ke titik akhir) sehingga proses pencarian node menjadi jauh lebih efektif.

## 5. Sudut Pandang Kecerdasan Buatan (AI Perspective)
* **Search Module:** Berperan sebagai motor penggerak utama untuk memetakan rute navigasi terbaik.
* **Expert System Module:** Berperan sebagai penasihat keputusan (*decision support*) berdasarkan kumpulan aturan spesifik.
* *Catatan:* Proyek ini murni dibangun menggunakan pendekatan logika terprogram dan algoritma klasik, tanpa melibatkan modul *Machine Learning*.

## 6. Keterbatasan Sistem
* Pemetaan area masih terbatas pada model simulasi buatan di dalam program, bukan data geografis riil perkotaan.
* Parameter hambatan bersifat manual dari masukan pengguna (*user-defined*).
* Faktor eksternal seperti kondisi cuaca atau dinamika lalu lintas nyata tidak diperhitungkan.

## 7. Kebutuhan Sistem & Pustaka
* Interpreter Python versi 3.x.
* Pustaka `pygame` untuk merender tampilan visual grafis.

## 8. Panduan Penggunaan
1. Jalankan berkas utama program melalui terminal.
2. Tentukan titik asal dan algoritma penelusuran yang ingin diuji.
3. Tambahkan titik hambatan atau blokade jika diperlukan.
4. Amati hasil diagnosis rute, jarak tempuh, serta saran yang diberikan sistem pada layar visualisasi.
5. Gunakan tombol reset untuk mengulang simulasi.

## 9. Instruksi Eksekusi Program
```bash
git clone [https://github.com/RoyalRamliwisjtra/AI-TE-1303.git](https://github.com/RoyalRamliwisjtra/AI-TE-1303.git)
cd AI-TE-1303
pip install pygame --prefer-binary

python search_algorithm/astar.py
python search_algorithm/greedy_best_first.py
python expert_system/expert_system.py
