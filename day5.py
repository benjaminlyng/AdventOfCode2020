import math

with open('day5.txt', 'r') as day5:
        bps = day5.read().splitlines()

def get_row_col(maxseat: int, seq : str):
    """convert string sequence to either row or column number

    >>> get_row_col(127, 'FBFBBFF')
    44
    >>> get_row_col(127, 'BFFFBBF')
    70
    >>> get_row_col(7, 'RLR')
    5
    """
    minseat=0
    for l in seq:
        mean = (maxseat+minseat)/2
        if l in ('F', 'L'):
            maxseat =  math.floor(mean)
        elif l in ('B', 'R'):
            minseat = math.ceil(mean)
    if l in ('F', 'L'):
        return minseat
    elif l in ('B', 'R'):
        return maxseat
    return f"{maxseat=} != {minseat=}"

def read_bp(bp):
    """ read boarding pass and output seat row, column and ID

    BFFFBBFRRR: row 70, column 7, seat ID 567.
    FFFBBBFRRR: row 14, column 7, seat ID 119.
    BBFFBBFRLL: row 102, column 4, seat ID 820.

    >>> read_bp('BFFFBBFRRR')
    [70, 7, 567]
    """
    row = bp[0:7]
    col = bp[7:10]
    #print(row, col)
    rownr = get_row_col(127, row)
    colnr = get_row_col(7, col)
    idnr = rownr * 8 + colnr

    return [rownr, colnr, idnr]
full_list= [read_bp(bp) for bp in bps]
max_id= max(bp[2] for bp in bps)
print(f"Part 1 \n {max_id=}")


full_list.sort()
taken_seats = [[x[0], x[1]] for x in full_list]
total = [[x, y] for x in range(127) for y in range(8)]
for row, col in total:
    if [row, col] not in taken_seats:
        print(row, col)


print(f"Part 1 \n My seat {69*8 + 2=}")
