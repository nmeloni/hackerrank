def repeatedString(s, n):
    count = [0]*len(s)
    if s[0]=='a':
        count[0]=1
    for i in range(1,len(s)):
        count[i]=count[i-1]
        if s[i]=='a':
            count[i]+=1
    q,r = n//len(s), n%len(s)
    if r==0:
        return q*count[-1]
    else:
        return q*count[-1]+count[r-1]

if __name__=='__main__':
    print(repeatedString('a',10000))
    print(repeatedString('aba',10))

