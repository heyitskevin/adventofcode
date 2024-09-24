FILENAME = 'input.txt'

def readfile():
    with open(FILENAME) as f:
        return f.read().strip().split(',')
    
from collections import deque

def func():
    q = deque([chr(i) for i in range(ord('a'), ord('q'))])
    visited = {}
    ordered = []
    for _ in range(10000):
        start = ''.join(q)
        if start in visited:
            q = visited[start]
            continue
        for inst in readfile():
            prefix = inst[0]
            if prefix == 's':
                q.rotate(int(inst[1:]))
            if prefix == 'x':
                v = inst[1:].split('/')
                pos_a = int(v[0])
                pos_b = int(v[-1])
                tmp = q[pos_a]
                q[pos_a] = q[pos_b]
                q[pos_b] = tmp
            if prefix == 'p':
                v = inst[1:].split('/')
                name_a = v[0]
                name_b = v[-1]
                ix_a = q.index(name_a)
                ix_b = q.index(name_b)
                q[ix_b] = name_a
                q[ix_a] = name_b
        visited[start] = q
        ordered.append(start)
    return ordered[1000000000 % len(ordered)]
    

print(func())