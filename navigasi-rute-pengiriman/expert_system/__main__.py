"""CLI mandiri expert system: python -m expert_system --berat 10 ..."""
import argparse
import json

from .engine import MesinInferensi, siapkan_fakta, NILAI_VALID


def main(argv=None):
    p = argparse.ArgumentParser(description="Expert system keputusan pengiriman")
    p.add_argument("--berat", type=float, required=True, help="berat barang (kg)")
    p.add_argument("--jenis", default="biasa", choices=NILAI_VALID["jenis_barang"])
    p.add_argument("--cuaca", default="cerah", choices=NILAI_VALID["cuaca"])
    p.add_argument("--kemacetan", default="rendah", choices=NILAI_VALID["kemacetan"])
    p.add_argument("--urgensi", default="normal", choices=NILAI_VALID["urgensi"])
    p.add_argument("--json", action="store_true", help="keluaran JSON")
    a = p.parse_args(argv)

    fakta = siapkan_fakta(a.berat, a.jenis, a.cuaca, a.kemacetan, a.urgensi)
    hasil = MesinInferensi.dari_file().inferensi(fakta)
    if a.json:
        print(json.dumps({"fakta": hasil.fakta, "jejak": hasil.penjelasan(),
                          "konflik": hasil.konflik}, indent=2, ensure_ascii=False))
        return
    print("Fakta akhir:")
    for k, v in hasil.fakta.items():
        print(f"  {k} = {v}")
    print("\nJejak penalaran:")
    for baris in hasil.penjelasan():
        print(" ", baris)
    if hasil.konflik:
        print("\nKonflik:", *hasil.konflik, sep="\n  ")


if __name__ == "__main__":
    main()
