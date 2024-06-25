from tabulate import tabulate

# Data Barang
barang = [
    {
        'item code': "CD01",
        'jenis': "CD",
        'Artist': "Raisa",
        'Album': "Handmade",
        'Genre': "POP",
        'Tahun Rilis': 2016,
        'jumlah': 50,
        'harga': 150000.00,
    },
    {
        'item code': "CD02",
        'jenis': "CD",
        'Artist': "Taylor Swift",
        'Album': "The Tortured Poets Department",
        'Genre': "POP",
        'Tahun Rilis': 2024,
        'jumlah': 50,
        'harga': 200000.00,
    },
    {
        'item code': "CD03",
        'jenis': "CD",
        'Artist': "Tulus",
        'Album': "Manusia",
        'Genre': "POP",
        'Tahun Rilis': 2022,
        'jumlah': 50,
        'harga': 130000.00,
    },
    {
        'item code': "VN04",
        'jenis': "Vinyl",
        'Artist': "Raisa",
        'Album': "Nyaman Tak Cukup - Single",
        'Genre': "POP",
        'Tahun Rilis': 2023,
        'jumlah': 10,
        'harga': 170000.00,
    },
    {
        'item code': "KA05",
        'jenis': "Kaset",
        'Artist': "MALIQ & D'Essentials",
        'Album': "Can Machines Fall In Love?",
        'Genre': "R&B/Soul",
        'Tahun Rilis': 2024,
        'jumlah': 10,
        'harga': 160000.00,
    },
    {
        'item code': "VN06",
        'jenis': "Vinyl",
        'Artist': "Taylor Swift",
        'Album': "Midnights (The Til Dawn Edition)",
        'Genre': "Pop",
        'Tahun Rilis': 2022,
        'jumlah': 20,
        'harga': 500000.00,
    },
    {
        'item code': "KA07",
        'jenis': "Kaset",
        'Artist': "Michael Jackson",
        'Album': "Bad",
        'Genre': "POP",
        'Tahun Rilis': 1987,
        'jumlah': 3,
        'harga': 500000.00,
    }
]


# Fungsi untuk menampilkan menu utama
def tampilkan_menu():
    print("\nMenu Utama:")
    print("1. Tampilkan Data Barang")
    print("2. Tambah Barang")
    print("3. Update Barang")
    print("4. Hapus Barang")
    print("5. Transaksi Penjualan")
    print("6. Keluar")

# Fungsi untuk menampilkan menu tambah data
def tampilkan_menu_create():
    print("\nMenu Tambah Data:")
    print("1. Tambah Data Barang")
    print("2. Kembali ke Menu Utama")

# Fungsi untuk menambahkan barang baru
def tambah_barang():
    while True:
        tampilkan_menu_create()
        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            while True:
                item_code = input("Masukkan Item Code (4 karakter): ").strip().upper()

                # Validasi panjang karakter
                if len(item_code) != 4:
                    print("Item Code harus 4 karakter.")
                    continue

                # Validasi keunikan item_code
                if any(b['item code'] == item_code for b in barang):
                    print("Item Code sudah ada.")
                    continue

                jenis_valid = False
                while not jenis_valid:
                    jenis = input("Masukkan Jenis Barang (Kaset/CD/Vinyl): ").strip().lower()
                    if jenis in ['kaset', 'cd', 'vinyl']:
                        jenis_valid = True
                    else:
                        print("Jenis barang tidak valid. Silakan masukkan Kaset, CD, atau Vinyl.")

                # Ubah jenis barang ke format yang konsisten
                if jenis == 'kaset':
                    jenis = 'Kaset'
                elif jenis == 'cd':
                    jenis = 'CD'
                elif jenis == 'vinyl':
                    jenis = 'Vinyl'

                artist = input("Masukkan Nama Artist: ").strip().title()  # Capitalize nama artist
                album = input("Masukkan Nama Album: ").strip().title()    # Capitalize nama album
                genre = input("Masukkan Genre: ").strip().upper()         # Capitalize genre

                tahun_rilis_valid = False
                while not tahun_rilis_valid:
                    tahun_rilis = input("Masukkan Tahun Rilis: ").strip()
                    if tahun_rilis.isdigit():
                        tahun_rilis = int(tahun_rilis)
                        if 1980 <= tahun_rilis <= 2024:
                            tahun_rilis_valid = True
                        else:
                            print("Masukkan tahun rilis antara 1980 - 2024.")
                    else:
                        print("Masukkan tahun rilis antara 1980 - 2024.")

                while True:
                    jumlah = input("Masukkan Jumlah Barang: ").strip()
                    if jumlah.isdigit():
                        jumlah = int(jumlah)
                        if jumlah >= 1:
                            break
                        else:
                            print("Jumlah harus minimal 1.")
                    else:
                        print("Input tidak valid. Masukkan angka yang benar.")

                while True:
                    harga = input("Masukkan Harga Barang: ").strip()
                    try:
                        harga = float(harga)
                        if harga >= 0:
                            break
                        else:
                            print("Harga tidak boleh negatif.")
                    except ValueError:
                        print("Input tidak valid. Masukkan angka yang benar.")

                

                print("\nData Barang:")
                print(f"Item Code: {item_code}")
                print(f"Jenis: {jenis}")
                print(f"Artist: {artist}")
                print(f"Album: {album}")
                print(f"Genre: {genre}")
                print(f"Tahun Rilis: {tahun_rilis}")
                print(f"Jumlah: {jumlah}")
                print(f"Harga: {harga}")

                simpan = input("Simpan data ini? (y/n): ")
                if simpan.lower() == 'y':
                    barang.append({
                        'item code': item_code,
                        'jenis': jenis,
                        'Artist': artist,
                        'Album': album,
                        'Genre': genre,
                        'Tahun Rilis': tahun_rilis,
                        'jumlah': jumlah,
                        'harga': harga
                    })
                    print("Barang berhasil ditambahkan.")
                else:
                    print("Data tidak disimpan.")

                break

        elif pilihan == '2':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Fungsi untuk menampilkan menu data barang
def tampilkan_menu_read():
    print("\nMenu Tampilkan Data:")
    print("1. Tampilkan Semua Data")
    print("2. Cari Barang Berdasarkan ID")
    print("3. Cari Barang Berdasarkan Nama")
    print("4. Kembali ke Menu Utama")

# Fungsi untuk menampilkan semua barang
def tampilkan_semua_barang():
    if not barang:
        print("Data tidak ada.")
        return
    
    headers = ["Item Code", "Jenis", "Artist", "Album", "Genre", "Tahun Rilis", "Jumlah", "Harga"]
    rows = []
    for b in barang:
        rows.append([
            b['item code'],
            b['jenis'],
            b['Artist'],
            b['Album'],
            b['Genre'],
            b['Tahun Rilis'],
            b['jumlah'],
            f"Rp {b['harga']:.1f}"
        ])
    
    print("\nTabel Daftar Barang:")
    print(tabulate(rows, headers=headers, tablefmt="grid"))

# Fungsi untuk mencari barang berdasarkan ID
def cari_barang_berdasarkan_id():
    while True:
        item_code = input("Masukkan Item Code yang dicari (4 karakter alphanumeric): ").strip().upper()

        # Validasi panjang karakter dan alphanumeric
        if len(item_code) != 4 or not item_code.isalnum():
            print("Item Code harus terdiri dari 4 karakter alphanumeric.")
            opsi = input("Masukkan 'c' untuk mencoba lagi atau 'k' untuk kembali: ").lower()
            while opsi not in ['c', 'k']:
                opsi = input("Pilihan tidak valid. Silakan masukkan 'c' untuk mencoba lagi atau 'k' untuk kembali: ").lower()
            
            if opsi == 'c':
                continue
            elif opsi == 'k':
                return

        found = False
        for b in barang:
            if b['item code'] == item_code:
                print(f"Item Code: {b['item code']}, Jenis: {b['jenis']}, Artist: {b['Artist']}, Album: {b['Album']}, Genre: {b['Genre']}, Tahun Rilis: {b['Tahun Rilis']}, Jumlah: {b['jumlah']}, Harga: Rp {b['harga']}")
                found = True
                break
        
        if not found:
            print("Barang tidak ditemukan.")

        opsi = input("Masukkan 'c' untuk mencoba lagi atau 'k' untuk kembali: ").lower()
        while opsi not in ['c', 'k']:
            opsi = input("Pilihan tidak valid. Silakan masukkan 'c' untuk mencoba lagi atau 'k' untuk kembali: ").lower()
        
        if opsi == 'k':
            return
        
# Fungsi untuk mencari barang berdasarkan nama
def cari_barang_berdasarkan_nama():
    while True:
        artist = input("Masukkan Nama Artist yang dicari: ").strip().lower()  # Ubah input ke huruf kecil dan hilangkan whitespace

        found = False
        for b in barang:
            if artist in b['Artist'].lower():  # Cek jika artist yang dicari ada dalam nama artist barang (case-insensitive)
                print(f"Item Code: {b['item code']}, Jenis: {b['jenis']}, Artist: {b['Artist']}, Album: {b['Album']}, Genre: {b['Genre']}, Tahun Rilis: {b['Tahun Rilis']}, Jumlah: {b['jumlah']}, Harga: {b['harga']}")
                found = True

        if not found:
            print("Barang tidak ditemukan.")

        opsi = input("Masukkan 'c' untuk mencoba lagi atau 'k' untuk kembali: ").lower()
        while opsi not in ['c', 'k']:
            opsi = input("Pilihan tidak valid. Silakan masukkan 'c' untuk mencoba lagi atau 'k' untuk kembali: ").lower()
        
        if opsi == 'k':
            return
        
# Fungsi untuk menampilkan data barang
def tampilkan_data_barang():
    while True:
        tampilkan_menu_read()
        pilihan = input("Pilih opsi: ").upper()  # Ubah ke huruf besar
        
        if pilihan == '1':
            tampilkan_semua_barang()
        elif pilihan == '2':
            cari_barang_berdasarkan_id()
        elif pilihan == '3':
            cari_barang_berdasarkan_nama()
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


# Fungsi untuk menampilkan menu update
def tampilkan_menu_update():
    print("Menu Update Barang:")
    print("1. Update Item Code")
    print("2. Update Jenis")
    print("3. Update Artist")
    print("4. Update Album")
    print("5. Update Genre")
    print("6. Update Tahun Rilis")
    print("7. Update Jumlah")
    print("8. Update Harga")
    print("9. Kembali ke Menu Sebelumnya")

# Fungsi untuk mengupdate data barang
def update_barang():
    while True:
        tampilkan_menu_update()
        pilihan = input("Pilih opsi: ")

        if pilihan == '9':
            print("Kembali ke menu sebelumnya...")
            break
        elif pilihan in ['1', '2', '3', '4', '5', '6', '7', '8']:
            kolom = ''
            if pilihan == '1':
                kolom = 'item code'
            elif pilihan == '2':
                kolom = 'jenis'
            elif pilihan == '3':
                kolom = 'Artist'
            elif pilihan == '4':
                kolom = 'Album'
            elif pilihan == '5':
                kolom = 'Genre'
            elif pilihan == '6':
                kolom = 'Tahun Rilis'
            elif pilihan == '7':
                kolom = 'jumlah'
            elif pilihan == '8':
                kolom = 'harga'

            while True:
                item_code = input("Masukkan Item Code yang ingin diupdate: ").strip().upper()
                barang_ditemukan = False
                for b in barang:
                    if b['item code'] == item_code:
                        barang_ditemukan = True
                        break
                
                if not barang_ditemukan:
                    print("Barang tidak ditemukan.")
                    continue
                
                if kolom == 'item code':
                    while True:
                        nilai_baru = input(f"Masukkan {kolom} baru (4 karakter alphanumeric): ").strip().upper()
                        if len(nilai_baru) != 4 or not nilai_baru.isalnum():
                            print("Item Code harus terdiri dari 4 karakter alphanumeric.")
                        elif any(brg['item code'] == nilai_baru for brg in barang):
                            print("Item Code sudah ada. Silakan masukkan Item Code yang berbeda.")
                        else:
                            break
                elif kolom == 'jenis':
                    while True:
                        print("Pilih jenis baru:")
                        print("1. Kaset")
                        print("2. CD")
                        print("3. Vinyl")
                        jenis_baru = input("Masukkan pilihan (1/2/3): ").strip()
                        if jenis_baru == '1':
                            nilai_baru = 'Kaset'
                        elif jenis_baru == '2':
                            nilai_baru = 'CD'
                        elif jenis_baru == '3':
                            nilai_baru = 'Vinyl'
                        else:
                            print("Pilihan tidak valid. Silakan coba lagi.")
                            continue
                        if nilai_baru == b['jenis']:
                            print("Jenis baru sama dengan yang lama. Silakan masukkan jenis yang berbeda.")
                            continue
                        break
                elif kolom == 'Artist':
                    while True:
                        nilai_baru = input(f"Masukkan {kolom} baru: ").strip().title()
                        if nilai_baru.lower() == b['Artist'].lower():
                            print("Nama artist baru sama dengan yang lama. Silakan masukkan nama yang berbeda.")
                        else:
                            break
                elif kolom == 'Album':
                    while True:
                        nilai_baru = input(f"Masukkan {kolom} baru: ").strip().title()
                        if nilai_baru.lower() == b['Album'].lower():
                            print("Nama album baru sama dengan yang lama. Silakan masukkan nama yang berbeda.")
                        else:
                            break
                elif kolom == 'Genre':
                    while True:
                        nilai_baru = input(f"Masukkan {kolom} baru: ").strip().upper()
                        if nilai_baru.lower() == b['Genre'].lower():
                            print("Nama genre baru sama dengan yang lama. Silakan masukkan nama yang berbeda.")
                        else:
                            break
                elif kolom == 'Tahun Rilis':
                    while True:
                        try:
                            nilai_baru = int(input(f"Masukkan {kolom} baru (1980-2024): "))
                            if nilai_baru < 1980 or nilai_baru > 2024:
                                print("Tahun Rilis harus antara 1980 dan 2024.")
                            else:
                                break
                        except ValueError:
                            print("Tahun Rilis harus berupa angka.")
                elif kolom == 'jumlah':
                    while True:
                        try:
                            nilai_baru = int(input(f"Masukkan {kolom} baru (lebih dari 0): "))
                            if nilai_baru <= 0:
                                print("Jumlah harus lebih dari 0.")
                            else:
                                break
                        except ValueError:
                            print("Jumlah harus berupa angka.")
                elif kolom == 'harga':
                    while True:
                        try:
                            nilai_baru = float(input(f"Masukkan {kolom} baru (lebih dari 0): "))
                            if nilai_baru <= 0:
                                print("Harga harus lebih dari 0.")
                            else:
                                break
                        except ValueError:
                            print("Harga harus berupa angka.")

                konfirmasi = input(f"Apakah Anda yakin ingin mengubah {kolom} {b[kolom]} menjadi {nilai_baru}? (y/n): ").strip().lower()
                if konfirmasi == 'y':
                    print(f"{kolom.capitalize()} berhasil diupdate: {b[kolom]} -> {nilai_baru}")
                    b[kolom] = nilai_baru
                else:
                    print(f"{kolom.capitalize()} tidak jadi diupdate.")
                break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Fungsi untuk menampilkan menu hapus
def tampilkan_menu_delete():
    print("Menu Hapus Barang:")
    print("1. Hapus Barang")
    print("2. Kembali ke Menu Sebelumnya")

# Fungsi untuk menghapus barang
def hapus_barang():
    while True:
        tampilkan_menu_delete()
        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            if not barang:
                print("Tidak ada barang yang tersedia untuk dihapus.")
                input("Tekan Enter untuk kembali ke menu sebelumnya...")
                break

            while True:
                item_code = input("Masukkan Item Code yang ingin dihapus: ").strip().upper()
                barang_ditemukan = False

                for b in barang:
                    if b['item code'] == item_code:
                        barang_ditemukan = True
                        print(f"Data yang akan dihapus:")
                        print(f"Item Code: {b['item code']}, Jenis: {b['jenis']}, Artist: {b['Artist']}, Album: {b['Album']}, Genre: {b['Genre']}, Tahun Rilis: {b['Tahun Rilis']}, Jumlah: {b['jumlah']}, Harga: Rp {b['harga']:.2f}")
                        konfirmasi = input("Apakah Anda yakin ingin menghapus barang ini? (y/n): ").strip().lower()
                        if konfirmasi == 'y':
                            barang.remove(b)
                            print("Barang berhasil dihapus.")
                        else:
                            print("Penghapusan dibatalkan.")
                        break
                
                if not barang_ditemukan:
                    print("Barang tidak ditemukan. Silakan masukkan Item Code yang benar.")
                    
                    if not barang:  # Check if list is now empty after deletion
                        print("Tidak ada barang yang tersedia untuk dihapus.")
                        input("Tekan Enter untuk kembali ke menu sebelumnya...")
                        break
                    continue
                
                break

        elif pilihan == '2':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


# Fungsi untuk menampilkan menu transaksi
def tampilkan_menu_transaksi():
    print("Menu Transaksi Penjualan:")
    print("1. Tambah Transaksi")
    print("2. Kembali ke Menu Utama")

# Fungsi untuk melakukan transaksi
def transaksi_penjualan():
    while True:
        tampilkan_menu_transaksi()
        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            while True:  # Loop untuk memastikan input item code yang valid
                item_code = input("Masukkan Item Code yang dijual: ").strip().upper()  # Konversi ke huruf kapital
                
                barang_ditemukan = False
                for b in barang:
                    if b['item code'].upper() == item_code:
                        try:
                            jumlah_jual = int(input("Masukkan Jumlah yang dijual: "))
                            if jumlah_jual <= 0:
                                print("Jumlah yang dijual harus lebih dari 0.")
                                continue
                            elif jumlah_jual > b['jumlah']:
                                print("Stok tidak mencukupi.")
                                continue
                            
                            # Menampilkan detail transaksi
                            print(f"Item Code: {b['item code']}, Jenis: {b['jenis']}, Artist: {b['Artist']}, Album: {b['Album']}, Genre: {b['Genre']}, Tahun Rilis: {b['Tahun Rilis']}, Jumlah: {b['jumlah']}, Harga: Rp {b['harga']}")
                            print(f"Jumlah yang akan dijual: {jumlah_jual}")
                            total_harga = jumlah_jual * b['harga']
                            print(f"Total harga: Rp {total_harga:.2f}")

                            # Konfirmasi transaksi
                            konfirmasi = input("Apakah Anda yakin akan memproses ransaksi barang ini? (y/n): ").strip().lower()
                            if konfirmasi == 'y':
                                b['jumlah'] -= jumlah_jual
                                print("Transaksi berhasil.")
                                print(f"Stok barang tersisa: {b['jumlah']}")
                            else:
                                print("Transaksi dibatalkan.")
                            
                            barang_ditemukan = True
                            break
                        except ValueError:
                            print("Jumlah harus berupa angka.")
                
                if barang_ditemukan:
                    break  # Keluar dari loop input item code jika barang ditemukan
                else:
                    print("Barang tidak ditemukan. Silakan coba lagi.")

        elif pilihan == '2':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")



# Main program loop
def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            tampilkan_data_barang()
        elif pilihan == '2':
            tambah_barang()
        elif pilihan == '3':
            update_barang()
        elif pilihan == '4':
            hapus_barang()
        elif pilihan == '5':
            transaksi_penjualan()
        elif pilihan == '6':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()


