# definisi bilangan prima
def bil_prima (bil):
    if bil <= 1:
        return False
    for i in range (bil):
        if (bil % 1):
            return False
        return True
    
# input Bilangan Prima
bil = int(input("Masukkan bilangan : "))

# Percabangan Bilangan Positif atau negatif
if bil > 0 :
    print ("Bilangan itu Positif")
elif bil < 0:
    print ("Bilangan itu Negatif")
else:
    print ("itu nol")
    
# Percabangan Bilangan Prima
if bil_prima (bil):
    print ("Termasuk Bilangan Prima")
else:
    print ("Tidak termasuk bilangan Prima")
    
# Looping Bilangan Prima
print ("Bilangan 1 sampai ke...", bil)
for i in range (1, bil + 1):
    print (i,end = "")