"""Algoritma pencarian rute.

Uninformed : BFS (jumlah ruas paling sedikit), UCS (biaya paling kecil)
Informed   : Greedy Best-First (h saja), A* (g + h)

Semua fungsi menerima (adj, koordinat, mulai, tujuan) dan mengembalikan HasilCari.
Hanya memakai pustaka standar Python.
"""
from collections import deque
from dataclasses import dataclass, field
import heapq
import itertools
import math


@dataclass
class HasilCari:
    algoritma: str
    ditemukan: bool
    jalur: list = field(default_factory=list)
    biaya: float = math.inf
    diperluas: int = 0          # jumlah node yang diekspansi


def _heuristik(koordinat, n, tujuan):
    (x1, y1), (x2, y2) = koordinat[n], koordinat[tujuan]
    return math.hypot(x1 - x2, y1 - y2)


def _rekonstruksi(induk, tujuan):
    jalur, n = [], tujuan
    while n is not None:
        jalur.append(n)
        n = induk[n]
    return jalur[::-1]


def _biaya_jalur(adj, jalur):
    total = 0.0
    for u, v in zip(jalur, jalur[1:]):
        total += next(c for nb, c in adj[u] if nb == v)
    return total


def _selesai(nama, adj, induk, tujuan, diperluas):
    jalur = _rekonstruksi(induk, tujuan)
    return HasilCari(nama, True, jalur, _biaya_jalur(adj, jalur), diperluas)


def _validasi(adj, mulai, tujuan):
    for n in (mulai, tujuan):
        if n not in adj:
            raise KeyError(f"Lokasi tidak dikenal: {n}")


def bfs(adj, koordinat, mulai, tujuan):
    _validasi(adj, mulai, tujuan)
    antrian, induk, diperluas = deque([mulai]), {mulai: None}, 0
    while antrian:
        n = antrian.popleft()
        diperluas += 1
        if n == tujuan:
            return _selesai("BFS", adj, induk, tujuan, diperluas)
        for tetangga, _ in adj[n]:
            if tetangga not in induk:
                induk[tetangga] = n
                antrian.append(tetangga)
    return HasilCari("BFS", False, diperluas=diperluas)


def _best_first(nama, adj, koordinat, mulai, tujuan, pakai_g, pakai_h):
    """Kerangka umum: UCS (g), Greedy (h), A* (g + h)."""
    _validasi(adj, mulai, tujuan)
    urutan = itertools.count()          # penentu urutan jika prioritas sama
    h = (lambda n: _heuristik(koordinat, n, tujuan)) if pakai_h else (lambda n: 0.0)
    g_terbaik = {mulai: 0.0}
    induk = {mulai: None}
    selesai, diperluas = set(), 0
    heap = [(h(mulai), next(urutan), 0.0, mulai)]
    while heap:
        _, _, g, n = heapq.heappop(heap)
        if n in selesai:
            continue
        selesai.add(n)
        diperluas += 1
        if n == tujuan:
            return _selesai(nama, adj, induk, tujuan, diperluas)
        for tetangga, biaya in adj[n]:
            g2 = g + biaya
            if tetangga in selesai:
                continue
            if pakai_g:
                if g2 >= g_terbaik.get(tetangga, math.inf):
                    continue
                g_terbaik[tetangga] = g2
                induk[tetangga] = n
            elif tetangga not in induk:  # Greedy: induk pertama dipertahankan
                induk[tetangga] = n
            prioritas = (g2 if pakai_g else 0.0) + h(tetangga)
            heapq.heappush(heap, (prioritas, next(urutan), g2, tetangga))
    return HasilCari(nama, False, diperluas=diperluas)


def ucs(adj, koordinat, mulai, tujuan):
    return _best_first("UCS", adj, koordinat, mulai, tujuan, True, False)


def greedy(adj, koordinat, mulai, tujuan):
    return _best_first("Greedy", adj, koordinat, mulai, tujuan, False, True)


def a_star(adj, koordinat, mulai, tujuan):
    return _best_first("A*", adj, koordinat, mulai, tujuan, True, True)


ALGORITMA = {"bfs": bfs, "greedy": greedy, "astar": a_star, "ucs": ucs}
