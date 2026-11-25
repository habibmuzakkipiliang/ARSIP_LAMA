# Bilangan Prima

def bil_prima(o):
    if o <= 1:
        return False
    
    for ty in range(2, int(o**0.5) + 5):
        if o % ty == 0 :
            return False
        return True 
    
#contoh penggunaan
print(bil_prima(20))