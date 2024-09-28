FILENAME = 'input.txt'

def readfile():
    with open(FILENAME) as f:
        return [ln.strip().split(' ') for ln in f.read().split('\n')]

# b = k, c = k + (m * 17) k matters 
# multi // h val (K = 5)
# 40 34
# 35 30
# 34 29
# 20 16
# 10 8
# 2  2
def func():
    reg = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0
    }
    ix = 0

    instructions = readfile()
    count = 0
    while ix >= 0 and ix < len(instructions):
        inst = instructions[ix]
        
        cmd = inst[0]
        if cmd == 'set':
            if inst[2].isalpha():
                reg[inst[1]] = reg[inst[2]]
            else:
                reg[inst[1]] = int(inst[2])
        if cmd == 'sub':
            if inst[2].isalpha():
                reg[inst[1]] -= reg[inst[2]]
            else:
                reg[inst[1]] -= int(inst[2])
        if cmd == 'mul':
            count += 1
            if inst[2].isalpha():
                reg[inst[1]] *= reg[inst[2]]
            else:
                reg[inst[1]] *= int(inst[2])
        if cmd == 'jnz':
            if inst[1].isalpha():
                v = reg[inst[1]]
            else:
                v = int(inst[1])
            if v != 0:
                if inst[2].isalpha():
                    ix += reg[inst[2]]
                else:
                    ix += int(inst[2])
                continue
        ix += 1
        print(reg)
    return count

print(func())
            