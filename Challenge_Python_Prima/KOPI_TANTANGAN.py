# definisi Python
def untuk_kopi(kopi):
    if kopi <= 1:
        return False
    for t in range (kopi):
        if (kopi % 1) == 0:
            return False
        return True
    
# input python
kopi = int(input("Masukkan kopi = ......"))

# percabangan python
if kopi > 0:
    print ("Positif", kopi)
elif kopi < 0:
    print ("Negatif", kopi)
else:
    print ("Bukan", kopi)
    
# percabangan python
if untuk_kopi(kopi):
    print ("Kategori", kopi)
else:
    print ("Bukan", kopi)
    
# Looping 
print ("Jumlah ke- ",kopi)
for t in range (1, kopi + 1):
        print (t,end = ".......")
