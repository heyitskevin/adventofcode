import copy

def readfile():
    rules = []
    page_numbers = []
    with open('rules.txt') as r:
        for ln in r.read().split('\n'):
            rules.append([int(x) for x in ln.strip().split('|')])
    with open('numbers.txt') as n:
        for ln in n.read().split('\n'):
            page_numbers.append([
                int(x) for x in ln.strip().split(',')
            ])
    return rules, page_numbers


def is_ordered(rules, pages):
    for before, after in rules:
        try:
            b_ix = pages.index(before)
        except ValueError as ve:
            b_ix = -1
        try:
            a_ix = pages.index(after)
        except ValueError as ve:
            a_ix = -1
        if a_ix >= 0 and b_ix >= 0:
            if a_ix < b_ix:
                return False
    return True


def getmid(rules, pages):
    ls = {}
    rs = {}
    # for every element in the list
    # get all its lefts and rights
    # find all the lefts and rights in the list
    # midpoint is when they're equal length
    # don't even need to order the array
    for elem in pages:
        l, r = [], []
        for left, right in rules:
            if elem == left and right in pages:
                r.append(right)
            elif elem == right and left in pages:
                l.append(left)
        ls[elem] = l
        rs[elem] = r
    
    for elem in pages:
        if len(ls[elem]) == len(rs[elem]):
            assert not len(set(ls[elem]).intersection(set(rs[elem])))
            return elem
    
    return -1

def main():
    ru, pn = readfile()
    
    mid = 0
    
    for p in pn:
        if not is_ordered(ru, p):
            mm = getmid(ru, p)
            if mm == -1:
                assert False
            mid += mm
    return mid

print(main())
