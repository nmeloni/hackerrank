def getTotalX(a, b):
    maxa = max(a)
    minb = min(b)
    lcd = maxa
    count = 0
    while lcd <= minb:
        bts = True
        for div in a:
            if lcd % div !=0:
                bts = False
                break
        if bts:
            for mul in b:
                if mul % lcd !=0:
                    bts = False
                    break
        if bts:
            count +=1
        lcd += maxa
    return count
