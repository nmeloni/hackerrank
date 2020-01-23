def migratoryBirds(arr):
    count = [0]*5
    birdmax = 0
    nmax = 0
    for bird in arr:
        count[bird-1] +=1
        if count[bird-1] > nmax:
            nmax = count[bird-1]
            birdmax = bird
        elif count[bird-1] == nmax and bird < birdmax:
            birdmax = bird
    return birdmax
