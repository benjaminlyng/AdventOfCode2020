import csv
import json
import re

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
with open('day4.txt', 'r') as csv_file:
    lines = csv_file.readlines()

as_text = "".join(lines).replace(' ', '\n')
newlist = as_text.split('\n\n')
newlist = [x.split('\n') for x in newlist]
newlist = [dict(attr.split(':') for attr in x) for x in newlist]

counter = 0
for passport in newlist:
    if all(y in passport.keys() for y in required):
        counter += 1
print(f"Part 1 \n {counter=}")


def check_passport(passport):
    if all(y in passport.keys() for y in required) \
    and (1920 <= int(passport.get('byr')) <= 2002) \
    and (2010 <= int(passport.get('iyr')) <= 2020) \
    and (2020 <= int(passport.get('eyr')) <= 2030) \
    and re.findall("(^[0-9]+)(cm|in)$", passport.get('hgt')) \
    and re.findall("(^#)([0-9a-f]{6})$", passport.get('hcl')) \
    and re.findall("^(amb|blu|brn|gry|grn|hzl|oth)$", passport.get('ecl')) \
    and re.findall("^([0-9]{9})$", passport.get('pid')) \
    and (((passport.get('hgt')[-2:] == 'cm') and (150 <= int(passport.get('hgt')[:-2]) <= 193)) \
        or (passport.get('hgt')[-2:] == 'in' and (59 <= int(passport.get('hgt')[:-2]) <= 76))):

        return True
    return False


counter=0
for passport in newlist:
    if check_passport(passport):
        counter += 1
print(f"Part 2 \n {counter=}")

# map(filter(lambda x: x in passport.keys()))
# reduce(lambda x: x in required, newlist[0])
