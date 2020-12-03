import csv
from numpy import array, append

direction = 3

org_list=[]
with open('day3.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=' ')
    for row in csv_reader:
        as_int = [int(x.replace('.', '0').replace('#','1')) for x in row[0]]
        org_list.append(as_int)

a = array(org_list)
b = array(org_list)
while len(b[0]) < len(a)*direction:
    b=append(a,b, 1)
trees = sum(b[i][i*3] for i in range(0, len(b)))
print(f"Part 1 \n {trees=}")