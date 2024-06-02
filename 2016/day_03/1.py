FILENAME = 'input.txt'

def func():
    count = 0
    with open(FILENAME) as f:
        for ln in f.read().split('\n'):
            a = [
                int(x) for x in ln.strip().split(' ') if x
            ]
            if (a[0] + a[1] > a[2]) and (a[1] + a[2] > a[0]) and (a[0] + a[2] > a[1]):
                count += 1
    print(count)


func()