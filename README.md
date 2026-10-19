# Kelompok AI-TE1303: Sistem Navigasi & Sistem Pakar

EvacRoute AI / Sistem Navigasi Rute Pengiriman Barang & Sistem Pakar Tugas 1, Kecerdasan Buatan: Search Algorithm dan Expert System (rule-based)

Peran | Nama | Branch
--- | --- | ---
Main | Royal Ramli Wisjtra | `main`
Dev 1 | Dwi Zarfa K | `dev1`
Dev 2 | Abimanyu Aziz | `dev2`

---

## 1. Deskripsi
Sistem Navigasi Rute Pengiriman Barang adalah aplikasi sederhana yang membantu menentukan rute pengiriman tercepat dari suatu titik gudang menuju lokasi tujuan pada model jaringan distribusi. Pengguna dapat menandai area yang terdampak hambatan (misalnya kemacetan atau jalur diblokir), lalu sistem mencari rute alternatif dan memberi status serta saran keselamatan pengiriman.

## 2. Tujuan
- Menerapkan algoritma pencarian (*search*) pada masalah nyata.
- Membandingkan algoritma *uninformed* (BFS, Dijkstra) dan *informed* (A*).
- Menerapkan sistem pakar sederhana berbasis aturan untuk menafsirkan hasil pencarian rute.

## 3. Teknologi
- Python 3.x: bahasa pemrograman utama.
- Pygame: antarmuka grafis (*GUI*) yang menampilkan peta grid dan visualisasi rute.
- BFS, Dijkstra, A*: algoritma pencarian rute.
- Rule-based expert system: aturan JIKA-MAKA untuk menentukan status dan saran pengiriman.

## 4. Cara Kerja Sistem
1. Pengguna memilih lokasi awal, algoritma, dan area hambatan/blokir.
2. Peta dibaca dari program sebagai graf: titik = node, jalur = edge berbobot (jarak meter).
3. Algoritma mencari rute ke tujuan akhir yang tidak terblokir, tanpa melewati area hambatan.
4. Hasil pencarian menjadi fakta untuk sistem pakar (apakah ada rute, berapa jalur alternatif tersisa, seberapa jauh, apakah harus memutar).
5. Aturan yang cocok menghasilkan status AMAN / WASPADA / BAHAYA dan saran operasional.
6. Rute digambar secara visual di layar.

Algoritma | Jenis | Menghasilkan | Optimal?
--- | --- | --- | ---
BFS | Uninformed | Rute dengan jumlah langkah paling sedikit | Hanya untuk jumlah langkah
Dijkstra | Uninformed | Rute dengan jarak (meter) terpendek | Ya
A* | Informed | Sama seperti Dijkstra, dipandu heuristik jarak garis lurus | Ya

*Informed vs uninformed:* BFS dan Dijkstra tidak tahu arah tujuan secara langsung. A* memakai heuristik (jarak garis lurus pada peta ke tujuan), sehingga biasanya mengekspansi lebih sedikit node.

## 5. Peran Kecerdasan Buatan
- **Search:** BFS, Dijkstra, dan A* menjadi inti pencarian rute.
- **Expert system:** Aturan pada modul sistem pakar menafsirkan hasil pencarian menjadi status operasional dan saran.
Sistem ini berbasis algoritma dan aturan, bukan *machine learning*.

## 6. Batasan Sistem
- Peta jaringan adalah model contoh di dalam program, bukan kondisi jalan raya sebenarnya.
- Area hambatan dimasukkan manual oleh pengguna; sistem tidak mendeteksi lalu lintas secara *real-time*.
- Kepadatan kendaraan dan cuaca tidak dimodelkan.
- Hasil hanya alat bantu simulasi dan pembelajaran.

## 7. Library / Kebutuhan
- Python 3.x.
- Pygame (`pip install pygame --prefer-binary`).

## 8. Cara Pakai
1. Jalankan aplikasi utama.
2. Pilih titik awal dan algoritma pencarian.
3. (Opsional) Pilih area terdampak hambatan.
4. Jalankan diagnosis: status, rute, jarak, dan saran akan muncul, serta rute digambar pada visualisasi.
5. Reset untuk mengosongkan area hambatan.

## 9. Cara Menjalankan
```bash
git clone [https://github.com/RoyalRamliwisjtra/AI-TE-1303.git](https://github.com/RoyalRamliwisjtra/AI-TE-1303.git)
cd AI-TE-1303
pip install pygame --prefer-binary

python search_algorithm/visualisasi_pathfinding.py    # Menjalankan Visualisasi Pathfinding
python expert_system/expert_system.py        
