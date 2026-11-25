menu_makanan = {
    "Rendang" : 10000,
    "Tambunsu" : 10000,
    "Nasi Goreng Padang" : 10000
}

menu_minuman = {
    "Teh Talua" : 9000,
    "Kopi Kawa Daun" : 8000,
    "Ampiang Dadiah" : 7000
}

print ("===Menu Makanan===")
for makanan, harga in menu_makanan.items():
    print (f"{makanan:20} Rp {harga :,.2f}")
    
print ("===Menu Minuman===")
for minuman, harga in menu_minuman.items():
    print (f"{minuman:20} Rp {harga :,.2f}")
    
    