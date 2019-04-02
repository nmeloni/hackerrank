def nonDivisibleSubset(k, S):
    residues=[0]*k
    maxsize=0
    for n in S:
        r = n%k
        residues[r]+=1        
    if k%2==0:
        residues[k//2]=min(residues[k//2],1)
    size = k//2
    if residues[0]!=0:
        maxsize+=1
    for i in range(1,size+1):
        maxsize+=max(residues[i],residues[k-i])
    return maxsize

if __name__ == '__main__':
    print(nonDivisibleSubset(3,[1,7,2,4]) == 3)
    print(nonDivisibleSubset(7,[278,576,496,727,410,124,338,149,209,702,282,718,771,575,436])==11)
    print(nonDivisibleSubset(4,[1,2,3,4,5,6,7,8,9,10])==5)
