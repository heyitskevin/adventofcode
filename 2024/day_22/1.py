def readfile():
    with open('input.txt') as f:
        return [int(x) for x in f.read().split('\n')]
    

def do_op(n):
    x = n
    for _ in range(2000):
        m = x * 64
        x = m ^ x
        x =  x % 16777216

        d = x // 32
        x = d ^ x
        x = x % 16777216

        t = x * 2048
        x = t ^ x
        x = x % 16777216
    return x


def main():
    d = readfile()
    res = 0
    for c in d:
        res += do_op(c)
    
    return res

print(main())

