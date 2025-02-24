import re

def readfile():
    with open('input.txt') as f:
        return f.read().strip()
    
def build_matcher():
    a = ord('a')
    s = []
    for ch in range(26):
        ltr = ch + a
        ln = chr(ltr) + chr(ltr).upper()
        s.append(ln)
        s.append(ln[::-1])
    return '|'.join(s)

def main():
    polymer = readfile()

    matcher = build_matcher()
    
    res = (polymer,  1)
    while res[1]:
        res = re.subn(matcher, '', res[0])
        print(res)
        
    return res[0], len(res[0])





print(main())