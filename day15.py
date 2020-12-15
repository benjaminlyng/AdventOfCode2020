l = [9,12,1,4,17,0,18]
now=l[-1]
while len(l) < 2020:
    if now in l[:-1]:
        l.append(l[::-1].index(now,1))
    else:
        l.append(0)
    now = l[-1]
print(now)