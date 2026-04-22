# main.py

from input_buku import input_petugas, input_buku
from proses_buku import total_halaman, buku_terbanyak, rata_rata_halaman

# Input data
petugas = input_petugas()
buku = input_buku()

# Proses data
total = total_halaman(buku)
terbanyak = buku_terbanyak(buku)
rata = rata_rata_halaman(buku)

# Output hasil
print("\n===================================")
print("      DATA BUKU PERPUSTAKAAN")
print("===================================")
print(f"Nama Petugas : {petugas}")
print("-----------------------------------")
print(f"{'Judul Buku':<20} {'Halaman':>10}")
print("-----------------------------------")

for item in buku:
    print(f"{item['judul']:<20} {item['halaman']:>10}")

print("-----------------------------------")
print(f"{'Total Halaman':<20} {total:>10}")
print(f"{'Rata-rata':<20} {rata:>10.2f}")
print("-----------------------------------")
print("Buku Halaman Terbanyak:")
print(f"{terbanyak['judul']} ({terbanyak['halaman']} halaman)")
print("===================================")
print("Data berhasil diproses!")
