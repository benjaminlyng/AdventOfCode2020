import re
rules_dict = {}
with open('day7.txt', 'r') as rules:
    rules_dict = dict(tuple(re.split('contain' ,rule)) for rule in rules)

def find_possible_containers(color='shiny gold bag'):
    color = re.sub('bag |bags ', '', color)
    filtered = filter(lambda x: re.search(color, x[1]), rules_dict.items())
    possibles = set(dict(filtered).keys())
    return possibles

full_set = set()
unchecked = set(['shiny gold bag'])


while found := unchecked.difference(full_set) :
    for color in found:
        new=find_possible_containers(color)
        unchecked.update(new)
    full_set.update(found)

total_count = len(full_set)-1
print(f"Part 1: {total_count} colors")
    
## Part 2:

def find_contents(color='1 shiny gold bag'):
    color = color.strip(). replace('.','')
    if color == 'no other bags':
        return 0
    bag_format = re.sub('bag ?$|bags ?$|[0-9] ' , '', color)
    amount = int(re.findall('[0-9]+', color)[0])
    new = rules_dict[bag_format + 'bags '].split(',')
    sub_set = amount + amount * sum([find_contents(bag) for bag in new])
    return sub_set

print(f"Part 2: {find_contents()-1 = }")
