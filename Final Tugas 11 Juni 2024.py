# Program 1
mahasiswa_list = []

def input_data_mahasiswa():
    n = int(input("Masukkan jumlah mahasiswa: "))
    for i in range(n):
        print(f"Masukkan data mahasiswa ke-{i+1}:")
        nama = input("Nama: ")
        nim = input("NIM: ")
        prodi = input("Prodi: ")
        nilai = float(input("Nilai: "))
        mahasiswa = {"Nama": nama, "NIM": nim, "Prodi": prodi, "Nilai": nilai}
        mahasiswa_list.append(mahasiswa)

def tampilkan_data_mahasiswa(mahasiswa_list):
    for i, mahasiswa in enumerate(mahasiswa_list):
        print(f"Mahasiswa ke-{i+1}:")
        print(f"Nama: {mahasiswa['Nama']}")
        print(f"NIM: {mahasiswa['NIM']}")
        print(f"Prodi: {mahasiswa['Prodi']}")
        print(f"Nilai: {mahasiswa['Nilai']}")

def rata_rata_nilai(mahasiswa_list):
    total_nilai = sum(mhs['Nilai'] for mhs in mahasiswa_list)
    rata_rata = total_nilai / len(mahasiswa_list)
    print(f"Rata-rata nilai mahasiswa adalah: {rata_rata:.2f}")

def nilai_tertinggi_terendah(mahasiswa_list):
    nilai_tertinggi = max(mahasiswa_list, key=lambda x: x['Nilai'])
    nilai_terendah = min(mahasiswa_list, key=lambda x: x['Nilai'])
    print(f"Mahasiswa dengan nilai tertinggi:")
    print(f"Nama: {nilai_tertinggi['Nama']}")
    print(f"NIM: {nilai_tertinggi['NIM']}")
    print(f"Prodi: {nilai_tertinggi['Prodi']}")
    print(f"Nilai: {nilai_tertinggi['Nilai']}\n")
    print(f"Mahasiswa dengan nilai terendah:")
    print(f"Nama: {nilai_terendah['Nama']}")
    print(f"NIM: {nilai_terendah['NIM']}")
    print(f"Prodi: {nilai_terendah['Prodi']}")
    print(f"Nilai: {nilai_terendah['Nilai']}")

def menu_mahasiswa():
    while True:
        print("\nMenu Data Mahasiswa:")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Data Mahasiswa")
        print("3. Rata-rata Nilai Mahasiswa")
        print("4. Nilai Tertinggi dan Terendah")
        print("5. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            input_data_mahasiswa()
        elif pilihan == '2':
            tampilkan_data_mahasiswa(mahasiswa_list)
        elif pilihan == '3':
            rata_rata_nilai(mahasiswa_list)
        elif pilihan == '4':
            nilai_tertinggi_terendah(mahasiswa_list)
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Program 2
inventaris = []

def input_barang():
    nama = input("Masukkan nama barang: ")
    kode = input("Masukkan kode barang: ")
    jumlah = int(input("Masukkan jumlah barang: "))
    inventaris.append({'nama': nama, 'kode': kode, 'jumlah': jumlah})
    print(f"Barang dengan kode {kode} berhasil ditambahkan.\n")

def tampilkan_semua_barang():
    if not inventaris:
        print("Tidak ada barang dalam inventaris.\n")
    else:
        for barang in inventaris:
            print(f"Nama: {barang['nama']}, Kode: {barang['kode']}, Jumlah: {barang['jumlah']}")
        print()

def cari_barang_berdasarkan_kode(kode):
    for barang in inventaris:
        if barang['kode'] == kode:
            return barang
    return None

def hapus_barang_berdasarkan_kode(kode):
    for barang in inventaris:
        if barang['kode'] == kode:
            inventaris.remove(barang)
            print(f"Barang dengan kode {kode} berhasil dihapus.\n")
            return
    print(f"Barang dengan kode {kode} tidak ditemukan.\n")

def menu_inventaris():
    while True:
        print("\nMenu Inventaris Barang:")
        print("1. Tambah Barang")
        print("2. Tampilkan Semua Barang")
        print("3. Cari Barang Berdasarkan Kode")
        print("4. Hapus Barang Berdasarkan Kode")
        print("5. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            input_barang()
        elif pilihan == '2':
            tampilkan_semua_barang()
        elif pilihan == '3':
            kode = input("Masukkan kode barang yang dicari: ")
            barang = cari_barang_berdasarkan_kode(kode)
            if barang:
                print(f"Barang ditemukan: Nama: {barang['nama']}, Kode: {barang['kode']}, Jumlah: {barang['jumlah']}\n")
            else:
                print(f"Barang dengan kode {kode} tidak ditemukan.\n")
        elif pilihan == '4':
            kode = input("Masukkan kode barang yang ingin dihapus: ")
            hapus_barang_berdasarkan_kode(kode)
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.\n")

# Program 3
transaksi = []

def masukkan_transaksi():
    jenis = input("Masukkan jenis transaksi (pemasukan/pengeluaran): ")
    nominal = float(input("Masukkan nominal transaksi: "))
    transaksi.append((jenis, nominal))
    print("Transaksi berhasil ditambahkan!\n")

def tampilkan_semua_transaksi(transaksi):
    if not transaksi:
        print("Tidak ada transaksi.")
    else:
        for idx, (jenis, nominal) in enumerate(transaksi, start=1):
            print(f"Transaksi {idx}:")
            print(f"Jenis: {jenis}")
            print(f"Nominal: {nominal}\n")

def total_pemasukan(transaksi):
    total = sum(nominal for jenis, nominal in transaksi if jenis == 'pemasukan')
    print(f"Total pemasukan: {total}\n")

def total_pengeluaran(transaksi):
    total = sum(nominal for jenis, nominal in transaksi if jenis == 'pengeluaran')
    print(f"Total pengeluaran: {total}\n")

def saldo_akhir(transaksi):
    pemasukan = sum(nominal for jenis, nominal in transaksi if jenis == 'pemasukan')
    pengeluaran = sum(nominal for jenis, nominal in transaksi if jenis == 'pengeluaran')
    saldo = pemasukan - pengeluaran
    print(f"Saldo akhir: {saldo}\n")

def menu_keuangan():
    while True:
        print("\nMenu Keuangan Pribadi:")
        print("1. Masukkan Transaksi")
        print("2. Tampilkan Semua Transaksi")
        print("3. Total Pemasukan")
        print("4. Total Pengeluaran")
        print("5. Saldo Akhir")
        print("6. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            masukkan_transaksi()
        elif pilihan == '2':
            tampilkan_semua_transaksi(transaksi)
        elif pilihan == '3':
            total_pemasukan(transaksi)
        elif pilihan == '4':
            total_pengeluaran(transaksi)
        elif pilihan == '5':
            saldo_akhir(transaksi)
        elif pilihan == '6':
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.\n")

# Menu Utama
def menu_utama():
    while True:
        print("\nMenu Utama:")
        print("1. Data Mahasiswa")
        print("2. Inventaris Barang")
        print("3. Keuangan Pribadi")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            menu_mahasiswa()
        elif pilihan == '2':
            menu_inventaris()
        elif pilihan == '3':
            menu_keuangan()
        elif pilihan == '4':
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Menjalankan menu utama
menu_utama()

