"""Mesin inferensi forward chaining berbasis aturan IF-THEN dari rules.json.

Cara kerja:
1. Mulai dari fakta awal (hasil input pengguna).
2. Setiap putaran, cari aturan yang semua kondisinya terpenuhi dan belum dipakai.
3. Jalankan aturan: tambahkan fakta baru. Jika fakta sudah ada dengan nilai lain,
   fakta lama dipertahankan (aturan yang lebih awal berprioritas) dan konflik dicatat.
4. Ulangi sampai tidak ada aturan baru yang aktif (fixpoint).
Setiap aturan yang aktif dicatat di jejak agar kesimpulan bisa dijelaskan.
"""
from dataclasses import dataclass, field
from pathlib import Path
import json

RULES_PATH = Path(__file__).with_name("rules.json")

NILAI_VALID = {
    "jenis_barang": ("biasa", "mudah_pecah", "dingin"),
    "cuaca": ("cerah", "hujan"),
    "kemacetan": ("rendah", "sedang", "tinggi"),
    "urgensi": ("rendah", "normal", "tinggi"),
}


def kategori_berat(berat_kg):
    if berat_kg <= 0:
        raise ValueError("Berat barang harus lebih dari 0 kg")
    if berat_kg <= 20:
        return "ringan"
    if berat_kg <= 300:
        return "sedang"
    return "berat"


def siapkan_fakta(berat_kg, jenis_barang, cuaca, kemacetan, urgensi):
    """Validasi input pengguna dan ubah menjadi fakta awal."""
    masukan = {"jenis_barang": jenis_barang, "cuaca": cuaca,
               "kemacetan": kemacetan, "urgensi": urgensi}
    for kunci, nilai in masukan.items():
        if nilai not in NILAI_VALID[kunci]:
            raise ValueError(f"{kunci} harus salah satu dari {NILAI_VALID[kunci]}, bukan '{nilai}'")
    fakta = dict(masukan)
    fakta["berat_kategori"] = kategori_berat(berat_kg)
    return fakta


@dataclass
class Hasil:
    fakta: dict                                   # fakta awal + fakta turunan
    jejak: list = field(default_factory=list)     # aturan yang aktif, berurutan
    konflik: list = field(default_factory=list)   # fakta yang ditolak karena sudah ada

    def peringatan(self):
        return [v for k, v in self.fakta.items() if k.startswith("peringatan_")]

    def penjelasan(self):
        baris = []
        for j in self.jejak:
            kondisi = " DAN ".join(
                f"{k}={'/'.join(v) if isinstance(v, list) else v}" for k, v in j["if"].items())
            hasil = ", ".join(f"{k}={v}" for k, v in j["then"].items())
            baris.append(f"[{j['id']}] JIKA {kondisi} MAKA {hasil}  ({j['alasan']})")
        return baris


def _cocok(kondisi, fakta):
    for kunci, diminta in kondisi.items():
        if kunci not in fakta:
            return False
        nilai = fakta[kunci]
        if isinstance(diminta, list):
            if nilai not in diminta:
                return False
        elif nilai != diminta:
            return False
    return True


class MesinInferensi:
    def __init__(self, aturan):
        self.aturan = list(aturan)
        self._validasi()

    @classmethod
    def dari_file(cls, path=RULES_PATH):
        with open(path, encoding="utf-8") as f:
            return cls(json.load(f)["aturan"])

    def _validasi(self):
        ids = set()
        for a in self.aturan:
            for kunci in ("id", "if", "then"):
                if kunci not in a:
                    raise ValueError(f"Aturan tidak punya kunci '{kunci}': {a}")
            if a["id"] in ids:
                raise ValueError(f"ID aturan ganda: {a['id']}")
            ids.add(a["id"])
            if not a["if"] or not a["then"]:
                raise ValueError(f"Aturan {a['id']} harus punya kondisi dan hasil")
            a.setdefault("alasan", "")

    def inferensi(self, fakta_awal):
        fakta = dict(fakta_awal)
        hasil = Hasil(fakta)
        terpakai = set()
        ada_perubahan = True
        while ada_perubahan:
            ada_perubahan = False
            for a in self.aturan:
                if a["id"] in terpakai or not _cocok(a["if"], fakta):
                    continue
                terpakai.add(a["id"])
                ada_perubahan = True
                for kunci, nilai in a["then"].items():
                    if kunci in fakta and fakta[kunci] != nilai:
                        hasil.konflik.append(f"{a['id']} ingin {kunci}={nilai} tetapi sudah {fakta[kunci]}")
                    elif kunci not in fakta:
                        fakta[kunci] = nilai
                hasil.jejak.append(a)
        return hasil
