from collections import Counter

FILENAME = 'input.txt'

def read_file():
    with open(FILENAME) as f:
        return [
            ln for ln in f.read().split('\n') if ln
        ]
    
def validate(test_str):
    tokens = test_str.split('-')
    last = tokens.pop(-1)
    c = Counter(''.join(tokens))
    checksum = last.split('[')[-1][:-1]
    c_list = sorted(list(c.most_common()), key=lambda x: (-x[1], x[0]))

    for ix, ch in enumerate(checksum):
        if ch != c_list[ix][0]:
            return 0
    return int(last.split('[')[0])

def func():
    s = read_file()
    t = 0
    for i in s:
        t += validate(i)
    print(t)

func()