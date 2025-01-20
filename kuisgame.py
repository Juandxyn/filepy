import os 
import time 
import pyfiglet

# Sistem bersih program
def clear_screen():
  os.system("cls" if os.name == "nt" else "clear")

# Membuat teks besar
teks = pyfiglet.figlet_format("Game Kuis")
print(teks)
print("≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")
print("\tStart Game")
print("\tExit")
print("≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")
print("S(mulai), E(keluar)")
jawab = str(input("pilih untuk melanjutkan (S/E): ")).lower()

def exit():
  if jawab == "e":
      time.sleep(1)
      clear_screen()
      print("Program berakhir, sampai jumpa :)")

# Soal kuis
soal_kuis = [
    {
        "pertanyaan": "Siapa penemu lampu pijar?",
        "pilihan": ["A. Thomas Alva Edison", "B. Nikola Tesla", "C. Alexander Graham Bell", "D. Albert Einstein"],
        "jawaban": "A"
    },
    {
        "pertanyaan": "Berapa hasil dari 7 x 8?",
        "pilihan": ["A. 48", "B. 54", "C. 56", "D. 63"],
        "jawaban": "C"
    },
    {
        "pertanyaan": "Ibukota Indonesia adalah?",
        "pilihan": ["A. Bandung", "B. Jakarta", "C. Surabaya", "D. Medan"],
        "jawaban": "B"
    },
    {
        "pertanyaan": "Hewan tercepat di dunia adalah?",
        "pilihan": ["A. Singa", "B. Cheetah", "C. Elang", "D. Kuda"],
        "jawaban": "B"
    },
    {
        "pertanyaan": "Planet terbesar dalam tata surya adalah?",
        "pilihan": ["A. Bumi", "B. Mars", "C. Jupiter", "D. Saturnus"],
        "jawaban": "C"
    }
]

# Program kuis sederhana
def kuis():
    if jawab == "s":
        time.sleep(1)
        clear_screen()
        skor = 0
        for indeks, soal in enumerate(soal_kuis, start=1):
            print(f"\nSoal {indeks}: {soal['pertanyaan']}")
            for pilihan in soal["pilihan"]:
                print(pilihan)
            jawaban = input("Masukkan jawaban Anda (A/B/C/D: ").strip().upper()
            if jawaban == soal["jawaban"]:
                print("Benar!")
                skor += 1
            else:
                print(f"Salah! Jawaban yang benar adalah {soal['jawaban']}")
        print(f"\nKuis selesai! Skor Anda: {skor}/{len(soal_kuis)}")

# Menjalankan kuis
kuis()