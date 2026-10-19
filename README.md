dev1-Dwi-Zarfa
# Search Algorithm - Rute Pengiriman Barang

## Deskripsi
Implementasi informed search (A* dan Greedy Best-First) untuk mencari
rute dari gudang ke lokasi tujuan. Heuristik: jarak garis lurus.

## Requirement / Library
- Python 3.x
- Library bawaan saja (`heapq`, `math`)

## How to Use
Ubah data `lokasi` dan `jalan` di bagian atas file, lalu ubah titik
awal dan tujuan di bagian `__main__`.

## Running
python search_algorithm/astar.py
python search_algorithm/greedy_best_first.py
=======
# Expert System - Rekomendasi Pengiriman Barang

## Deskripsi
Sistem pakar berbasis aturan (rule-based) yang merekomendasikan
kendaraan dan layanan pengiriman dari berat, jarak, dan kondisi barang.

## Requirement / Library
- Python 3.x
- Tidak perlu library tambahan

## How to Use
Jalankan program, lalu jawab pertanyaan yang muncul. Aturan dapat
diubah pada daftar `aturan` di `expert_system/expert_system.py`.

## Running
python expert_system/expert_system.py
main
