# luas persegi panjang
p = int (input ("Masukkan persegi panjang (p) : "))
l = int (input ("Masukkan persegi panjang (l) : "))

print ("Luas persegi panjang : \n", p * l)
print ("Keliing persegi panjang : \n", 2 * (p + l))

# luas persegi empat 
s = int (input ("Masukkan persegi empat (s) : "))

print ("Luas persegi empat : \n", s * s)
print ("Keliling persegi empat : \n ", 4 * s)

# luas dan keliling belah ketupat 
d1 = int (input ("Masukkan belah ketupat d1 : "))
d2 = int (input ("Masukkan belah ketupat d2 : "))
s = int (input ("Masukkan belah ketupat s : "))

print ("Luas Belah ketupat  : \n ", d1 * d2 / 2)
print ("Keliling Belah ketupat : \n ", 4 * s)

# luas dan keliling Trapesium
a = int (input ("Masukkan Trapesium a : "))
b = int (input ("Masukkan Trapesium b : "))
c = int (input ("Masukkan Trapesium c : "))
d = int (input ("Masukkan Trapesium d : "))
t = int (input ("Masukkan Trapesium tinggi : "))

print ("Luas Trapesium : \n ", a + b / 2 * t) 
print ("Keliling Trapesium : \n", a + b + c + d)

# Luas dan keliling segitiga
a = int (input ("Masukkan segitiga a : "))
b = int (input ("Masukkan segitiga b : "))
c = int (input ("Masukkan segitiga c : "))
t = int (input ("Masukkan segitiga tinggi : "))

print ("Luas Segitiga : \n", a * t / 2)
print ("Keliling Segitiga : \n",  a + b + c)