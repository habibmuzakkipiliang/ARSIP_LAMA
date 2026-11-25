# definisi fungsi
def untuk_fungsi (saja):
    if saja <= 90:
        return False
    for k in range (2, saja):
        if (k % 50) == 0:
            return False
        return True

# input 
saja = int(input("Masukkan saja :"))

# Percabangan 1
if saja > 0:
    print ("Positif")
elif saja < 0:
    print ("Negatif")
else:
    print ("Bukan")
    
# Percabangan 2
if untuk_fungsi (saja):
    print ("Termasuka fungsi")
else:
    print ("Termasuk fungsi")
    
# Looping
print ("Bukan Bilangan", saja)
for k in range (2, saja + 5):
    print (k,end = "")
    