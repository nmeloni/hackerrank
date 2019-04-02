def jumpingClouds(c):
    nbsteps=0
    step = len(c)-1
    while step !=0:
        if step >=2 and c[step-2]==0:
            step-=2
        else:
            step-=1
        nbsteps+=1    
    return nbsteps

if __name__=='__main__':
    print(jumpingClouds([0,0,1,0,0,1,0])==4)
    print(jumpingClouds([0,0,0,0,1,0])==3)
