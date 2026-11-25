def kalkulator():
    print("Pilih operasi:\n1. Tambah\n2. Kurang\n3. Kali\n4. Bagi")
    pilihan = input("Masukkan pilihan (1/2/3/4): ")
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    
    if pilihan == '1':
        print(f"Hasil: {angka1 + angka2}")
    elif pilihan == '2':
        print(f"Hasil: {angka1 - angka2}")
    elif pilihan == '3':
        print(f"Hasil: {angka1 * angka2}")
    elif pilihan == '4':
        print(f"Hasil: {angka1 / angka2}")
    else:
        print("Pilihan tidak valid.")
        
kalkulator()