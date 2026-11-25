# Definisikan fungsi untuk mengecek bilangan prima 
def cek_prima(angka):
    if angka <= 1:
        return False
    for i in range(2, angka):
        if (angka % i) == 0:
            return False
    return True

# Meminta Input pengguna 
bilangan = int(input("Masukkan bilangan :"))

# Memeriksa bilangan itu 0 atau tidak
if bilangan > 0:
    print ("Bilangan", bilangan,"itu Positif")
elif bilangan < 0:
    print ("Bilangan", bilangan, "itu Negatif")
else:
    print ("Bilangan", bilangan, "adalah nol")

# Memanggil fungsi untuk bilangan prima

if cek_prima (bilangan):
    print ("Bilangan", bilangan, "Termasuk Bilangan Prima")
else:
    print ("Bilangan", bilangan, "Bukan termasuk bilangan Prima") 

# Menggunakan looping untuk mencetak bilangan dari 1 hingga bilangan yang dimasukkan
print ("Bilangan dari 1 hingga", bilangan, "adalah")
for i in range(1, bilangan + 1):
    print (i,end = "")