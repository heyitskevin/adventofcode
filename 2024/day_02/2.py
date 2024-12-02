def readfile():
    res = []
    with open('input.txt') as f:
        for ln in f.read().split('\n'):
            res.append([int(x) for x in ln.strip().split(' ')])
    return res

def is_safe(arr):
    inc = False
    dec = False
    s = sorted(arr)
    if arr == s:
        inc = True
    if arr == s[::-1]:
        dec = True
    safe = False
    if inc or dec:
        for ix, elem in enumerate(arr):
                if ix == len(arr) - 1:
                    continue
                nxt = arr[ix + 1]
                diff = abs(elem - nxt)
                if diff > 3 or diff < 1:
                    safe = False
                    break
                else:
                    safe = True
    return safe

def main():
    f = readfile()
    safe = 0
    for report in f:
        if is_safe(report):
            safe += 1
            continue
        else:
            for ix in range(len(report)):
                if is_safe(report[:ix]+report[ix+1:]):
                    safe += 1
                    break
        
    return safe

print(main())