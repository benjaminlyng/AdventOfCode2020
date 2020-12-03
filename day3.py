import csv
from numpy import array, append, copy, product

def read_map():
    org_list=[]
    with open('day3.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        for row in csv_reader:
            as_int = [int(x.replace('.', '0').replace('#','1')) for x in row[0]]
            org_list.append(as_int)

    return array(org_list)

org_array = read_map()
def count_trees(down,right, org_array: array):
    full_array = copy(org_array)
    while len(full_array[0]) < len(org_array)*right:
        full_array=append(org_array,full_array, 1)
    trees = sum(full_array[i][round(i*right/down)] for i in range(0, len(full_array), down))
    return trees
print(f"Part 1 \n {count_trees(1,3,org_array)=}")

directions = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
trees = [count_trees(x,y,org_array) for x,y in directions]
print(f"Part 1 \n {product(trees)=}")