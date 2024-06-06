FILENAME = 'input.txt'

def read_file():
    with open(FILENAME) as f:
        return [
            ln for ln in f.read().split('\n') if ln
        ]
    
def decrypt(ln):
    tokens = ln.split('-')
    last = tokens.pop(-1)
    checksum = last.split('[')[-1][:-1]
    shift = int(last.split('[')[0]) % 26
    a = ord('a')
    z = ord('z')
    s = ''
    for i in ' '.join(tokens):
        if i != ' ': 
            shifted = ord(i) + shift
            if shifted > z:
                shifted = (shifted - z) + a - 1
            shifted = chr(shifted)
        else:
            shifted = ' '
        s += shifted
    if 'north' in s:
        print(s, last)

def func():
    dat = read_file()
    for l in dat:
        decrypt(l)


func()