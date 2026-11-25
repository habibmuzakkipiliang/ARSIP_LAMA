# definisi Python
def untuk_saya (saya):
    if saya <= 1:
        return False
    for u in range (saya):
        if (saya % 1) == 0:
            return False
        return True
    
# Input Python
saya = int(input("Masukkan input :"))

# Percabangan 1
if saya > 0:
    print ("Positif", saya)
elif saya > 0:
    print ("Negatif", saya)
else:
    print ("Bukan termasuk", saya)
    
# Percabangan 2
if untuk_saya (saya):
    print ("Iya", saya)
else:
    print ("Tidak", saya)
    
# Looping
print ("contoh ke- ...", saya)
for u in range (1, saya + 1):
    print (u,end = "")