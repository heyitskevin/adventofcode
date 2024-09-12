FILENAME = 'input.txt'

def read_file():
    with open(FILENAME) as f:
        return f.read().split('\n')
    
def func():
    registers = {}
    mv = 0
    f = read_file()
    for ln in f:
        cmd, cond = ln.split(' if ')
        reg, op, v = cmd.strip().split(' ')
        v = int(v)
        left, ev, right = cond.strip().split(' ')
        
        left = registers.get(left, 0)
        right = int(right)
        b = False
        if ev == '<':
            b = left < right
        if ev == '>':
            b = left > right
        if ev == '>=':
            b = left >= right
        if ev == '<=':
            b = left <= right
        if ev == '==':
            b = left == right
        if ev == '!=':
            b = left != right
        if b:
            reg_val = registers.get(reg, 0)
            sign = 1 if op == 'inc' else -1
            reg_val = reg_val + (sign * v)
            registers[reg] = reg_val
            mv = max(mv, reg_val)
    return mv


print(func())