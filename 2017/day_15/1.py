FILENAME = 'modified_input.txt'
A_FACTOR = 16807
B_FACTOR = 48271
DIVISOR = 2147483647

def read_file():
    with open(FILENAME) as f:
        return [int(x) for x in f.read().split('\n')]
    

def func():
    a, b = read_file()
    pairs = 0

    for _ in range(40000000):
        bin_a = bin(a)[2:]
        bin_b = bin(b)[2:]
        if len(bin_a) < 16:
            for i in range(16-len(bin_a)):
                bin_a = '0' + bin_a
        if len(bin_b) < 16:
            for i in range(16 - len(bin_b)):
                bin_b = '0' + bin_b
        
        if bin_a[-16:] == bin_b[-16:]:
            pairs += 1
        a = (a * A_FACTOR) % DIVISOR
        b = (b * B_FACTOR) % DIVISOR

    return pairs

print(func())