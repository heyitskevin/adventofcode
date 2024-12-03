import re

def readfile():
    with open('input.txt') as f:
        return f.read().strip()

def main():
    a = readfile()
    elems = re.findall(r'mul\(\d+,\d+\)', a)
    m = 0
    for e in elems:
        x, y = e.split('(')[1].split(',')
        m += int(x) * int(y[:-1])
    return m
print(main())