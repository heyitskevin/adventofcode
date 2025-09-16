def readfile():
    initial_state = ''
    rules = []

    with open('input.txt') as f:
        for ln in f.readlines():
            if 'initial' in ln:
                initial_state = ln.split(':')[1].strip()
            elif '=>'  in ln:
                rules.append(ln.strip().split(' => '))

    return initial_state, rules

def refined_rules(raw_rules):
    ref = []
    for r1, r2 in raw_rules:
        r2 = r1[:2] + r2 + r1[3:]
        ref.append((r1, r2))
    return ref

def dict_rules(raw_rules):
    d = {}
    for r1, r2 in raw_rules:
        d[r1] = r2
    return d

def main():
    curr, rules = readfile()
    d = dict_rules(rules)
    # r_rules = refined_rules(rules)
    generations = 201
    affix = '.' * generations
    curr = affix + curr + affix
    for _ in range(generations):
        next_state = list(curr)
        for ix, v in enumerate(curr):
            if ix == 0:
                ll = '..'
                rr = curr[ix + 1 : ix + 3]
            elif ix == 1:
                ll = '.' + curr[0]
                rr = curr[ix + 1 : ix + 3]
            elif ix == len(curr) - 2:
                ll = curr[ix - 2 : ix]
                rr = curr[-1] + '.'
            elif ix == len(curr) - 1:
                ll = curr[ix - 2 : ix]
                rr = '..'
            else:
                ll = curr[ix - 2 : ix]
                rr = curr[ix + 1 : ix + 3]
            test_v = ll + v + rr
            flip = d.get(test_v, None)
            if flip is not None:
                next_state[ix] = flip
        curr = ''.join(next_state)
        print(curr)
    score = 0
    for ix, pot in enumerate(curr):
        if pot == '#':
            score += (ix - len(affix))
    
    print(score)



main()