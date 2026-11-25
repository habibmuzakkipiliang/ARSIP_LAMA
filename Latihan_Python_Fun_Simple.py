# Hello World Python
print ("Hello World", "\n")

# Sintaks dasar Python

x = "- Acara ABG (Arena Boarding Gembira) 2025 adalah acara yang keren, terbaik dan paling dikenal sepanjang hidupku, terutama saat makan-makan di RM Saung Sunda Bhayangkara, Kota Serang, Provinsi Banten"
print (x, "\n")

u = "- Acara MAN2 Fest 2024 adalah acara yang terbaik yang pernah ada selama saya sekolah di MAN 2 Kota Serang dan paling seru"
print (u, "\n")

angka = 23
print (angka, "\n")

desimal = 2.24
print (desimal, "\n")

# tipe data Python

a = 12 # integer
b = "Hallo " # String
c = 3.14 # float
d = ["Hujan", "Es", "Badai", "Salju"] # Array atau List
e = {"Rurik", "Hansel", "Roger", "Dower"} # Set
f = ("Minangkabau", "Jawa", "Bali", "Sasak") # Tuple

print (a)
print (b)
print (c)
print (d)
print (e)
print (f)

# Operator Dasar Python
o = 12
t = 13

print ("Tambah : ", o + t)
print ("Kurang :", o - t)
print ("Bagi : ", o / t)
print ("Kali : ", o * t)
print ("Pangkat : ", o ** t)
print ("Bagi double : ", o // t)
print ("Modulus : ", o % t)

# operator perbandingan 

print ("Hasilnya :", o < t)
print ("Hasilnya : ", o > t)
print ("Hasilnya : ", o == t)
print ("Hasilnya : ", o <= t)
print ("Hasilnya : ", o >= t)

# Operator Logika

m = True
l = False

print (m or l)
print (m and l)
print (not l)
print (not m)

# Percabangan Python Biasa

yui = 50

if yui > 23:
    print ("Besar")
elif yui < 23:
    print ("Kecil")
else:
    print ("Sama saja")
    
# Percabangan Bersarang

jui = 55
ren = True

if jui < 50:
    if (ren):
        print ("Besar")
    elif jui > 50:
        print ("Kecil")
else :
    print ("Sama saja")
    
# for perulangan Python

for i in range (1,5):
    print ("Perulangan ke -", i)
    
for e in range (10, 15):
    print ("Ulang ke -", e)
    
ju = ["Juka", "Jepang", "Orodoks", "Johannes"]

for ju in sorted (ju):
    print (ju)
    
# while perulangan python

t = 0

while t < 3:
    print ("While ke -", t)
    t = t + 1
    
# function Python

def ruji ():
    print ("Hello Dunia")

ruji ()
ruji ()

def hujan (hujan):
    print ("Hello " + hujan)
    
hujan ("Felicia Kurniawan")
hujan ("Theresa")
hujan ("Freya JKT48")