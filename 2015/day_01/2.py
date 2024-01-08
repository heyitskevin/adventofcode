with open('input.txt') as f:
    t = 0
    for ix, c in enumerate(f.read()):
        if c == '(':
            t += 1
        elif c == ')':
            t -= 1
        if t == -1:
            print(ix+1)
            break
    