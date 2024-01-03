FILENAME = 'input.txt'

def read_file():
    with open(FILENAME) as f:
        return [
            [int(a) for a in ln.strip().split('x')] for ln in f.read().split('\n')
        ]
    
def get_ribbon(dims):
    l, w, h = dims
    shortest, sec_shortest = sorted(dims)[:2]
    perim = 2*(shortest + sec_shortest)
    vol = l*w*h

    return perim + vol


def func():
    dat = read_file()
    tot = 0
    for d in dat:
        tot += get_ribbon(d)
    print(tot)

func()