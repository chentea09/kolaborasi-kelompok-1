# input_buku.py

def input_petugas():
    nama = input("Masukkan nama petugas: ")
    return nama


def input_buku():
    daftar_buku = []

    for i in range(1, 4):
        print(f"\nData Buku ke-{i}")
        judul = input("Judul buku      : ")

        while True:
            try:
                halaman = int(input("Jumlah halaman : "))
                break
            except ValueError:
                print("Jumlah halaman harus berupa angka!")

        daftar_buku.append({
            "judul": judul,
            "halaman": halaman
        })

    return daftar_buku
