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

def main():
    ru, pn = readfile()
    
    mid = 0

    for p in pn:
        if is_ordered(ru, p):
            mid += p[len(p)//2]
    return mid

print(main())