FILENAME = 'input.txt'
from itertools import product
import re

def read_file():
    expr = r'([0-9]*,[0-9]*)'
    with open(FILENAME) as f:
        return [(inst, re.findall(expr, inst)) for inst in f.read().split('\n')]
    
def func():
    instructions = read_file()
    lights(instructions)

def lights(instructions):
    coords = {k: 0 for k in product(range(0,1000), range(0,1000))}
    for inst in instructions:
        cmd = inst[0]
        first, second = inst[1]
        f_r, f_c = [int(a) for a in first.split(',')]
        s_r, s_c = [int(b) for b in second.split(',')]
        switches = product(range(f_r, s_r+1), range(f_c, s_c+1))

        if 'turn on' in cmd:
            for x in switches:
                coords[x] += 1
        elif 'turn off' in cmd:
            for x in switches:
                if coords[x] > 0:
                    coords[x] -= 1
                else:
                    coords[x] = 0
        elif 'toggle' in cmd:
            for x in switches:
                coords[x] += 2
    
    print('tot', sum(coords.values()))
    

func()