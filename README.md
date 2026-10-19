# Kelompok AI-TE1303: Sistem Navigasi & Sistem Pakar

Repository ini berisi tugas implementasi **Sistem Pakar** dan **Algoritma Pathfinding Visualization** (*A\*, Dijkstra, dan BFS*).

---

## Tangkapan Layar Program & Visualisasi:

### 1. Sistem Pakar Rekomendasi Navigasi (`expert_system/`)
```text
C:\Users\Royal\AI-TE-1303> python expert_system/sistem_pakar_navigasi.py
=== Sistem Pakar Rekomendasi Navigasi & Pengiriman ===
Jawab dengan y (ya) atau n (no).

Apakah jarak pengiriman tergolong jauh (> 10 km)? (y/n): y
Apakah pengiriman membutuhkan waktu sangat cepat (prioritas tinggi)? (y/n): n
Apakah rute memiliki banyak kemacetan / hambatan? (y/n): y
Apakah muatan paket berukuran besar / berat? (y/n): y
Apakah area tujuan berada di dalam gang / jalur sempit? (y/n): n

--- Rekomendasi Navigasi ---
- Mobil Box / Truk Pengiriman - Cocok untuk jarak jauh dan kapasitas besar.
- Rute Navigasi A* Search - Menghindari kemacetan berbasis nilai heuristik.
