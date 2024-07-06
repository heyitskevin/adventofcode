def iswall(x, y):
    f = (x+y)**2 + 3*x + y + 1350
    return  int.bit_count(f) % 2

def bfs(des_x, des_y):
    x = 1
    y = 1
    steps = 0
    q = [(x,y, steps)]
    visited = set()
    while q:
        x,y,steps = q.pop(0)
        
        if x == des_x and y == des_y:
            return steps
        
        if (x,y) in visited:
            continue

        visited.add((x,y))
        steps += 1
        for a,b in [(0,1), (1,0), (0,-1), (-1,0)]:
            n_x = x + a
            n_y = y + b
            if n_x >= 0 and n_y >= 0 and not iswall(n_x, n_y):
                q.append((n_x,n_y,steps))
    return -1

print(bfs(31, 39))