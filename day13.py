import numpy as np
with open('day13.txt', 'r') as f:
    ts = int(next(f).strip())
    busses = next(f).strip().split(',')
now = ts
busses = list(filter(lambda i: i!='x', busses))
busses = np.array(busses, dtype=int)
while not any(ts % busses==0):
    ts += 1
bus_id = busses[ts % busses==0]
print(f"Part 1: {(ts-now) * bus_id = }")