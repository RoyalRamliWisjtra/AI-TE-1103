"""Graf jaringan jalan (contoh: Bandung dan sekitarnya, koordinat disederhanakan).

Setiap lokasi punya koordinat (x, y) dalam km pada peta abstrak. Jarak jalan
dihitung dari garis lurus dikali faktor kelokan (>= 1), sehingga heuristik jarak
garis lurus selalu admissible untuk A*.
"""
from dataclasses import dataclass
import math

SEMUA_KENDARAAN = ("motor", "mobil_box", "truk")


@dataclass(frozen=True)
class Jalan:
    a: str
    b: str
    faktor: float = 1.3                 # faktor kelokan jalan (>= 1.0)
    akses: tuple = SEMUA_KENDARAAN      # kendaraan yang boleh lewat


class GrafKota:
    def __init__(self, koordinat, jalan):
        self.koordinat = dict(koordinat)
        self.jalan = list(jalan)
        self._jarak = {}
        for j in self.jalan:
            if j.a not in self.koordinat or j.b not in self.koordinat:
                raise ValueError(f"Jalan {j.a}-{j.b} memakai lokasi yang tidak terdaftar")
            if j.faktor < 1.0:
                raise ValueError(f"Faktor jalan {j.a}-{j.b} harus >= 1.0")
            self._jarak[frozenset((j.a, j.b))] = self.garis_lurus(j.a, j.b) * j.faktor

    def garis_lurus(self, a, b):
        (x1, y1), (x2, y2) = self.koordinat[a], self.koordinat[b]
        return math.hypot(x1 - x2, y1 - y2)

    def lokasi(self):
        return sorted(self.koordinat)

    def jarak_jalan(self, a, b):
        return self._jarak[frozenset((a, b))]

    def jarak_jalur(self, jalur):
        """Total jarak dasar (km) sebuah jalur, tanpa pengali kondisi."""
        return sum(self.jarak_jalan(u, v) for u, v in zip(jalur, jalur[1:]))

    def bangun(self, kendaraan, pengali=1.0, ditutup=()):
        """Bangun adjacency list untuk satu kendaraan.

        pengali : faktor biaya global (macet, cuaca) dari expert system, >= 1.
        ditutup : iterable pasangan (a, b) jalan yang ditutup.
        """
        if pengali < 1.0:
            raise ValueError("pengali biaya harus >= 1.0 agar heuristik tetap admissible")
        tutup = {frozenset(p) for p in ditutup}
        adj = {n: [] for n in self.koordinat}
        for j in self.jalan:
            if kendaraan not in j.akses or frozenset((j.a, j.b)) in tutup:
                continue
            biaya = self._jarak[frozenset((j.a, j.b))] * pengali
            adj[j.a].append((j.b, biaya))
            adj[j.b].append((j.a, biaya))
        for n in adj:
            adj[n].sort()
        return adj


def buat_graf_bandung():
    koordinat = {
        "Gudang Pusat": (0, 0), "Cimahi": (-5, 5), "Pasteur": (1, 6),
        "Dago": (5, 9), "Lembang": (6, 17), "Kiaracondong": (9, 2),
        "Buah Batu": (6, -3), "Soreang": (-2, -9), "Gedebage": (14, -1),
        "Ujung Berung": (16, 7),
    }
    sempit = ("motor", "mobil_box")  # truk tidak boleh lewat jalan sempit
    jalan = [
        Jalan("Gudang Pusat", "Cimahi", 1.3),
        Jalan("Gudang Pusat", "Pasteur", 1.25),
        Jalan("Gudang Pusat", "Buah Batu", 1.3),
        Jalan("Gudang Pusat", "Soreang", 1.4),
        Jalan("Cimahi", "Pasteur", 1.3),
        Jalan("Pasteur", "Dago", 1.2),
        Jalan("Pasteur", "Kiaracondong", 1.3),
        Jalan("Pasteur", "Lembang", 1.6),
        Jalan("Dago", "Lembang", 1.5, sempit),
        Jalan("Dago", "Ujung Berung", 1.4),
        Jalan("Kiaracondong", "Buah Batu", 1.2),
        Jalan("Kiaracondong", "Gedebage", 1.3),
        Jalan("Kiaracondong", "Ujung Berung", 1.3),
        Jalan("Buah Batu", "Gedebage", 1.3),
        Jalan("Buah Batu", "Soreang", 1.35),
        Jalan("Gedebage", "Ujung Berung", 1.25),
    ]
    return GrafKota(koordinat, jalan)
