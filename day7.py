import re
rules_dict = {}
with open('day7.txt', 'r') as rules:
    rules_dict = dict(tuple(re.split('contain' ,rule)) for rule in rules)

#print(rules_dict)
def find_possible_containers(color='shiny gold bag'):
    color = re.sub('bag |bags ', '', color)
    filtered = filter(lambda x: re.search(color, x[1]), rules_dict.items())
    possibles = set(dict(filtered).keys())
    return possibles

full_set = set()
unchecked = set(['shiny gold bag'])


# while found := unchecked.difference(full_set) :
#     for color in found:
#         new=find_possible_containers(color)
#         unchecked.update(new)
#     full_set.update(found)

total_count = len(full_set)-1
print(f"Part 1 - {total_count} colors")
    
## Part 2:

def find_contents(color='shiny gold bags '):
    #color = re.sub('bag |bags ', '', color)
    #filtered = filter(lambda x: re.search(color, x[1]), rules_dict.items())
    contents =list(dict(filtered).values())
    return contents
cont1 = rules_dict.get('shiny gold bags ')

cont2 = re.findall('[0-9] [a-z ]*', cont1)

for bag in cont2:
    print(re.replace(('bag|bags', '').strip())
    bag_format = bag[2:]+'s '
    print(bag_format)
    print(rules_dict.get(bag_format))

