import os
import time
from datetime import datetime as dti

# Penggunaan Waktu
x = dti.now()

# Penggunaan Variabel
kasir = "Bayu"
total = []
nm_minuman, nm_makanan = "-", "-"
hrg_minuman, hrg_makanan = 0, 0
jlh_minuman, jlh_makanan = 0, 0

# Proses pembersihan screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Proses Dialog Kasir
print(f"{kasir}: Halo, selamat datang silahkan dipilih menu nya!!")
time.sleep(2)
clear_screen()

print("""
≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
Bayu Coffe
List Menu Minuman & Makanan
≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
》Minuman
1. Cappuccino  : Rp 15.000
2. Espresso    : Rp 20.000 
3. Latte       : Rp 25.000
4. Americano   : Rp 30.000 
5. Mocha       : Rp 35.000

》Makanan
1. Sandwich    : Rp 9.000        
2. Mie Ayam    : Rp 10.000
3. Croissant   : Rp 18.000
4. Nasi Goreng : Rp 15.000
5. Quiche      : Rp 20.000

~~~~~~~~~~ ☆☆☆☆☆ ~~~~~~~~~~
""")

# Proses input minuman
minuman = int(input("Masukkan list angka menu minuman: "))
jlh_minuman = int(input("Masukkan jumlah pesanan: "))

if minuman == 1:
    nm_minuman = "Cappuccino"
    hrg_minuman = 15000 * jlh_minuman
elif minuman == 2:
    nm_minuman = "Espresso"
    hrg_minuman = 20000 * jlh_minuman
elif minuman == 3:
    nm_minuman = "Latte"
    hrg_minuman = 25000 * jlh_minuman
elif minuman == 4:
    nm_minuman = "Americano"
    hrg_minuman = 30000 * jlh_minuman
elif minuman == 5:
    nm_minuman = "Mocha"
    hrg_minuman = 35000 * jlh_minuman
else:
    print("Input tidak valid")
    exit()

total.append(hrg_minuman)

# Proses input makanan
pertanyaan = input(f"{kasir}: Anda ingin memesan makanan? (y/n): ").lower()

if pertanyaan == "y":
    makanan = int(input("Masukkan list angka menu makanan: "))
    jlh_makanan = int(input("Masukkan jumlah pesanan: "))
    time.sleep(2)
    clear_screen()
    
    if makanan == 1:
        nm_makanan = "Sandwich"
        hrg_makanan = 9000 * jlh_makanan
    elif makanan == 2:
        nm_makanan = "Mie Ayam"
        hrg_makanan = 10000 * jlh_makanan
    elif makanan == 3:
        nm_makanan = "Croissant"
        hrg_makanan = 18000 * jlh_makanan
    elif makanan == 4:
        nm_makanan = "Nasi Goreng"
        hrg_makanan = 15000 * jlh_makanan
    elif makanan == 5:
        nm_makanan = "Quiche"
        hrg_makanan = 20000 * jlh_makanan
    else:
        print("Input tidak valid")
        exit()

    total.append(hrg_makanan)

if pertanyaan == "n":
  print(f"{kasir}: Terimakasi telah memesan, ini struk anda!!")
  time.sleep(2)
  clear_screen()

# Struk
print(f"""
≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
Bayu Coffe
Tanggal: {x.day}/{x.month}/{x.year}
≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
Minuman: {nm_minuman} x{jlh_minuman} Rp {hrg_minuman}
Makanan: {nm_makanan} x{jlh_makanan} Rp {hrg_makanan}
≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
Total: Rp {sum(total)}
jangan lupa mampir lagi ya.. :)
""")