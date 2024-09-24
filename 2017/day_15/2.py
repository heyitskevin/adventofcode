FILENAME = 'modified_input.txt'
A_FACTOR = 16807
B_FACTOR = 48271
DIVISOR = 2147483647

def read_file():
    with open(FILENAME) as f:
        return [int(x) for x in f.read().split('\n')]

def make_a(start):
    res = []
    a = start
    while len(res) < 5000000:
        bin_a = bin(a)[2:].zfill(16)
        if bin_a[-2:] == '00':
            res.append(bin_a)
        a = (a * A_FACTOR) % DIVISOR
    return res

def make_b(start):
    res = []
    b = start
    while len(res) < 5000000:
        bin_b = bin(b)[2:].zfill(16)
        if bin_b[-3:] == '000':
            res.append(bin_b)
        b = (b * B_FACTOR) % DIVISOR
    return res

def func():
    a, b = read_file()
    pairs = 0

    aa = make_a(a)
    print('a done')
    bb = make_b(b)
    print('b done')
    for ix in range(len(aa)):
        if aa[ix][-16:]  == bb[ix][-16:]:
            pairs += 1
    return pairs

print(func())