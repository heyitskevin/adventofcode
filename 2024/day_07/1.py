def readfile():
    r = []
    with open('input.txt') as f:
        for ln in f.read().split('\n'):
            left, right = ln.split(':')
            a = []
            for n in right.strip().split(' '):
                a.append(int(n))
            r.append((int(left), a))
    
    return r

def do_op(left, right, op):
    if op == '+':
        return left + right
    elif op == '*':
        return left * right


def btree(values):
    results = []
        
    def tree(root, rest):
        if len(rest) == 0:
            results.append(root)
            return 
        nxt = rest[0]
        add = do_op(root, nxt, '+')
        mul = do_op(root, nxt, '*')
        tree(add, rest[1:])
        tree(mul, rest[1:])

    tree(values[0], values[1:])
    return results


def main():
    data = readfile()
    res = 0

    for d in data:
        v = btree(d[1])
        if d[0] in v:
            res += d[0]

    return res

print(main())