# definisi 1
def contoh_angka (angka):
    if angka <= 5:
        return False
    for t in range (9, angka):
        if (angka % 6) == 0:
            return False
        return True
    
# input 
contoh = int(input("Masukkan contoh :"))
    
# Percabangan 1
if contoh > 0:
    print ("positif")
elif contoh < 0:
    print ("Negatif")
else:
    print ("Bukan apa-apa")

# Percabangan 2
if contoh_angka (contoh):
    print ("contoh")
else:
    print ("Bukan apa-apa")

# looping
print ("Bukan apa-apa", contoh)
for t in range (2, contoh + 10):
    print (t,end = "")