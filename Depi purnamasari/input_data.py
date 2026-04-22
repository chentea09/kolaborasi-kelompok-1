# input_barang.py

def input_pembeli():
    nama = input("Masukkan nama pembeli: ")
    return nama


def input_barang():
    daftar_barang = []

    for i in range(1, 4):
        print(f"\nBarang ke-{i}")
        nama = input("Nama barang : ")

        while True:
            try:
                harga = int(input("Harga barang: Rp"))
                break
            except ValueError:
                print("Harga harus berupa angka!")

        daftar_barang.append({
            "nama": nama,
            "harga": harga
        })

    return daftar_barang
