import numpy as np
with open('day22.txt', 'r') as f:
    decks = f.read().split('\n\n')

decks = np.array([x.splitlines()[1:] for x in decks], dtype= int)
p1, p2 = decks[0], decks[1]
l = len(p1) + len(p2)
p1_next, p2_next = p1, p2
while len(p1) > 0 and len(p2) >0:
    assert len(p1) + len(p2) == l
    r = min(map(len, [p1,p2]))
    p1_rem, p2_rem = p1[r:], p2[r:]
    p1, p2 = p1[:r], p2[:r]

    p1_next = np.insert(p1, np.where(p1>p2)[0]+1 , p2[p1>p2])
    p2_next = np.insert(p2, np.where(p1<p2)[0]+1 , p1[p1<p2])
    for x in p1[p1<p2]:
        p1_next = np.delete(p1_next, np.where(p1_next==x))
    for y in p2[p1>p2]:
        p2_next = np.delete(p2_next, np.where(p2_next==y))

    p1 = np.insert(p1_next, 0, p1_rem)
    p2 = np.insert(p2_next, 0, p2_rem)


print(sum(x*y for x,y in enumerate(p1[::-1],1)))
print(sum(x*y for x,y in enumerate(p2[::-1],1)))