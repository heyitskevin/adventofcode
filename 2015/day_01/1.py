with open('input.txt') as f:
    t = 0
    for c in f.read():
        if c == '(':
            t += 1
        elif c == ')':
            t -= 1
    print(t)