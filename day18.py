import re
with open('day18.txt', 'r') as f:
    l = f.read().splitlines()

def do_math(homework:str):
    """ Do wierd math so that 
    >>> do_math('2 * 3 + (4 * 5)')
    '26'
    >>> do_math('5 + (8 * 3 + 9 + 3 * 4 * 3)')
    '437'
    >>> do_math('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))')
    '12240'
    >>> do_math('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')
    '13632'
    """
    
    if isinstance(homework, re.Match) :
        homework = homework.group()
        
    homework = re.sub(r'\([\d+* ]*\)', lambda x : do_math(x.group()[1:-1]), homework)
    
    homework = re.sub(r'\([\d+* ]*\)', do_math, homework)   
    homework = re.sub(r'^\d* [+*] \d*', lambda x: str(eval(x.group())), homework)
    homework = re.sub(r'^\d* [\d+* ]* \d*', lambda x: do_math(x.group()), homework)
    return homework

print(f"Part 1: {sum(int(do_math(i)) for i in l)=}")


def do_math2(homework:str):
    """ Do wierd math so that '+' evaluates before '*'

    >>> do_math2('2 * 3 + (4 * 5)')
    '46'
    >>> do_math2('5 + (8 * 3 + 9 + 3 * 4 * 3)')
    '1445'
    >>> do_math2('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))')
    '669060'
    >>> do_math2('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')
    '23340'
    """
    
    if isinstance(homework, re.Match) :
        homework = homework.group()
    # print(homework)
    
    homework = re.sub(r'\([\d+* ]*\)', lambda x : do_math2(x.group()[1:-1]), homework)
    
    homework = re.sub(r'\([\d+* ]*\)', do_math2, homework)   
    homework = re.sub(r'\d+ [+] \d+', lambda x: str(eval(x.group())), homework)
    homework = re.sub(r'\d+ [\d+ ]+ \d+', lambda x: do_math2(x.group()), homework)

    homework = re.sub(r'\d+ [*] \d+', lambda x: str(eval(x.group())), homework)
    homework = re.sub(r'\d+ [\d* ]+ \d+', lambda x: do_math2(x.group()), homework)
    return homework

print(f"Part 2: {sum(int(do_math2(i)) for i in l)=}")
