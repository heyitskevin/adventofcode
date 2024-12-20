def readfile():
    with open('input.txt') as f:
        return [x for x in f.read().strip().split(' ')]


def blink(st):
    new_stones = []
    for s in st:
        if s == '0':
            new_stones.append('1')
        elif len(s) % 2 == 0:
            new_stones.append(str(int(s[:len(s)//2])))
            new_stones.append(str(int(s[len(s)//2:])))
        else:
            new_stones.append(str(int(s) * 2024))
    return new_stones
        

def main():
    stones = readfile()
    for _ in range(25):
        stones = blink(stones)
    return len(stones)

print(main())
    