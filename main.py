catatan = []
target_harian = None  # Menyimpan target harian dalam menit
pengingat = []  # Menyimpan pengingat belajar untuk ujian

def tambah_catatan():
    print("\n--- Tambah Catatan Belajar ---")
    
    # Meminta input dari pengguna
    mapel = input("Masukkan mata pelajaran: ")
    topik = input("Masukkan topik: ")
    durasi = int(input("Masukkan durasi belajar (menit): "))
    
    # Menyimpan data ke dalam list
    # Menggunakan dictionary agar mudah dibaca
    data_belajar = {
        "mapel": mapel,
        "topik": topik,
        "durasi": durasi
    }
    
    catatan.append(data_belajar)
    print(f"✓ Catatan '{topik}' ({mapel}) berhasil disimpan!")

def lihat_catatan():
    print("\n--- Catatan Belajar ---")
    
    # Cek apakah ada data catatan
    if not catatan:
        print("Belum ada catatan belajar. Mulai dengan menambah catatan!")
        return
    
    # Tampilkan semua catatan dengan format rapi
    print(f"\n{'No':<4} {'Mapel':<15} {'Topik':<25} {'Durasi (menit)':<15}")
    print("-" * 60)
    
    for i, data in enumerate(catatan, 1):
        mapel = data["mapel"]
        topik = data["topik"]
        durasi = data["durasi"]
        print(f"{i:<4} {mapel:<15} {topik:<25} {durasi:<15}")
    
    print("-" * 60)

def total_waktu():
    print("\n--- Total Waktu Belajar ---")
    
    # Cek apakah ada data catatan
    if not catatan:
        print("Belum ada catatan belajar.")
        return
    
    # Hitung total durasi dari semua catatan
    total_durasi = 0
    for data in catatan:
        total_durasi += data["durasi"]
    
    # Konversi menit ke jam dan menit
    jam = total_durasi // 60
    menit = total_durasi % 60
    
    # Tampilkan hasil dengan format rapi
    print(f"\nTotal waktu belajar: {total_durasi} menit")
    print(f"Atau: {jam} jam {menit} menit")
    
    # Tampilkan progress target jika ada target harian
    if target_harian:
        persentase = (total_durasi / target_harian) * 100
        sisa = max(0, target_harian - total_durasi)
        
        print(f"\n📊 Target Harian: {target_harian} menit")
        print(f"Progress: {persentase:.1f}%")
        
        if total_durasi >= target_harian:
            print("🎉 Selamat! Target harian sudah tercapai!")
        else:
            print(f"⏳ Sisa: {sisa} menit lagi untuk mencapai target")
    
    print(f"\nBagus! Terus tingkatkan waktu belajarmu! 📚")

def set_target_harian():
    global target_harian
    print("\n--- Set Target Harian ---")
    
    try:
        target = int(input("Masukkan target belajar harian (menit): "))
        if target > 0:
            target_harian = target
            jam = target // 60
            menit = target % 60
            print(f"✓ Target harian {target} menit ({jam}j {menit}m) berhasil disimpan!")
        else:
            print("Target harus lebih dari 0 menit!")
    except ValueError:
        print("Input tidak valid! Masukkan angka.")

def lihat_target():
    print("\n--- Target Harian ---")
    
    if not target_harian:
        print("Belum ada target harian. Atur target terlebih dahulu!")
        return
    
    jam = target_harian // 60
    menit = target_harian % 60
    print(f"Target harian Anda: {target_harian} menit ({jam}j {menit}m)")
    
    # Tampilkan progress jika ada catatan
    if catatan:
        total_durasi = sum(data["durasi"] for data in catatan)
        persentase = (total_durasi / target_harian) * 100
        sisa = max(0, target_harian - total_durasi)
        
        print(f"\nProgress hari ini: {total_durasi} menit ({persentase:.1f}%)")
        if total_durasi >= target_harian:
            print("✨ Target sudah tercapai! Lanjutkan semangat! 🔥")
        else:
            print(f"Sisa: {sisa} menit")

def tambah_pengingat():
    print("\n--- Tambah Pengingat Belajar Ujian ---")
    
    # Meminta input dari pengguna
    mapel = input("Masukkan mata pelajaran (penting untuk ujian): ")
    materi = input("Masukkan materi/bab yang harus dipelajari: ")
    
    # Menyimpan data pengingat
    data_pengingat = {
        "mapel": mapel,
        "materi": materi,
        "status": "Belum dipelajari"
    }
    
    pengingat.append(data_pengingat)
    print(f"✓ Pengingat '{mapel}' - '{materi}' berhasil ditambahkan!")

def lihat_pengingat():
    print("\n--- Pengingat Belajar Ujian ---")
    
    # Cek apakah ada pengingat
    if not pengingat:
        print("Belum ada pengingat. Tambahkan pengingat untuk fokus belajar ujian!")
        return
    
    # Tampilkan semua pengingat dengan format rapi
    print(f"\n{'No':<4} {'Mapel':<20} {'Materi/Bab':<35} {'Status':<20}")
    print("-" * 80)
    
    for i, data in enumerate(pengingat, 1):
        mapel = data["mapel"]
        materi = data["materi"]
        status = data["status"]
        print(f"{i:<4} {mapel:<20} {materi:<35} {status:<20}")
    
    print("-" * 80)
    print("\n💡 Tips: Tandai materi yang sudah dipelajari untuk tracking progress!")

def tandai_pengingat():
    print("\n--- Tandai Materi Sudah Dipelajari ---")
    
    if not pengingat:
        print("Belum ada pengingat untuk ditandai.")
        return
    
    lihat_pengingat()
    
    try:
        nomor = int(input("\nNomor pengingat yang sudah dipelajari: "))
        if 1 <= nomor <= len(pengingat):
            pengingat[nomor - 1]["status"] = "✓ Sudah dipelajari"
            print(f"✓ '{pengingat[nomor - 1]['materi']}' ditandai sebagai sudah dipelajari!")
        else:
            print("Nomor pengingat tidak valid!")
    except ValueError:
        print("Input tidak valid! Masukkan nomor.")

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Set target harian")
    print("5. Lihat target harian")
    print("6. Tambah pengingat ujian")
    print("7. Lihat pengingat ujian")
    print("8. Tandai materi sudah dipelajari")
    print("9. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "4":
        set_target_harian()
    elif pilihan == "5":
        lihat_target()
    elif pilihan == "6":
        tambah_pengingat()
    elif pilihan == "7":
        lihat_pengingat()
    elif pilihan == "8":
        tandai_pengingat()
    elif pilihan == "9":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")