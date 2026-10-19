import unittest

from search_algorithm import buat_graf_bandung, a_star, ucs, bfs, greedy, ALGORITMA

GRAF = buat_graf_bandung()
KENDARAAN = ("motor", "mobil_box", "truk")


class TestPencarian(unittest.TestCase):
    def test_astar_sama_optimal_dengan_ucs_untuk_semua_pasangan(self):
        for kend in KENDARAAN:
            for pengali in (1.0, 1.7 * 1.2):
                adj = GRAF.bangun(kend, pengali)
                for s in GRAF.lokasi():
                    for t in GRAF.lokasi():
                        ra, ru = a_star(adj, GRAF.koordinat, s, t), ucs(adj, GRAF.koordinat, s, t)
                        self.assertEqual(ra.ditemukan, ru.ditemukan)
                        if ra.ditemukan:
                            self.assertAlmostEqual(ra.biaya, ru.biaya, places=9, msg=f"{kend} {s}->{t}")

    def test_semua_jalur_valid_dan_dimulai_dari_asal(self):
        adj = GRAF.bangun("mobil_box")
        for nama, fn in ALGORITMA.items():
            r = fn(adj, GRAF.koordinat, "Gudang Pusat", "Lembang")
            self.assertTrue(r.ditemukan, nama)
            self.assertEqual((r.jalur[0], r.jalur[-1]), ("Gudang Pusat", "Lembang"))
            for u, v in zip(r.jalur, r.jalur[1:]):
                self.assertIn(v, [n for n, _ in adj[u]], f"{nama}: {u}->{v} bukan jalan")

    def test_bfs_minimal_jumlah_ruas(self):
        adj = GRAF.bangun("motor")
        r = bfs(adj, GRAF.koordinat, "Gudang Pusat", "Lembang")
        self.assertEqual(len(r.jalur) - 1, 2)  # Gudang -> Pasteur -> Lembang

    def test_truk_tidak_lewat_jalan_sempit(self):
        adj = GRAF.bangun("truk")
        r = a_star(adj, GRAF.koordinat, "Gudang Pusat", "Lembang")
        self.assertTrue(r.ditemukan)
        self.assertNotIn(("Dago", "Lembang"), list(zip(r.jalur, r.jalur[1:])))
        self.assertNotIn(("Lembang", "Dago"), list(zip(r.jalur, r.jalur[1:])))

    def test_jalan_ditutup_memaksa_rute_lain(self):
        normal = a_star(GRAF.bangun("motor"), GRAF.koordinat, "Gudang Pusat", "Dago")
        tutup = a_star(GRAF.bangun("motor", ditutup=[("Pasteur", "Dago")]), GRAF.koordinat, "Gudang Pusat", "Dago")
        self.assertTrue(tutup.ditemukan)
        self.assertGreater(tutup.biaya, normal.biaya)

    def test_tidak_ada_rute_jika_terisolasi(self):
        semua = [(j.a, j.b) for j in GRAF.jalan if "Soreang" in (j.a, j.b)]
        for fn in (bfs, greedy, a_star, ucs):
            r = fn(GRAF.bangun("motor", ditutup=semua), GRAF.koordinat, "Gudang Pusat", "Soreang")
            self.assertFalse(r.ditemukan)

    def test_asal_sama_tujuan(self):
        r = a_star(GRAF.bangun("motor"), GRAF.koordinat, "Dago", "Dago")
        self.assertEqual(r.jalur, ["Dago"])
        self.assertEqual(r.biaya, 0)

    def test_lokasi_tidak_dikenal(self):
        with self.assertRaises(KeyError):
            a_star(GRAF.bangun("motor"), GRAF.koordinat, "Mars", "Dago")

    def test_pengali_di_bawah_satu_ditolak(self):
        with self.assertRaises(ValueError):
            GRAF.bangun("motor", pengali=0.5)


if __name__ == "__main__":
    unittest.main()
