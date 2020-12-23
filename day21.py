from more_itertools import flatten
def find_alergens(ingredients_list):
    matches = dict()
    all_ingredients = list()
    for x in ingredients_list:
        x=x[:-1]
        ing, alergens = x.split(' (contains ')
        ing, alergens = ing.split(' '), alergens.split(', ')
        all_ingredients.append(ing)
        for a in alergens:
            matches[a] = matches.get(a, set(ing))
            matches[a] = matches[a].intersection(set(ing))
            
    return matches
    

with open('day21.txt', 'r') as f:
    ingredient_text = f.read()
ingredient_list = ingredient_text.splitlines()
all_ingredients = [ x[:x.index(' (')].split() for x in ingredient_list ]
all_ingredients = list(flatten(all_ingredients))
possible_alergens = find_alergens(ingredient_list)
print(possible_alergens)

safe = [x for x in all_ingredients if x not in set(flatten(possible_alergens.values()))]

print(f"Part 1: {len(safe)} ingredients are safe")

it = 0
alergen_names = set()
while it < 5:
    it += 1
    unknown_alergens = dict(filter(lambda x: len(x[1]) > 1, possible_alergens.items()))
    known_alergens = dict(filter(lambda x: len(x[1]) ==1, possible_alergens.items()))
    
    alergen_names.update(set(flatten(known_alergens.values())))
    
    possible_alergens = {key:(val.difference(alergen_names) if key in unknown_alergens else val)  for key,val in possible_alergens.items() }
    
canonical_dangerous_ingredient_list = sorted([x for x in known_alergens])
canonical_dangerous_ingredient_list = ",".join([list(known_alergens[a])[0] for a in canonical_dangerous_ingredient_list])
print(canonical_dangerous_ingredient_list)