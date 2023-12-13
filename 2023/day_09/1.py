FILENAME = 'input.txt'

def read_input():
    r = []
    with open(FILENAME) as f:
        for ln in f:
            r.append([int(x) for x in ln.strip().split(' ')])
    return r

def get_next_val(row):
    pile = [row]
    while any(pile[-1]):
        nxt = []
        for ix, v in enumerate(pile[-1]):
            if ix == len(pile[-1]) - 1:
                continue
            nxt.append(pile[-1][ix+1] - v)
        pile.append(nxt)
    n_val = sum([p[-1] for p in pile])
    return n_val



def func():
    # naievely process
    tot = 0
    rows = read_input()
    for r in rows:
        tot += get_next_val(r)
    print(tot)


func()
