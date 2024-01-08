FILENAME = 'input.txt'
import re


def read_file():
    with open(FILENAME) as f:
        return  [ln.strip() for ln in f.read().split('\n')]
    

def is_nice(word):
    count_double = r'(\w\w).*?(\1)'
    if not re.search(count_double, word):
        return False
    one_between = r'(\w).{1}(\1)'
    if not re.search(one_between, word):
        return False
    return True

def func():
    words = read_file()
    c = 0
    for w in words:
        if is_nice(w):
            c += 1
    print('nice', c)

func()
    