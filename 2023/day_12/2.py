FILENAME = 'input.txt'

def read_input():
    with open(FILENAME) as f:
        return [(x[0], tuple([int(y) for y in x[1].split(',')])) for x in [ln.strip().split(' ') for ln in f]]

def unfold_data(data):
    return [
        ((elem[0]+'?') * 4 + elem[0], elem[1] * 5) for elem in data
    ]

from functools import cache

@cache
def cached_recursive(springs, groups):
    springs = springs.lstrip('.') # Don't care leading dots
    if springs == '':
        return 1 if not groups else 0
    if not groups:
        return int(springs.find('#') == -1)
    
    if springs[0] == '#':
        if len(springs) < groups[0] or '.' in springs[:groups[0]]:
            return 0
        elif len(springs) == groups[0]:
            return 1 if len(groups) == 1 else 0
        elif springs[groups[0]] == '#':
            return 0
        else:
            return cached_recursive(springs[groups[0] + 1:], groups[1:])
    s = cached_recursive('#' + springs[1:], groups) + cached_recursive(springs[1:], groups)
    return(s)

def func():
    data = read_input()
    new_data = unfold_data(data)
    tot = 0
    for [springs, groups] in new_data:
        tot += cached_recursive(springs, groups)
    print(tot)

func()