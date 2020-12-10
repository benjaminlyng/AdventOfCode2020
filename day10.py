import numpy as np

with open("day10.txt", "r") as f:
    a = np.fromfile(f,sep='\n', dtype=np.int)
a = np.insert(a, 0, 0)
a = np.append(a, np.max(a)+3)

a.sort()

b= list(a[i+1]-a[i] for i in range(len(a)-1))
print(f"Part 1 - {b.count(1)* b.count(3)=}")
