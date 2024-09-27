FILENAME = 'input.txt'

def readfile():
    res = []
    with open(FILENAME) as f:
        for ln in f.read().split('\n'):
            a = []
            for v in ln.split(', '):
                a.append(
                    [int(x) for x in v.split('=')[1][1:-1].split(',')]
                )
            res.append(a)
    return res

def func():
    d = readfile()
    valid = []
    mindist = 99999999999
    minid = -1
    big_time = 10000
    for bigtime in [100, 1000, 10000, 1000000, 1000000]:
        for pid, data in enumerate(d):
            p, v, a = data
            x = p[0] + (v[0] * big_time) + (a[0] * big_time * big_time)
            y = p[1] + (v[1] * big_time) + (a[1] * big_time * big_time)
            z = p[2] + (v[2] * big_time) + (a[2] * big_time * big_time)

            mdist = abs(x) + abs(y) + abs(z)
            if mdist < mindist:
                minid = pid
                mindist = mdist
        print(minid, mindist)

    return minid, mindist

print(func())