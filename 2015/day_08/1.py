FILENAME = 'input.txt'

import re

def read_file():
    with open(FILENAME) as f:
       return [ln for ln in f.read().split('\n')]
            
            
def get_literals(s):
    return len(s)

def func():
    strings = read_file()
    tot = 0
    for s in strings:
        # print('--------')
        lit = get_literals(s)
        mm = len(eval(s))
        v = lit - mm
        tot += v
    print(tot)
func()
