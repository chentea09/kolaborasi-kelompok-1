# hitung_total.py

def hitung_total(daftar_barang):
    total = 0

    for barang in daftar_barang:
        total += barang["harga"]

    return total


def barang_termahal(daftar_barang):
    mahal = daftar_barang[0]

    for barang in daftar_barang:
        if barang["harga"] > mahal["harga"]:
            mahal = barang

    return mahal
