# definisi dan fungsi
def contoh_fungsi (contoh):
    if contoh <= 2:
        return False
    for n in range (contoh):
        if (contoh % 2) == 0:
            return False
        return True
    
# input Python
contoh = int(input("Masukkan contoh :"))
    
# Percabangan 1 
if contoh > 0:
    print ("Positif", contoh)
elif contoh < 0:
    print ("Negatif", contoh)
else:
    print ("Bukan bilangan", contoh)

# Percabangan 2
if contoh_fungsi (contoh):
    print ("Contoh", contoh)
else:
    print ("Bukan contoh", contoh)

# Looping
print ("Contoh ke- ",contoh)
for n in range (1, contoh + 1):
    print (n,end = "")