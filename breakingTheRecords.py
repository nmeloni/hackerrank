def breakingRecords(scores):
    smin, smax = scores[0], scores[0]
    rmin, rmax = 0,0
    for score in scores[1:]:
        if score < smin:
            smin = score
            rmin += 1
        elif score > smax:
            smax =score
            rmax += 1
    return rmax, rmin
