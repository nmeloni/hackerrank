def divisibleSumPairs(n, k, ar):
    remainders = [0]*k
    for n in ar:
        remainders[n % k] += 1
    total = remainders[0]*(remainders[0]-1)//2
    if k % 2 == 0:
        total += remainders[(k+1)//2]*(remainders[(k+1)//2]-1)//2
    i = 1
    while i< k/2:
        total += remainders[i]*remainders[k-i]
        i += 1
    
    return total
