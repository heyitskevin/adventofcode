FILENAME = 'input.txt'

import re

def read_file():
    with open(FILENAME) as f:
       return [ln for ln in f.read().split('\n')]
    
def func():
    strings = read_file()
    tot = 0
    chara = ['\\', '"']
    for s in strings:
        ct = 2
        for ch in s:
            if ch in chara:
                ct += 1
        tot += ct
    print(tot)
        

func()