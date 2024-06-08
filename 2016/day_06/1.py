FILENAME = 'input.txt'
from collections import Counter

def read_file():
    with open(FILENAME) as f:
        return [ln.strip() for ln in f.read().split('\n')]
    
def get_max_occ(signals):
    buckets = [Counter() for _ in signals[0]]
    char_candidates = ['!' for _ in signals[0]] # Just init it to a non alphabetic chara
    for s in signals:
        for ix, v in enumerate(s):
            if v in buckets[ix]:
                buckets[ix][v] += 1
            else:
                buckets[ix][v] = 1
            if buckets[ix].get(char_candidates[ix], 0) < buckets[ix].get(v):
                char_candidates[ix] = v
    return ''.join(char_candidates)

def func():
    dat = read_file()
    x = get_max_occ(dat)
    print(x)

func()