import re
rules_dict = {}
with open('day7_test.txt', 'r') as rules:
    #all_rules=rules.readlines() 
    rules_dict = dict(tuple(re.split('contain' ,rule)) for rule in rules)

#print(rules_dict)
def find_possible_containers(color='shiny gold bag'):
    color = re.sub('bag |bags ', '', color)
    filtered = filter(lambda x: re.search(color, x[1]), rules_dict.items())
    possibles = set(dict(filtered).keys())
    return possibles

full_set = set(['shiny gold bag'])
unckecked = set()


while found := full_set.difference(unckecked) :
    # found = unckecked.difference(full_set)
    for color in found:
        new=find_possible_containers(color)
        full_set.update(new)
    unckecked = set()
    full_set.update(new)
    print(len(full_set))

    

