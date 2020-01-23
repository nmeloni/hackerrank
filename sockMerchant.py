def sockMerchant(n, ar):
    ar.sort()
    total = 0
    beg,end = 0,0
    while end < len(ar):
        if ar[beg]!=ar[end]:
            total+= (end-beg)//2
            beg = end
        end += 1
    total+= (end-beg)//2
    return total
