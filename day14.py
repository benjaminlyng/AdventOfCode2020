import numpy as np
import re

def mask_number(mask, number):
    """ mask number

    >>> mask_number('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 11)
    73
    >>> mask_number('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 101)
    101
    >>> mask_number('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 0)
    64
    """
    before_mask = np.zeros([len(mask)], dtype=int)
    num = np.array([i for i in bin(number)[2:]])
    before_mask[-len(num):] = num
    
    mask = mask.replace('X', '9')
    mask = np.array([i for i in mask], dtype=int)
    

    outnum = before_mask.copy()

    outnum[mask == 1] = 1
    outnum[mask == 0] = 0
    outnum = "".join([str(i) for i in outnum])
    return int(outnum,2)

mem = {}

with open('day14.txt', 'r') as f:
    for line in f:
        command, val = line.strip().split(' = ')
        if command == 'mask':
            mask = val
        else:
            p = command.replace('mem[','')
            p = p.replace(']','')
            mem[p] = mask_number(mask, int(val))

print(sum(i for i in mem.values()))