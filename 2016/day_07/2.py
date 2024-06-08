FILENAME = 'input.txt'

def read_file():
    with open(FILENAME) as f:
        return [ln for ln in f.read().split('\n')]
    
def is_ssl(test):
    a = set()
    b = set()

    in_brack = False

    for i in range(len(test) - 2):
        if test[i] == '[':
            in_brack = True
        if test[i] == ']':
            in_brack = False
        lookahead = test[i:i+3]
        if lookahead[0] == lookahead[2] and lookahead[0] != lookahead[1]:
            if in_brack:
                b.add(lookahead)
            else:
                a.add(lookahead)
    if len(a) == 0:
        return 0
    else:
        for aa in a:
            if f"{aa[1]}{aa[0]}{aa[1]}" in b:
                return 1
    return 0

def func():
    data = read_file()
    s = 0
    for d in data:
        s += is_ssl(d)
    print(s)

func()