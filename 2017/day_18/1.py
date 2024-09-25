FILENAME = 'input.txt'

def readfile():
    res = []
    with open(FILENAME) as f:
        for ln in f.read().split('\n'):
            res.append(ln.strip().split(' '))
    return res

from collections import defaultdict
def func():
    reg = defaultdict(int)
    inst = readfile()
    sound = 0
    ix = 0
    while ix < len(inst) and ix >= 0:
        i = inst[ix]
        cmd = i[0]
        
        if cmd == 'snd':
            try:
                sound = int(i[1])
            except:
                sound = reg[i[1]]
        if cmd == 'set':
            try:
                reg[i[1]] = int(i[2])
            except:
                reg[i[1]] = reg[i[2]]
        if cmd == 'add':
            try:
                reg[i[1]] += int(i[2])
            except:
                reg[i[1]] += reg[i[2]]
        if cmd == 'mul':
            try:
                reg[i[1]] *= int(i[2])
            except:
                reg[i[1]] *= reg[i[2]]
        if cmd == 'mod':
            try:
                reg[i[1]] = reg[i[1]] % int(i[2])
            except:
                reg[i[1]] = reg[i[1]] % reg[i[2]]
        if cmd == 'rcv':
            v = 0
            
            try:
                v = int(i[1])
            except:
                v = reg[i[1]]
            if v != 0:
                return sound
        if cmd == 'jgz':
            try:
                x = int(i[1])
            except:
                x = reg[i[1]]
            try:
                y = int(i[2])
            except:
                y = reg[i[2]]
            
            if x > 0:
                ix += y
                continue
        ix += 1



print(func())