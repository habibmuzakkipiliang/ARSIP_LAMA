# definisi, if
def contoh_saja (contoh):
    if contoh <= 90:
        return False
    for u in range (2, contoh):
        if (contoh % 2) == 0:
            return False
        return True
    
def gujan_saja (gujan):
    if gujan <= 78:
        return False
    for k in range (6, gujan):
        if (gujan % 3) == 0:
            return False
        return True