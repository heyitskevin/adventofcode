FILENAME = 'input.txt'

def read_file():
    with open(FILENAME) as f:
        return [ln for ln in f.read().split('\n')]
    
def is_tls(test):
    in_brack = False
    has_abba = False
    for i in range(len(test) - 3):
        if test[i] == '[':
            in_brack = True
        if test[i] == ']':
            in_brack = False
        lookahead = test[i:i+4]
        if lookahead == lookahead [::-1] and lookahead[0] != lookahead[1] and in_brack:
            return 0
        if lookahead == lookahead [::-1] and lookahead[0] != lookahead[1] and not in_brack:
            has_abba = True
    
    if has_abba:
        return 1
    else:
        return 0

def func():
    data = read_file()
    s = 0
    for d in data:
        s += is_tls(d)
    print(s)

func()