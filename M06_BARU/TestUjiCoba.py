def pesan_tiket():
    print("🎬 Selamat datang di Bioskop Bandaru 🎬")

    # Input usia pengguna
    usia = int(input("Masukkan usia Anda: "))

    # Pilihan film
    print("\nPilih jenis film:")
    print("1. Animasi (Semua Umur)")
    print("2. Aksi (13+)")
    print("3. Horor (17+)")
    pilihan_film = int(input("Masukkan nomor pilihan (1-3): "))

    # Validasi usia dan jenis film
    if pilihan_film == 1:
        film = "Animasi"
    elif pilihan_film == 2 and usia >= 13:
        film = "Aksi"
    elif pilihan_film == 3 and usia >= 17:
        film = "Horor"
    else:
        print("❌ Maaf, usia Anda tidak memenuhi syarat untuk menonton film ini.")
        return

    # Input jumlah tiket
    jumlah_tiket = int(input("\nMasukkan jumlah tiket yang ingin dibeli: "))

    # Harga tiket berdasarkan jenis film
    harga_tiket = 0
    if film == "Animasi":
        harga_tiket = 25000
    elif film == "Aksi":
        harga_tiket = 35000
    elif film == "Horor":
        harga_tiket = 40000

    # Diskon jika membeli lebih dari 3 tiket
    total_harga = harga_tiket * jumlah_tiket
    if jumlah_tiket > 3:
        total_harga *= 0.9  # Diskon 10%

    # Cetak tiket dengan loop
    print("\n🎟️ Tiket Anda 🎟️")
    for i in range(jumlah_tiket):
        print(f"Tiket {i + 1}: {film} - Rp {harga_tiket}")

    print(f"\nTotal Harga: Rp {int(total_harga)}")
    print("✅ Terima kasih telah membeli tiket di Bioskop Bandaru!")


# Jalankan program
pesan_tiket()
