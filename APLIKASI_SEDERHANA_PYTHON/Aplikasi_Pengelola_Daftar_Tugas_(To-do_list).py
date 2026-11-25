def to_do_list():
    daftar_tugas = []
    
    while True:
        print("\nMenu")
        print("1. Tambah tugas")
        print("2. Hapus tugas")
        print("3. Lihat daftar tugas")
        print("4. Keluar")
        pilihan = input("pilih opsi: ")
        
        if pilihan == '1':
            tugas = input("masukan tugas: ")
            daftar_tugas.append(tugas)
            print("Tugas berhasil ditambahkan!")
        elif pilihan == '2':
            tugas = input("masukan tugas yang ingin dihapus: ")
            if tugas in daftar_tugas:
                daftar_tugas.remove(tugas)
                print("Tugas berhasil dihapus!")
            else:
                print("Tugas tidak ditemukan.")
        elif pilihan == '3':
            print("Daftar Tugas:")
            for i, tugas in enumerate(daftar_tugas, 1):
                print(f"{i}. {tugas}")
        elif pilihan == '4':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid")
            
to_do_list()