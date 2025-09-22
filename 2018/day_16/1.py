def readfile():
    re = []
    with open('input_1.txt') as f:
        for blob in f.read().split('\n\n'):
            before, inst, after = blob.rstrip('\n').split('\n')
            before = [int(x) for x in before.strip().split(':')[1].strip()[1:-1].split(',')]
            inst = [int(x.strip()) for x  in inst.strip().split(' ')]
            after = [int(x) for x in after.strip().split(':')[1].strip()[1:-1].split(',')]
            re.append((before, inst, after))
    return re

def addr(b, inst):
    reg = {r: b[r] for r in range(4)}
    code, i0, i1, out = inst
    reg[out] = reg[i0] + reg[i1]
    return list(reg.values())

def addi(b, inst):
    reg = {r: b[r] for r in range(4)}
    code, i0, i1, out = inst
    reg[out] = reg[i0] + i1
    return list(reg.values())

def mulr(b, inst):
    reg = {r: b[r] for r in range(4)}
    code, i0, i1, out = inst
    reg[out] = reg[i0] * reg[i1]
    return list(reg.values())

def muli(b, inst):
    reg = {r: b[r] for r in range(4)}
    code, i0, i1, out = inst
    reg[out] = reg[i0] * i1
    return list(reg.values())

def banr(b, inst):
    reg = {r: b[r] for r in range(4)}
    code, i0, i1, out = inst
    reg[out] = reg[i0] & reg[i1]
    return list(reg.values())


def bani(b, inst):
    reg = {r: b[r] for r in range(4)}
    code, i0, i1, out = inst
    reg[out] = reg[i0] & i1
    return list(reg.values())

def borr(b, inst):
    reg = {r: b[r] for r in range(4)}
    code, i0, i1, out = inst
    reg[out] = reg[i0] | reg[i1]
    return list(reg.values())
    
def bori(b, inst):
    reg = {r: b[r] for r in range(4)}
    code, i0, i1, out = inst
    reg[out] = reg[i0] | i1
    return list(reg.values())

def setr(b, inst):
    reg = {r: b[r] for r in range(4)}
    code, i0, i1, out = inst
    reg[out] = reg[i0]
    return list(reg.values())

def seti(b, inst):
    reg = {r: b[r] for r in range(4)}
    code, i0, i1, out = inst
    reg[out] = i0
    return list(reg.values())

def gtir(b, inst):
    reg = {r: b[r] for r in range(4)}
    code, i0, i1, out = inst
    if i0 > reg[i1]:
        reg[out] = 1
    else:
        reg[out] = 0
    return list(reg.values())

def gtri(b, inst):
    reg = {r: b[r] for r in range(4)}
    code, i0, i1, out = inst
    if reg[i0] > i1:
        reg[out] = 1
    else:
        reg[out] = 0
    return list(reg.values())

def gtrr(b, inst):
    reg = {r: b[r] for r in range(4)}
    code, i0, i1, out = inst
    if reg[i0] > reg[i1]:
        reg[out] = 1
    else:
        reg[out] = 0
    return list(reg.values())

def eqir(b, inst):
    reg = {r: b[r] for r in range(4)}
    code, i0, i1, out = inst
    if i0 == reg[i1]:
        reg[out] = 1
    else:
        reg[out] = 0
    return list(reg.values())

def eqri(b, inst):
    reg = {r: b[r] for r in range(4)}
    code, i0, i1, out = inst
    if reg[i0] == i1:
        reg[out] = 1
    else:
        reg[out] = 0
    return list(reg.values())

def eqrr(b, inst):
    reg = {r: b[r] for r in range(4)}
    code, i0, i1, out = inst
    if reg[i0] == reg[i1]:
        reg[out] = 1
    else:
        reg[out] = 0
    return list(reg.values())


def main():
    # How many samples behave like GTE 3 opcodes
    samples = readfile()
    op_calls = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
    more_than_three = 0
    for b, i, a in samples:
        # For each before, if try all operations that work
        # Increment the ones that do
        ct = 0
        for o in op_calls:
            result = o(b, i)
            if result == a:
                ct += 1
        if ct >= 3:
            more_than_three += 1
    return more_than_three
        
print(main())