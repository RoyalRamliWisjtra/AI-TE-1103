# Sistem Pakar Rekomendasi Pengiriman Barang (rule-based, forward chaining)

# Setiap aturan: (nama, kondisi, kesimpulan)
aturan = [
    ("R1", lambda f: f["dingin"],
     "Kendaraan: mobil berpendingin"),
    ("R2", lambda f: not f["dingin"] and f["berat"] > 50,
     "Kendaraan: truk"),
    ("R3", lambda f: not f["dingin"] and 10 < f["berat"] <= 50,
     "Kendaraan: mobil boks"),
    ("R4", lambda f: not f["dingin"] and f["berat"] <= 10 and f["jarak"] <= 15,
     "Kendaraan: motor"),
    ("R5", lambda f: not f["dingin"] and f["berat"] <= 10 and f["jarak"] > 15,
     "Kendaraan: mobil kecil"),
    ("R6", lambda f: f["mudah_pecah"],
     "Tambahan: gunakan bubble wrap dan kardus berlapis"),
    ("R7", lambda f: f["mendesak"],
     "Layanan: ekspres (sampai hari yang sama)"),
    ("R8", lambda f: not f["mendesak"],
     "Layanan: reguler (1-3 hari)"),
]


def tanya_ya_tidak(pertanyaan):
    return input(pertanyaan + " (y/n): ").strip().lower() == "y"


def inferensi(fakta):
    hasil = []
    for nama, kondisi, kesimpulan in aturan:
        if kondisi(fakta):
            hasil.append((nama, kesimpulan))
    return hasil


if __name__ == "__main__":
    print("=== Sistem Pakar Rekomendasi Pengiriman ===")
    fakta = {
        "berat": float(input("Berat barang (kg): ")),
        "jarak": float(input("Jarak pengiriman (km): ")),
        "dingin": tanya_ya_tidak("Perlu suhu dingin?"),
        "mudah_pecah": tanya_ya_tidak("Barang mudah pecah?"),
        "mendesak": tanya_ya_tidak("Pengiriman mendesak?"),
    }

    print("\nHasil rekomendasi:")
    for nama, kesimpulan in inferensi(fakta):
        print(f"- [{nama}] {kesimpulan}")
