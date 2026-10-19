"""Program utama: sistem navigasi rute pengiriman barang.

Contoh:
  python main.py --asal "Gudang Pusat" --tujuan Lembang --berat 15 --jenis mudah_pecah \
                 --cuaca hujan --kemacetan tinggi --urgensi tinggi
  python main.py --asal "Gudang Pusat" --tujuan "Ujung Berung" --berat 500 --bandingkan
  python main.py --daftar-lokasi
"""
import argparse
import json
import sys

from expert_system import NILAI_VALID
from planner import rencanakan, NAMA_ALGORITMA
from search_algorithm import ALGORITMA, buat_graf_bandung


def _cetak(r, tampil_jejak=True):
    print(f"Pengiriman : {r.asal} -> {r.tujuan}")
    print(f"Kendaraan  : {r.kendaraan}   (pengali biaya x{r.pengali_biaya:.2f})")
    print(f"Algoritma  : {NAMA_ALGORITMA[r.algoritma]}   (node diperluas: {r.diperluas})")
    if r.ditemukan:
        print(f"Rute       : {' -> '.join(r.jalur)}")
        print(f"Jarak      : {r.jarak_km:.1f} km  | biaya efektif: {r.biaya_efektif:.1f}")
        print(f"Estimasi   : {r.eta_menit:.0f} menit")
    for c in r.catatan:
        print(f"Catatan    : {c}")
    for w in r.peringatan:
        print(f"Peringatan : {w}")
    if tampil_jejak:
        print("\nPenjelasan expert system:")
        for baris in r.penjelasan:
            print(" ", baris)


def main(argv=None):
    graf = buat_graf_bandung()
    p = argparse.ArgumentParser(description="Navigasi rute pengiriman barang (expert system + search)")
    p.add_argument("--asal", default="Gudang Pusat")
    p.add_argument("--tujuan")
    p.add_argument("--berat", type=float, help="berat barang (kg)")
    p.add_argument("--jenis", default="biasa", choices=NILAI_VALID["jenis_barang"])
    p.add_argument("--cuaca", default="cerah", choices=NILAI_VALID["cuaca"])
    p.add_argument("--kemacetan", default="rendah", choices=NILAI_VALID["kemacetan"])
    p.add_argument("--urgensi", default="normal", choices=NILAI_VALID["urgensi"])
    p.add_argument("--algoritma", choices=sorted(ALGORITMA), help="paksa algoritma (default: pilihan expert system)")
    p.add_argument("--tutup", action="append", default=[], metavar="A-B",
                   help="tutup jalan, mis. --tutup 'Pasteur-Dago' (boleh diulang)")
    p.add_argument("--bandingkan", action="store_true", help="bandingkan semua algoritma")
    p.add_argument("--tanpa-jejak", action="store_true", help="sembunyikan penjelasan aturan")
    p.add_argument("--json", action="store_true", help="keluaran JSON")
    p.add_argument("--daftar-lokasi", action="store_true")
    a = p.parse_args(argv)

    if a.daftar_lokasi:
        print("\n".join(graf.lokasi()))
        return 0
    if not a.tujuan or a.berat is None:
        p.error("--tujuan dan --berat wajib diisi (atau pakai --daftar-lokasi)")

    ditutup = []
    for s in a.tutup:
        if "-" not in s:
            p.error(f"Format --tutup harus 'A-B', bukan '{s}'")
        u, v = s.split("-", 1)
        ditutup.append((u.strip(), v.strip()))

    try:
        kwargs = dict(asal=a.asal, tujuan=a.tujuan, berat_kg=a.berat, jenis_barang=a.jenis,
                      cuaca=a.cuaca, kemacetan=a.kemacetan, urgensi=a.urgensi,
                      ditutup=ditutup, graf=graf)
        if a.bandingkan:
            hasil = [rencanakan(algoritma=k, **kwargs) for k in ALGORITMA]
        else:
            hasil = [rencanakan(algoritma=a.algoritma, **kwargs)]
    except (KeyError, ValueError) as e:
        print(f"Error: {e.args[0]}", file=sys.stderr)
        return 2

    if a.json:
        print(json.dumps([r.__dict__ for r in hasil], indent=2, ensure_ascii=False, default=str))
        return 0
    if a.bandingkan:
        r0 = hasil[0]
        print(f"Perbandingan algoritma: {r0.asal} -> {r0.tujuan} | kendaraan {r0.kendaraan} | x{r0.pengali_biaya:.2f}\n")
        print(f"{'Algoritma':<10}{'Biaya':>8}{'ETA(mnt)':>10}{'Diperluas':>11}  Rute")
        for r in hasil:
            if r.ditemukan:
                print(f"{NAMA_ALGORITMA[r.algoritma]:<10}{r.biaya_efektif:>8.1f}{r.eta_menit:>10.0f}{r.diperluas:>11}  {' > '.join(r.jalur)}")
            else:
                print(f"{NAMA_ALGORITMA[r.algoritma]:<10}{'-':>8}{'-':>10}{r.diperluas:>11}  (tidak ada rute)")
        print("\nPeringatan expert system:")
        for w in r0.peringatan or ["(tidak ada)"]:
            print(" ", w)
        return 0
    _cetak(hasil[0], tampil_jejak=not a.tanpa_jejak)
    return 0 if hasil[0].ditemukan else 1


if __name__ == "__main__":
    sys.exit(main())
