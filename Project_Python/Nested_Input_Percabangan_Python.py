a = int (input ("Masukkan angka 1: "))
b = int (input ("Masukkan angka 2: "))
c = int (input ("Masukkan angka 3: "))

if a > b and a > c:
    print ("Angka 1 adalah yang terbesar")
elif b > a and b > c:
    print ("Angka 2 adalah yang terbesar")
elif c > a and c > b:
    print ("Angka 3 adalah yang terbesar")
else:
    print ("Ada dua atau lebih angka yang sama besar")