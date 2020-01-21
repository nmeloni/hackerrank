def kangaroo(x1, v1, x2, v2):
    num = x2-x1
    den = v1-v2
    if den == 0:
        if num == 0:
            return "YES"
        else:
            return "NO"
    k = num/den
    res = (math.floor(k)==k) and k>=0
    if res:
        return "YES"
    else:
        return "NO"
