FILENAME = 'input.txt'
from collections import Counter

def read_file():
    with open(FILENAME) as f:
        return [ln.strip() for ln in f.read().split('\n')]
    
def get_min_occ(signals):
    buckets = [Counter() for _ in signals[0]]
    
    for s in signals:
        for ix, v in enumerate(s):
            if v in buckets[ix]:
                buckets[ix][v] += 1
            else:
                buckets[ix][v] = 1
    char_candidates = []
    for b in buckets:
        c = ''
        mm = len(signals)
        for k, v in b.items():
            if mm > v:
                mm = v
                c = k
        char_candidates.append(c)
    return ''.join(char_candidates)

def func():
    dat = read_file()
    x = get_min_occ(dat)
    print(x)

func()