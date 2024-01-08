FILENAME = 'input.txt'

def read_file():
    with open(FILENAME) as f:
        return [ln.strip().split('x') for ln in f.read().split('\n')]
    
def surface_area_and_slack(dimensions):
    l, w, h = dimensions
    l = int(l)
    w = int(w)
    h = int(h)

    s1 = l * w
    s2 = w * h
    s3 = l * h

    slack = min([s1,s2,s3])

    surface_area = 2*(s1 + s2 + s3)
    return surface_area + slack

def func():
    tot = 0
    dat = read_file()
    for d in dat:
        tot += surface_area_and_slack(d)
    print(tot)

func()