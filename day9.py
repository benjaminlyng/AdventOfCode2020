import numpy as np

with open("day9.txt", "r") as f:
    a = np.fromfile(f,sep='\n', dtype=np.uint32)

p = 25
for i in range(len(a)-(p)):
    pre = a[i:i+p]
    target= a[i+p]    
    if not any((target - pre[j]) in pre for j in range(p-1)):
        print(f"Part 1 - {target=}")
        break

##Part 2:
sums=0
i=0
j=1
while sums != target:
    sums = sum(a[i:j])
    if sums > target:
        i += 1
        j = i + 1
    elif sums < target:
        j += 1

print(f"Part 2 - {min(a[i:j])+ max(a[i:j])=}")
