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

def replacer(starter):
    matcher = build_matcher()
    
    res = (starter,  1)
    while res[1]:
        res = re.subn(matcher, '', res[0])
        
    return res[0], len(res[0])

def main():
    polymer = readfile()

    alpha = [c for c in range(ord('a'), ord('a') + 26)]
    min_size = len(polymer)
    best_chara = None
    for a in alpha:
        test = polymer.replace(chr(a), '')
        test = test.replace(chr(a).upper(), '')

        res, size = replacer(test)
        if size < min_size:
            min_size = size
            best_chara = a
    return min_size


print(main())