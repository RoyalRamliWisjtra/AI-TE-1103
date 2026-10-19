import heapq
import math

lokasi = {
    "Gudang":   (0, 0),
    "Hub A":    (4, 1),
    "Hub B":    (3, 5),
    "Pasar":    (8, 2),
    "Kampus":   (7, 6),
    "Perumahan": (11, 5),
}

jalan = {
    "Gudang":    {"Hub A": 4.5, "Hub B": 6.0},
    "Hub A":     {"Gudang": 4.5, "Pasar": 4.5, "Kampus": 6.5},
    "Hub B":     {"Gudang": 6.0, "Kampus": 4.5},
    "Pasar":     {"Hub A": 4.5, "Perumahan": 4.0},
    "Kampus":    {"Hub A": 6.5, "Hub B": 4.5, "Perumahan": 4.5},
    "Perumahan": {"Pasar": 4.0, "Kampus": 4.5},
}


def heuristik(a, b):
    (x1, y1), (x2, y2) = lokasi[a], lokasi[b]
    return math.hypot(x2 - x1, y2 - y1)


def greedy_best_first(awal, tujuan):
    antrian = [(heuristik(awal, tujuan), awal, [awal], 0)]
    dikunjungi = set()

    while antrian:
        h, node, rute, g = heapq.heappop(antrian)
        if node == tujuan:
            return rute, g
        if node in dikunjungi:
            continue
        dikunjungi.add(node)

        for tetangga, jarak in jalan[node].items():
            if tetangga not in dikunjungi:
                heapq.heappush(
                    antrian,
                    (heuristik(tetangga, tujuan), tetangga, rute + [tetangga], g + jarak),
                )
    return None, float("inf")


if __name__ == "__main__":
    rute, total = greedy_best_first("Gudang", "Perumahan")
    print("Rute pengiriman :", " -> ".join(rute))
    print(f"Total jarak     : {total} km")
