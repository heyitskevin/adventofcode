import re

FILENAME = 'input.txt'

def read_file():
    with open(FILENAME) as f:
        return f.read().strip()
    
def decompress(line):
    r = r'\(\d+x\d+\)'
    count = 0
    hnxt = re.search(r, line)
    while hnxt:
        count += hnxt.start()
        seq, mult = [int(l) for l in line[hnxt.start() + 1:hnxt.end() - 1].split('x')]
        
        chunk_size = decompress(line[hnxt.end():hnxt.end()+seq])
        count += chunk_size * mult
        line = line[hnxt.end() + seq:]
        hnxt = re.search(r, line)
    if count == 0 and not hnxt and len(line) > 0:
        count = len(line)
    return count

def func():
    line = read_file()
    count = decompress(line)
    print(count)

func()