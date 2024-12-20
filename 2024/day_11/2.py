def readfile():
    with open('input.txt') as f:
        return [x for x in f.read().strip().split(' ')]
    
from functools import cache
# cached recursion my beloved
@cache
def recur(s, b):
    if b == 0:
        return 1
    if int(s) == 0:
        return recur("1", b - 1)
    elif len(s) % 2 == 0 and int(s) != 0:
        left = str(int(s[:len(s) // 2]))
        right = str(int(s[len(s) // 2:]))
        return recur(left, b - 1) + recur(right, b - 1)
    else:
        return recur(str(int(s) * 2024), b - 1)

def main():
    stones = readfile()
    tot = 0
    
    for stone in stones:
        tot += (recur(stone, 75))
    return tot


print(main())