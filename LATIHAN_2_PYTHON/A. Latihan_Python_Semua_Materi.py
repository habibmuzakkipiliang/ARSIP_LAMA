#Tipe String atau Variabel Python#
print ("Halo Dunia");
print ("Halo Indonesia");

pollo = "Selamat Datang di Duniacoding"
print (pollo)

hallo = "Selamat Datang di Dicoding Indonesia"
print (hallo)

hello = "Selamat Datang di Duniacoding Academy"
print (hello)

d = "Belajar Pemrograman Lengkap "
e = "di "
h = "Dicoding Indonesia"
hasil = d + e + h
print (hasil)

#Tipe Logika Python#
a = 12
b = 90

if a > b :
    print ("a lebih besar daripada b ");
elif a < b :
    print ("a lebih kecil daripada b");
else :
    print ("a dan b sama besar");
    
    
a = 90
b = 12
if a > b :
    print ("a lebih besar daripada b");
elif a < b :
    print ("a lebih kecil daripada b");
else :
    print ("a dan b sama besar");


#Tipe Number Python#
p = -6.3445
r = -7.8990
e = -8.2131
print (p)
print (r)
print (e)

t = -9.1333
e = -10.3131
x = -11.3232
print (t)
print (e)
print (x)

#Tipe Boolen Python#
foo = True 
doo = False 
print (foo)
print (doo)

koo = 12 < 13
print (koo)
koo = 89 > 12
print (koo)
koo = "A" == "a"
print (koo)

#Tipe List Python#
w = ["Belajar", "Coding", "Di", "Dicoding Indonesia"]
d = [100, 200, 300, 400]
j = ["Python", 233, 450, 120, True]
print (w)
print (d)
print (j)

un = ["Belajar", "Pemrograman", "Di", "Dicoding Indonesia"]
qw = ["Belajar", 12, 13, 900]
we = ["Java", 313, 131, 313, True]
print (type (un))
print (type (qw))
print (type (we))

roo = ["Java", 2330, 33134, 13, "Golang"]
print (roo [0])
print (roo [1])
print (roo [2])
print (roo [3])
print (roo [4])

#Tipe Tuple Python#
yuu = ("Belajar", "Coding", "di", "Duniacoding")
klo = (100, 200, 300, 400, 500, 600 )
mo  = ("Jacha", 134, 242, 133, True)
print (yuu)
print (klo)
print (mo)

yuu = ("Belajar", "Coding", "di", "Duniacoding")
klo = (100, 200, 300, 400, 500, 600) 
mo  = ("Jacha", 134, 242, 133, True)
print (type (yuu))
print (type (klo))
print (type (mo))

yuu = ("Belajar", "Coding", "di", "Duniacoding", "Indonesia")
print (yuu [0])
print (yuu [1])
print (yuu [3])
print (yuu [4])

#Tipe Set Python#
lo = {"Belajar", "Coding", "di", "Sandhika Galih"}
ty = {100, 200, 300, 400, 500, 600}
re = {"Belajar", 34, 23, 12, True}
print (lo)
print (ty)
print (re)

lo = {"Belajar", "Coding", "di", "Sandhika Galih"}
ty = {100, 200, 300, 400, 500, 600}
re = {"Belajar", 34, 23, 12, True}
print (type (lo))
print (type (ty))
print (type (re))

#Operator Aritmatika Python#

r = 11
e = 32

print (' r + e =', x + e),
print (' r * e =', r * e)
print (' r ** e =', r**e )

hasil = 12 + 12
print (hasil)

hasil = (13 + 1) * (90 + 1)
print (hasil)

hasil = (12 + 1) * (33 +1)
print (hasil)

#Operator Aritmatika Perbandingan Python#

p = 90 
o = 12

print (' p =', p)
print (' o =', o)

print (" p == o hasilnya", p == o)
print (" p != 0 hasilnya", p != o)
print (" p < o hasilnya", p < o)
print (" p > o hasilnya", p > o)

#Tipe Dictionary Python#
data = {
    "nama lengkap" : "Habib Muzakki",
    "nama panggilan" : "Habib",
    "kelas" : "10 Agama",
    "nomor hp wa" : "0821-1347-7785",
    "nomor hp telegram" : "0851-6182-1652",
    "ig account" : "@habib_muzakki_piliang",
    "tiktok account" : "@habib_muzakki_piliang",
}

print ("Nama lengkap :", data ["nama lengkap"]),
print ("Nama panggilan :", data ["nama panggilan"]),
print ("Kelas :", data ["kelas"]),
print ("Nomor HP WA :", data ["nomor hp wa"]),
print ("Nomor Hp Telegram :", data ["nomor hp telegram"]),
print ("IG Account :", data ["ig account"]),
print ("Tiktok Account :", data ["tiktok account"]),

data = {
    "nama lengkap" : "John Lock James",
    "nama panggilan" : "John",
    "pekerjaan" : "Developer, Programmer, Software Engineering",
}
print ("Nama lengkap :", data ["nama lengkap"]),
print ("Nama Panggilan :", data ["nama panggilan"]),
print ("Pekerjaan :", data ["pekerjaan"]),