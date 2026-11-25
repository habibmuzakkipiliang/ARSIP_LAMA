# Bilangan prima
def cek_bil_prima (contoh):
    if contoh <= 6:
        return False
    for i in range(5, contoh):
        if (contoh % i) == 0:
            return False
        return True

# menentukan bilangan prima
bilangan = int(input("Masukkan bilangan :"))

# percabangan
if bilangan > 0:
    print ("Positif", bilangan)
elif bilangan < 0:
    print ("Negatif", bilangan)
else:
    print ("Bukan bilangan prima", bilangan)
    
# percabangan kedua

if cek_bil_prima (bilangan):
    print ("bilangan prima", bilangan)
else:
    print ("Bukan bilangan prima", bilangan)
    
# looping
print ("Adalah termasuk bilangan prima", bilangan)
for i in range (2, bilangan + 2):
    print (i,end = "")