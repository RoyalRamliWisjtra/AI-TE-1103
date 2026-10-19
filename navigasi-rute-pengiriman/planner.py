"""Penghubung expert system dan search algorithm.

Alur:
  input pengguna -> fakta -> expert system (forward chaining)
      -> kendaraan, pengali biaya, algoritma, peringatan
      -> graf dibangun sesuai kendaraan dan kondisi
      -> algoritma pencarian -> rute, jarak, ETA
"""
from dataclasses import dataclass, field
import math

from expert_system import MesinInferensi, siapkan_fakta
from search_algorithm import ALGORITMA, buat_graf_bandung

KECEPATAN_KMH = {"motor": 35, "mobil_box": 30, "truk": 25}
NAMA_ALGORITMA = {"bfs": "BFS", "greedy": "Greedy", "astar": "A*", "ucs": "UCS"}


@dataclass
class Rencana:
    asal: str
    tujuan: str
    fakta: dict
    penjelasan: list
    peringatan: list
    kendaraan: str
    pengali_biaya: float
    algoritma: str              # kunci algoritma yang dipakai
    ditemukan: bool
    jalur: list = field(default_factory=list)
    jarak_km: float = 0.0       # jarak dasar jalur
    biaya_efektif: float = 0.0  # jarak setelah dikali macet dan cuaca
    eta_menit: float = 0.0
    diperluas: int = 0
    catatan: list = field(default_factory=list)


def pengali_dari_fakta(fakta):
    """Kalikan semua fakta berawalan 'faktor_' (macet, cuaca, dst)."""
    return math.prod(v for k, v in fakta.items() if k.startswith("faktor_"))


def rencanakan(asal, tujuan, berat_kg, jenis_barang="biasa", cuaca="cerah",
               kemacetan="rendah", urgensi="normal", algoritma=None,
               ditutup=(), graf=None, mesin=None):
    graf = graf or buat_graf_bandung()
    mesin = mesin or MesinInferensi.dari_file()
    for lokasi in (asal, tujuan):
        if lokasi not in graf.koordinat:
            raise KeyError(f"Lokasi tidak dikenal: {lokasi}. Pilihan: {', '.join(graf.lokasi())}")
    if algoritma is not None and algoritma not in ALGORITMA:
        raise ValueError(f"Algoritma harus salah satu dari {sorted(ALGORITMA)}")

    fakta = siapkan_fakta(berat_kg, jenis_barang, cuaca, kemacetan, urgensi)
    hasil = mesin.inferensi(fakta)
    f = hasil.fakta

    kendaraan = f["kendaraan"]
    pengali = pengali_dari_fakta(f)
    kunci_algo = algoritma or f["algoritma"]
    catatan = []
    if algoritma and algoritma != f["algoritma"]:
        catatan.append(f"Algoritma dipilih manual ({NAMA_ALGORITMA[algoritma]}), "
                       f"rekomendasi expert system: {NAMA_ALGORITMA[f['algoritma']]}.")

    adj = graf.bangun(kendaraan, pengali, ditutup)
    cari = ALGORITMA[kunci_algo](adj, graf.koordinat, asal, tujuan)

    rencana = Rencana(
        asal=asal, tujuan=tujuan, fakta=f, penjelasan=hasil.penjelasan(),
        peringatan=hasil.peringatan(), kendaraan=kendaraan, pengali_biaya=pengali,
        algoritma=kunci_algo, ditemukan=cari.ditemukan, diperluas=cari.diperluas,
        catatan=catatan)
    if cari.ditemukan:
        rencana.jalur = cari.jalur
        rencana.jarak_km = graf.jarak_jalur(cari.jalur)
        rencana.biaya_efektif = cari.biaya
        buffer = f.get("buffer_waktu", 1.0)
        rencana.eta_menit = cari.biaya / KECEPATAN_KMH[kendaraan] * 60 * buffer
    else:
        rencana.catatan.append(
            f"Tidak ada rute untuk {kendaraan} dari {asal} ke {tujuan} "
            "(cek jalan yang ditutup atau pembatasan kendaraan).")
    return rencana
