from uninformed_search import bfs_search
from informed_search import greedy_search

# REPRESENTASI GRAF (Peta Lokasi / Titik Pengiriman Barang)
graph = {
    'Gudang Utama': [('Pos 1', 4), ('Pos 2', 2)],
    'Pos 1': [('Pos 3', 5), ('Pos 4', 10)],
    'Pos 2': [('Pos 4', 3), ('Pos 5', 8)],
    'Pos 3': [('Tujuan Akhir', 7)],
    'Pos 4': [('Tujuan Akhir', 2)],
    'Pos 5': [('Tujuan Akhir', 4)],
    'Tujuan Akhir': []
}

# Nilai Heuristic (Perkiraan jarak garis lurus ke 'Tujuan Akhir')
heuristic = {
    'Gudang Utama': 8,
    'Pos 1': 6,
    'Pos 2': 4,
    'Pos 3': 5,
    'Pos 4': 2,
    'Pos 5': 3,
    'Tujuan Akhir': 0
}

# PROGRAM UTAMA
if __name__ == "__main__":
    start_point = 'Gudang Utama'
    target_point = 'Tujuan Akhir'
    
    print("=" * 60)
    print("SISTEM NAVIGASI RUTE PENGIRIMAN BARANG")
    print("=" * 60)
    print(f"Titik Awal  : {start_point}")
    print(f"Titik Tujuan: {target_point}\n")
    
    # Eksekusi Uninformed Search
    rute_bfs = bfs_search(graph, start_point, target_point)
    print("[1] Uninformed Search (BFS)")
    print(f"    Rute ditemukan: {' -> '.join(rute_bfs) if rute_bfs else 'Tidak ditemukan'}\n")
    
    # Eksekusi Informed Search
    rute_greedy = greedy_search(graph, heuristic, start_point, target_point)
    print("[2] Informed Search (Greedy Best-First Search)")
    print(f"    Rute ditemukan: {' -> '.join(rute_greedy) if rute_greedy else 'Tidak ditemukan'}")
    print("=" * 60)