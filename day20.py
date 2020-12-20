import re 
from math import prod
with open('day20.txt', 'r') as f:
    pixels = f.read()

pixels = re.findall(r'Tile \d*:[.#\n]*', pixels)

mem={}
pixels = map(lambda x: x.splitlines(), pixels)
for p in pixels:
    id = re.search(r'\d+', p[0]).group(0)
    p = p[1:-1]
    assert len(p) == 10
    #edges:
    top = p[0]
    bot = p[-1]
    left = "".join([x[0] for x in p])
    right = "".join([x[-1] for x in p])
    directions = [direction for direction in [top,bot,left,right]]
    _ = [directions.append(direction[::-1]) for direction in [top,bot,left,right]]

    for i in directions:
        mem[i] = mem.get(i, [])
        mem[i].append(id)

corners = filter(lambda x: len(x)<2, mem.values())
corners = [c[0] for c in corners]

res = filter(lambda x : corners.count(x) ==4, set(corners))
res = prod(int(x) for x in res)

print(f"Part 1: {res}")