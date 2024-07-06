def iswall(x, y):
    f = (x+y)**2 + 3*x + y + 1350
    return  int.bit_count(f) % 2

def bfs():
    x = 1
    y = 1
    steps = 0
    q = [(x,y, steps)]
    visited = set()
    while q:
        x,y,steps = q.pop(0)
        
        if steps > 50:
            continue
        
        steps += 1
        if (x,y) in visited:
            continue
        
        visited.add((x,y))
        for a,b in [(0,1), (1,0), (0,-1), (-1,0)]:
            n_x = x + a
            n_y = y + b
            if n_x >= 0 and n_y >= 0 and not iswall(n_x, n_y):
                q.append((n_x,n_y,steps))
    return len(visited)

print(bfs())