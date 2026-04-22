# main.py

from input_barang import input_pembeli, input_barang
from hitung_total import hitung_total, barang_termahal

# Input data
nama_pembeli = input_pembeli()
barang = input_barang()

# Proses
total = hitung_total(barang)
mahal = barang_termahal(barang)

# Output Struk Rapi
print("\n=================================")
print("         STRUK BELANJA")
print("=================================")
print(f"Nama Pembeli : {nama_pembeli}")
print("---------------------------------")

for item in barang:
    print(f"{item['nama']:<15} Rp{item['harga']:>8}")

print("---------------------------------")
print(f"{'TOTAL':<15} Rp{total:>8}")
print("---------------------------------")
print("Barang Termahal :")
print(f"{mahal['nama']} - Rp{mahal['harga']}")
print("=================================")
print("Terima kasih sudah belanja!")
