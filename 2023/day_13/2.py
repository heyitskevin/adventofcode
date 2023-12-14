FILENAME = 'input.txt'

def read_file():
    with open(FILENAME) as f:
        return [[list(ln.strip()) for ln in blck.split('\n')]for blck in f.read().split('\n\n')]

def transpose(arr):
    # short circuits at shortest nested list if table is jagged:
    return list(map(list, zip(*arr)))

def reflect(arr):
    res = []
    for ix in range(len(arr)-1):
        c_ix = ix
        curr = arr[c_ix]
        m_ix = ix + 1
        mirror = arr[m_ix]
        while curr == mirror:
            c_ix = c_ix - 1
            m_ix = m_ix + 1
            if c_ix < 0 or m_ix >= len(arr):
                res.append(ix + 1)
                break
            curr = arr[c_ix]
            mirror = arr[m_ix]
    return res

def get_reflections(arr):
    trans = transpose(arr)
    res = []
    r = reflect(arr)
    if r:
        res.append((r, 'rows'))
    c = reflect(trans)
    if c:
        res.append((c, 'cols'))
    return res

import copy

def smudge_reflection(base_arr):
    base = get_reflections(base_arr).pop(0)
    
    for ix in range(len(base_arr)):
        for ixx in range(len(base_arr[0])):
            smudge = copy.deepcopy(base_arr)
            smudge[ix][ixx] = '#' if smudge[ix][ixx] == '.' else '.'
            all_reflections = get_reflections(smudge)
            for refl in all_reflections:
                if len(refl[0]) > 1:
                    for elem in refl[0]:
                        test_refl = ([elem], refl[1])
                        if test_refl and test_refl != base:
                            return (test_refl[0][0], test_refl[1])
                if refl and (refl != base):
                    return (refl[0][0], refl[1])


def func(): 
    rocks = read_file()
    summary = 0
    for r in rocks:
        ct, direction = smudge_reflection(r)
        if direction == 'rows':
            ct = 100 * ct
        summary += ct
    print(summary)
    
func()
