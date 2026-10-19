import unittest

from planner import rencanakan
import main as cli


class TestIntegrasi(unittest.TestCase):
    def test_truk_ke_lembang_lewat_pasteur(self):
        r = rencanakan("Gudang Pusat", "Lembang", 500)
        self.assertEqual(r.kendaraan, "truk")
        self.assertTrue(r.ditemukan)
        self.assertEqual(r.jalur[-2:], ["Pasteur", "Lembang"])

    def test_motor_ke_lembang_boleh_lewat_dago(self):
        r = rencanakan("Gudang Pusat", "Lembang", 5, ditutup=[("Pasteur", "Lembang")])
        self.assertEqual(r.kendaraan, "motor")
        self.assertTrue(r.ditemukan)
        self.assertIn("Dago", r.jalur)

    def test_macet_dan_hujan_menaikkan_biaya_dan_eta(self):
        lancar = rencanakan("Gudang Pusat", "Gedebage", 10)
        buruk = rencanakan("Gudang Pusat", "Gedebage", 10, cuaca="hujan", kemacetan="tinggi")
        self.assertAlmostEqual(buruk.pengali_biaya, 1.7 * 1.2)
        self.assertAlmostEqual(buruk.biaya_efektif, lancar.biaya_efektif * 1.7 * 1.2)
        self.assertGreater(buruk.eta_menit, lancar.eta_menit * 1.7 * 1.2)  # ada buffer 30%

    def test_override_algoritma_dicatat(self):
        r = rencanakan("Gudang Pusat", "Dago", 10, algoritma="bfs")
        self.assertEqual(r.algoritma, "bfs")
        self.assertTrue(any("manual" in c for c in r.catatan))

    def test_tidak_ada_rute_dilaporkan(self):
        tutup = [("Pasteur", "Lembang"), ("Dago", "Lembang")]
        r = rencanakan("Gudang Pusat", "Lembang", 500, ditutup=tutup)
        self.assertFalse(r.ditemukan)
        self.assertTrue(r.catatan)

    def test_lokasi_salah(self):
        with self.assertRaises(KeyError):
            rencanakan("Gudang Pusat", "Jakarta", 10)

    def test_cli_berhasil_dan_gagal(self):
        self.assertEqual(cli.main(["--tujuan", "Dago", "--berat", "10", "--tanpa-jejak"]), 0)
        self.assertEqual(cli.main(["--tujuan", "Jakarta", "--berat", "10"]), 2)
        self.assertEqual(cli.main(["--tujuan", "Dago", "--berat", "-3"]), 2)


if __name__ == "__main__":
    unittest.main()
