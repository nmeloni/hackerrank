def pickingNumbers(a):
    a.sort()
    maxlen = 0
    deb,mid = 0,0
    i = 1

    while i<len(a):
        if a[i] == a[i-1]+1:
            mid=i
        if a[i] > a[deb]+1:
          newlen = i-deb
          if newlen > maxlen:
              maxlen = newlen
          if a[deb] == a[mid]+1:
              deb = mid
          else:
              deb = i
        i+=1
    newlen = i-deb
    if newlen > maxlen:
        maxlen = newlen
    return maxlen
