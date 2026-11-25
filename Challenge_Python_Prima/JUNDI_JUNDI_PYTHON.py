# definisi dan fungsi Python
def koplit_banget (jun):
    if jun <= 1:
        return False
    for i in range (jun):
        if (jun % 1) == 0:
            return False
        return True
    
# Input dan Output Python
jun = int(input("Masukkan jun : "))
    
# Percabangan Python
if jun > 0:
    print ("Positif", jun)
elif jun < 0:
    print ("Negatif", jun)
else:
    print ("Bukan keduanya", jun)

# Percabangan Python 1
if koplit_banget (jun):
    print ("Termasuk", jun)
else:
    print ("Tidak termasuk", jun)

# Looping Python
print ("Jun ke- ....", jun)
for i in range (1, jun + 1):
    print (i,end = "")