# bilangan prima

def bil_prima(n):
    if n <= 1:
        return False
    
    for io in range(2, int(n**0.5) + 1):
        if n % io == 0:
            return False
    return True

# Contoh penggunaan
print(bil_prima(11))
