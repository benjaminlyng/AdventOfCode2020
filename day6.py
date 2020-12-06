import csv

with open('day6.txt', 'r') as csv_file:
    lines = csv_file.readlines()

as_text = "".join(lines).replace(' ', '\n')
newlist = as_text.split('\n\n')
full_set = [set(x.replace('\n', '')) for x in newlist]
count = sum(len(group) for group in full_set)
print(f"Part 1 - {count=}")


grouped_list = list(x.split('\n') for x in newlist)
counts = []
for group in grouped_list:
    group_set = [set(x) for x in group]
    common = group_set[0].intersection(*group_set)
    counts.append(len(common))

print(f"Part 2 - {sum(counts)=} ")

## Part 2 rewritten:
def get_common_count(group:list):
    """ Count letters that are common in each entry of a list of strings
    >>> get_common_count(['ab', 'ac'])
    1
    >>> get_common_count(['a', 'b', 'c'])
    0
    """
    group_set = [set(x) for x in group]
    common = group_set[0].intersection(*group_set)
    return len(common)

counts = map(get_common_count, grouped_list)
print(f"Part 2 - rewritten - {sum(counts)=} ")


