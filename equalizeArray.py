def equalizeArray(arr):
    count=[0]*100
    imax=0
    for i in range(len(arr)):
        count[arr[i]-1]+=1
        if count[arr[i]-1]>count[imax]:
            imax=arr[i]-1
    return len(arr)-count[imax]

if __name__=='__main__':
    print(equalizeArray([3,3,2,1,3])==2)
