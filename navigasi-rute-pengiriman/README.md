# Sistem Navigasi Rute Pengiriman Barang

[![Tests](https://github.com/USERNAME/navigasi-rute-pengiriman/actions/workflows/tests.yml/badge.svg)](https://github.com/USERNAME/navigasi-rute-pengiriman/actions/workflows/tests.yml)

Program Python yang menggabungkan **Expert System** (aturan IF-THEN, forward chaining) dan
**Search Algorithm** (BFS, UCS, Greedy Best-First, A*) untuk menentukan kendaraan,
rute, dan estimasi waktu pengiriman barang.

Hanya memakai pustaka standar Python 3.9+, tanpa dependensi eksternal.

## Cara kerja

```
input pengguna ──► Expert System (forward chaining, rules.json)
(berat, jenis, cuaca,      │  menghasilkan: kendaraan, pengali biaya (macet x cuaca),
 macet, urgensi)           │  algoritma yang disarankan, peringatan, waktu cadangan
                           ▼
                 Graf jalan dibangun sesuai kendaraan
                 (truk dilarang di jalan sempit, jalan bisa ditutup, biaya x pengali)
                           ▼
                 Search Algorithm ──► rute, jarak, biaya efektif, ETA
```

Contoh rantai inferensi (multi-hop): `berat ringan → kendaraan_dasar=motor`, lalu
`motor + barang mudah pecah → kendaraan=mobil_box`; `hujan + macet tinggi → tingkat_risiko=tinggi → buffer_waktu x1.3`.

## Struktur proyek

```
├── main.py                  # CLI utama
├── planner.py               # penghubung expert system + search
├── search_algorithm/
│   ├── graph.py             # graf kota (contoh: Bandung) dan filter kendaraan
│   └── algorithms.py        # BFS, UCS, Greedy, A*
├── expert_system/
│   ├── rules.json           # basis pengetahuan (22 aturan), mudah diedit
│   ├── engine.py            # mesin inferensi forward chaining + penjelasan
│   └── __main__.py          # CLI expert system mandiri
├── tests/                   # 29 unit test
└── .github/workflows/       # CI GitHub Actions
```

## Cara menjalankan

```bash
git clone https://github.com/USERNAME/navigasi-rute-pengiriman.git
cd navigasi-rute-pengiriman

python main.py --daftar-lokasi
python main.py --asal "Gudang Pusat" --tujuan Lembang --berat 15 --jenis mudah_pecah \
               --cuaca hujan --kemacetan tinggi --urgensi tinggi
```

Keluaran:

```
Pengiriman : Gudang Pusat -> Lembang
Kendaraan  : mobil_box   (pengali biaya x2.04)
Algoritma  : A*   (node diperluas: 7)
Rute       : Gudang Pusat -> Pasteur -> Dago -> Lembang
Jarak      : 25.7 km  | biaya efektif: 52.4
Estimasi   : 136 menit
Peringatan : Risiko tinggi: tambahkan waktu cadangan 30% pada estimasi tiba.
Peringatan : Barang mudah pecah: beri pengaman dan hindari rem mendadak.
```

### Membandingkan semua algoritma

```bash
python main.py --asal "Gudang Pusat" --tujuan "Ujung Berung" --berat 500 --kemacetan sedang --bandingkan
```

```
Algoritma    Biaya  ETA(mnt)  Diperluas  Rute
BFS           38.7        93         10  Gudang Pusat > Buah Batu > Gedebage > Ujung Berung
Greedy        38.7        93          4  Gudang Pusat > Buah Batu > Gedebage > Ujung Berung
A*            35.0        84          8  Gudang Pusat > Buah Batu > Kiaracondong > Ujung Berung
UCS           35.0        84          9  Gudang Pusat > Buah Batu > Kiaracondong > Ujung Berung
```

A* dan UCS menghasilkan biaya optimal, A* memperluas lebih sedikit node. Greedy paling sedikit
memperluas node tetapi tidak menjamin optimal. BFS hanya meminimalkan jumlah ruas jalan.

### Opsi lain

| Opsi | Fungsi |
|------|--------|
| `--algoritma {bfs,greedy,astar,ucs}` | paksa algoritma (default: saran expert system) |
| `--tutup "Pasteur-Dago"` | tutup sebuah jalan (boleh diulang) |
| `--tanpa-jejak` | sembunyikan penjelasan aturan |
| `--json` | keluaran JSON |

### Expert system saja

```bash
python -m expert_system --berat 10 --jenis dingin --cuaca hujan --kemacetan sedang --urgensi tinggi
```

## Menjalankan tes

```bash
python -m unittest discover -s tests -v
```

Tes mencakup: A* selalu sama optimal dengan UCS untuk semua pasangan lokasi dan kendaraan,
validitas jalur semua algoritma, pembatasan truk, jalan ditutup, rute tidak ada, seluruh 162
kombinasi input expert system (tanpa konflik), validasi aturan, dan CLI.

## Menyesuaikan

- **Menambah/mengubah aturan**: edit `expert_system/rules.json`. Format:
  `{"id": "R23", "if": {"cuaca": "hujan"}, "then": {"fakta_baru": "nilai"}, "alasan": "..."}`.
  Nilai kondisi boleh berupa daftar (salah satu dari). Fakta berawalan `faktor_` otomatis
  dikalikan ke biaya jalan; berawalan `peringatan_` otomatis tampil sebagai peringatan.
- **Mengganti peta**: ubah `buat_graf_bandung()` di `search_algorithm/graph.py`
  (koordinat km, faktor kelokan >= 1.0, dan kendaraan yang diizinkan per jalan).

## Batasan

- Peta berupa contoh sederhana, bukan data jalan nyata.
- Heuristik A* memakai jarak garis lurus. Ini admissible selama faktor kelokan dan pengali biaya >= 1.
- Aturan expert system bersifat ilustrasi dan belum divalidasi pakar logistik.
- Satu pengiriman, satu kendaraan, tanpa jendela waktu atau kapasitas multi-titik (VRP).

## Ide pengembangan

Antarmuka Streamlit, dukungan banyak titik antar (TSP/VRP), data peta OpenStreetMap,
certainty factor pada aturan, dan backward chaining untuk menjelaskan "mengapa kendaraan ini dipilih".
