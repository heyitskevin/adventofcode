import re

FILENAME = 'input.txt'

def read_file():
    with open(FILENAME) as f:
        return f.read().strip()
    
def decompress(line):
    r = r'\(\d+x\d+\)'
    count = 0
    x = re.search(r, line)
    while x:
        if x.start() != 0:
            count += x.start()
        n, mult = line[x.start()+1:x.end()-1].split('x')
        count += int(n) * int(mult)
        line = line[x.end() + int(n):]
        x = re.search(r, line)
    return count
    
    
    

def func():
    line = read_file()
    count = decompress(line)
    print(count)

func()