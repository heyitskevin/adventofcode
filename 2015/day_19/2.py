import re


REPLACEMENTS = 'replacements.txt'
MEDICINE = 'medicine.txt'

def read_requirements():
    with open(REPLACEMENTS) as f_r:
        r = f_r.read().split('\n')
        d = {}
        for ln in r:
            k, v = ln.split('=>')
            d[v.strip()] = k.strip()
    return d

def read_medicine():
    with open(MEDICINE) as f_m:
        return f_m.read().strip()
    
def count_elements(input):
    c = 0
    for ix in range(len(input)-1):
        n = input[ix+1]
        if n.isupper():
            c += 1
    if input[0].isupper():
        c += 1
    return c

def func():
    med = read_medicine()
    # Insight from reddit is as follows
    # There are two types of molecule transforms
    # one molecule -> two molecules
    # one molecule -> X Rn X Ar or X Rn X Y X Ar or X Rn X Y X Y X Ar
    # Note that can interpret Rn Ar and Y as characters ( ) and , respectively
    # It then becomes formulaic to derive the min number of steps
    # There is only one solution to this problem so the min is also the only
    left_parens = len(re.findall('Rn', med))
    print(re.findall('Rn', med))
    print(re.findall('Ar', med))
    print(re.findall('Y', med))
    right_parens = len(re.findall('Ar', med))
    commas = len(re.findall('Y', med))

    num_tokens = count_elements(med)

    res = num_tokens - left_parens - right_parens - 2*commas - 1
    print(res)
    
func()
        