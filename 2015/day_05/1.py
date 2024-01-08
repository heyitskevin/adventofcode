FILENAME = 'input.txt'
from collections import Counter
def read_file():
    with open(FILENAME) as f:
        return  [ln.strip() for ln in f.read().split('\n')]
    
def is_nice(word):
    for e in ['ab', 'cd', 'pq', 'xy']:
        if e in word:
            return False
    
    c = Counter(word)
    vows = 0
    for v in ['a', 'e', 'i', 'o', 'u']:
        vows += c[v]
    if vows < 3:
        return False
    
    for ix, ch  in enumerate(word):
        if ix == len(word) - 1:
            return False
        else:
            if word[ix+1] == ch:
                break
    return True

def func():
    words = read_file()
    nice = 0
    for w in words:
        if is_nice(w):
            nice += 1
    print('nice', nice)


func()