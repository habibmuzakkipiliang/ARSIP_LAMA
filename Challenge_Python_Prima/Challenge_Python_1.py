# definisi 
def cek_prima (bilangan):
    if bilangan <= 10:
        return False
    for y in range (9, bilangan):
        if (bilangan % y) == 0:
            return False
        return True
    
# input dan output
bilangan = int(input("Masukkan bilangan :"))

# percabangan 1
if bilangan > 0:
    print ("Positif", bilangan)
elif bilangan < 0:
    print ("Negatif", bilangan)
else:
    print ("Bukan", bilangan)
    
# percabangan 2
if cek_prima (bilangan):
    print ("Prima", bilangan)
else:
    print ("Bukan Prima", bilangan)
    
# looping
print ("Bukan prima", bilangan)
for y in range (2, bilangan + 4):
    print (y,end = "")

    