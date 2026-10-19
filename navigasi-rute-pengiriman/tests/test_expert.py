import itertools
import unittest

from expert_system import MesinInferensi, siapkan_fakta, kategori_berat, NILAI_VALID

MESIN = MesinInferensi.dari_file()


def infer(berat=10, jenis="biasa", cuaca="cerah", macet="rendah", urgensi="normal"):
    return MESIN.inferensi(siapkan_fakta(berat, jenis, cuaca, macet, urgensi))


class TestExpertSystem(unittest.TestCase):
    def test_kategori_berat(self):
        self.assertEqual(kategori_berat(20), "ringan")
        self.assertEqual(kategori_berat(20.1), "sedang")
        self.assertEqual(kategori_berat(300), "sedang")
        self.assertEqual(kategori_berat(301), "berat")
        with self.assertRaises(ValueError):
            kategori_berat(0)

    def test_pemilihan_kendaraan(self):
        self.assertEqual(infer(10).fakta["kendaraan"], "motor")
        self.assertEqual(infer(100).fakta["kendaraan"], "mobil_box")
        self.assertEqual(infer(500).fakta["kendaraan"], "truk")

    def test_chaining_barang_mudah_pecah_naik_ke_mobil_box(self):
        h = infer(10, jenis="mudah_pecah")
        self.assertEqual(h.fakta["kendaraan_dasar"], "motor")
        self.assertEqual(h.fakta["kendaraan"], "mobil_box")
        ids = [a["id"] for a in h.jejak]
        self.assertLess(ids.index("R01"), ids.index("R05"))

    def test_chaining_hujan_macet_tinggi_memicu_buffer(self):
        h = infer(cuaca="hujan", macet="tinggi")
        self.assertEqual(h.fakta["tingkat_risiko"], "tinggi")
        self.assertEqual(h.fakta["buffer_waktu"], 1.3)
        self.assertTrue(any("waktu cadangan" in w for w in h.peringatan()))

    def test_tanpa_risiko_tidak_ada_buffer(self):
        self.assertNotIn("buffer_waktu", infer(cuaca="hujan", macet="sedang").fakta)

    def test_pilihan_algoritma(self):
        self.assertEqual(infer(urgensi="tinggi", macet="rendah").fakta["algoritma"], "greedy")
        self.assertEqual(infer(urgensi="tinggi", macet="tinggi").fakta["algoritma"], "astar")
        self.assertEqual(infer(urgensi="normal").fakta["algoritma"], "astar")

    def test_greedy_memicu_peringatan_tidak_optimal(self):
        h = infer(urgensi="tinggi", macet="rendah")
        self.assertIn("peringatan_algoritma", h.fakta)

    def test_peringatan_hujan_sesuai_kendaraan(self):
        self.assertIn("jas hujan", " ".join(infer(10, cuaca="hujan").peringatan()))
        self.assertIn("kecepatan truk", " ".join(infer(500, cuaca="hujan").peringatan()))

    def test_semua_kombinasi_input_menghasilkan_keputusan_lengkap_tanpa_konflik(self):
        for berat, jenis, cuaca, macet, urg in itertools.product(
                (10, 100, 500), NILAI_VALID["jenis_barang"], NILAI_VALID["cuaca"],
                NILAI_VALID["kemacetan"], NILAI_VALID["urgensi"]):
            h = infer(berat, jenis, cuaca, macet, urg)
            for kunci in ("kendaraan", "algoritma", "faktor_macet", "faktor_cuaca"):
                self.assertIn(kunci, h.fakta, (berat, jenis, cuaca, macet, urg))
            self.assertEqual(h.konflik, [], (berat, jenis, cuaca, macet, urg))

    def test_input_tidak_valid_ditolak(self):
        with self.assertRaises(ValueError):
            siapkan_fakta(10, "aneh", "cerah", "rendah", "normal")
        with self.assertRaises(ValueError):
            siapkan_fakta(-5, "biasa", "cerah", "rendah", "normal")

    def test_validasi_aturan(self):
        with self.assertRaises(ValueError):
            MesinInferensi([{"id": "X", "if": {}, "then": {"a": 1}}])
        with self.assertRaises(ValueError):
            MesinInferensi([{"id": "X", "if": {"a": 1}, "then": {"b": 1}},
                            {"id": "X", "if": {"a": 1}, "then": {"c": 1}}])

    def test_konflik_dicatat_dan_aturan_awal_menang(self):
        m = MesinInferensi([
            {"id": "A", "if": {"x": 1}, "then": {"y": "pertama"}},
            {"id": "B", "if": {"x": 1}, "then": {"y": "kedua"}}])
        h = m.inferensi({"x": 1})
        self.assertEqual(h.fakta["y"], "pertama")
        self.assertEqual(len(h.konflik), 1)

    def test_deterministik(self):
        self.assertEqual(infer(100, "dingin", "hujan", "sedang", "tinggi").fakta,
                         infer(100, "dingin", "hujan", "sedang", "tinggi").fakta)


if __name__ == "__main__":
    unittest.main()
