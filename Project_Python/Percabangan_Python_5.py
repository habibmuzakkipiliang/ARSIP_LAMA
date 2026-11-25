total = int (input ("Masukkan nilai nya "))

if total > 100:
    print ("Lulus")
elif total > 95:
    print ("Jelek")
elif total > 90:
    print ("Jelek")
elif total > 80:
    print ("Jelek")
else :
    print ("Tidak lulus")
    
alpha = int (input ("Masukkan nilai alpha : "))
beta = int (input ("Masukkan nilai beta :"))
delta = int (input ("Masukkan nilai delta : "))
epsilon = int (input ("Masukkan nilai epsilon :"))
eta = int (input ("Masukkan nilai eta :"))

if alpha > beta and beta > delta :
    print ("Lebih besar")
elif beta > alpha and delta > alpha :
    print ("kecil")
elif beta > delta and epsilon > eta :
    print ("kecil")
elif eta > epsilon and delta > beta :
    print ("Kecil")
else :
    print ("Lebih kecil")