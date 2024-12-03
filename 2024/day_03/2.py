import re
def readfile():
    with open('input.txt') as f:
        return f.read().strip()


def main():
    data = readfile()
    m = 0
    s = re.finditer(r"(mul\(\d+,\d+\))|(do\(\))|(don't\(\))", data)
    dodont = True
    for i in s:
        mul, do, dont  = i.groups()
        if mul is not None:
            if dodont:
                a, b = mul.split('(')[1][:-1].split(',')
                m += int(a) * int(b)
        if do is not None:
            dodont = True
        if dont is not None:
            dodont = False
            
    return m

print(main())