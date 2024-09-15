FILENAME = 'input.txt'

def readfile():
    with open(FILENAME) as f:
        return f.read().strip()

def hash(input_string: str):
    numbers = [i for i in range(256)]
    current_pos = 0
    skip = 0
    as_ascii = [ord(c) for c in input_string]
    as_ascii += [17, 31, 73, 47, 23]
    for _ in range(64):
        for l in as_ascii:
            if l > len(numbers):
                continue
            end = current_pos + l
            if end > len(numbers):
                sub = numbers[current_pos:] + numbers[:end - len(numbers)]
                sub = sub[::-1]
                
                numbers = numbers[:current_pos] + sub
                trunc = numbers[256:]
                numbers = trunc + numbers[len(trunc):256]
            else:
                sub = numbers[current_pos:end][::-1]
                numbers = numbers[:current_pos] + sub + numbers[end:]
            
            current_pos = (end + skip) % len(numbers)
            skip += 1
    hash = []
    for i in range(16):
        ix = i*16
        s = numbers[ix:ix+16]
        v = 0
        for j in s:
            v ^= j
        h = hex(v)[2:]
        if len(h) == 1:
            h = '0' + h
        hash.append(h)
    return ''.join(hash)

def func():
    start = readfile() 
    res = 0
    for r in range(128):
        h = f'{start}-{r}'
        o = hash(h)
        
        for cc in o:
            bb = bin(int(cc, 16))[2:]
            for c in bb:
                if c == '1':
                    res += 1
    return res

print(func())
