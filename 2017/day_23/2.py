FILENAME = 'input.txt'

def readfile():
    with open(FILENAME) as f:
        return [ln.strip().split(' ') for ln in f.read().split('\n')]
    
import math
def func():
    b = 105700
    c = 122700
    step = 17
    h = 0
    for bb in range(b, c+1, step):
        for i in range(2, math.isqrt(bb) + 1):
            if bb % i == 0:
                h += 1
                break
    return h

print(func())