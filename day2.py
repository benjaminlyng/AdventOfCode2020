import csv
import re

def check_password(mincount, maxcount, letter, password):
    """ checks if the letter appears in a password the correct amount of times
    
    >>> check_password(1,3, "a", "abcde")
    True
    >>> check_password(1,3, "b", "cdefg")
    False
    >>> check_password(2,9, "c", "ccccccccc")
    True
     """
    found = re.findall(letter, password)
    return  mincount <= len(found) <= maxcount

def check_password2(pos1, pos2, letter, password):
    """ checks if the letter appears in a password in one of the specified places
    
    >>> check_password2(1,3, "a", "abcde")
    True
    >>> check_password2(1,3, "b", "cdefg")
    False
    >>> check_password2(2,9, "c", "ccccccccc")
    False
     """
    return (password[pos1-1] == letter) ^ (password[pos2-1] == letter)
     

counter1 = counter2 = 0

with open('day2.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=' ')
    for counts, letter, password in csv_reader:
        mincount, maxcount = counts.split('-')
        mincount, maxcount = int(mincount), int(maxcount)
        letter= letter[0]
        if check_password(mincount, maxcount, letter, password):
            counter1 += 1
        if check_password2(mincount, maxcount, letter, password):
            counter2 += 1
print(f"Part 1 \n There were {counter1} valid passwords \n")
print(f"Part 2 \n There were {counter2} valid passwords \n")