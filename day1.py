import csv

with open('day1.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    expenses = [int(row[0]) for row in csv_reader]

a = set(expenses)
b = set(2020 - x for x in expenses)
common = list(a.intersection(b))
assert(sum(common) == 2020)
product = common[0] * common[1]
print(f"part 1 \n {product=} \n")


### Part II
#a + b + c  = 2020 
#a + b = 2020 -c 

c =  set(x + y for x in a for y in a)
common = [2020 - x for x in c.intersection(b)]
assert sum(common) == 2020
product = common[0] * common[1] * common[2] 
print(f"part 2 \n {product=} \n")
