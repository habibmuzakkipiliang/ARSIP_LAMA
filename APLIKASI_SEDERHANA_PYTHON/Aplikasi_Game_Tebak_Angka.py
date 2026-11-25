import random 

def tebak_angka():
    angka_rahasia = random.randint(1, 100)
    percobaan = 0 
    print("Tebak angka antara 1 hingga 100") 
    while True:
        tebakan = int(input("Masukkan tebakanmu: "))
        percobaan += 1
        
        if tebakan < angka_rahasia:
            print("Terlalu kecil")
        elif tebakan > angka_rahasia:
            print("Terlalu besar")
        else:
            print(f"Selamat! Kamu menebak dalam {percobaan} percobaan.")
            break
        
tebak_angka()