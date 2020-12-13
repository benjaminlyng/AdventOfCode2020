import numpy as np
import re

with open("day11.txt", "r") as f:
    a = f.read().splitlines()
a = [re.sub('L', '1', b) for b in a]
a = [re.sub(r'\.', '0', b) for b in a]
chairs = np.zeros([len(a), len(a[0])], dtype=np.float)
a = np.array([[int(i) for i in row] for row in a])
chairs = chairs + a


chairs[chairs==0] = np.nan
chairs[chairs==1] = 0


def seat_switch(people):

    lx=len(people)
    ly=len(people[0])
    # boarder of NaN's (Band name idea!)
    grid = people.copy()
    grid =np.insert(grid, (0,lx), np.nan, axis=0)
    grid =np.insert(grid, (0,ly), np.nan, axis=1)

    counter = np.zeros([lx,ly])
    for i in (0,1,2):
        for j in (0,1,2):
            if i == 1 and j == 1:
                continue   
            counter += grid[i:(lx+i),j:(ly+j)] == 1
    
    people[(counter >= 4) & (people ==1)] = 0
    people[(counter == 0) & (people ==0)] = 1
    return people

chairs_next = seat_switch(chairs.copy())
while not np.allclose(chairs, chairs_next , equal_nan=True):
    chairs = chairs_next
    chairs_next = seat_switch(chairs.copy())
    
print(np.nansum(chairs))