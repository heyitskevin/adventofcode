FILENAME = 'input.txt'
import pprint
from functools import cache
def read_file():
    with open(FILENAME) as f:
        return [list(ln.strip()) for ln in f.read().split('\n')]

def get_start(garden):
    for ix, row in enumerate(garden):
        for xix, col in enumerate(row):
            if col == 'S':
                return ix, xix


def wander_garden(row, col, max_steps, garden):
    visited = set()
    """
            O
          O X O   
        O X S X O
          O X O
            O
    """
    
    frontier = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    steps = 0
    q = [(row, col, steps)] # row, col, steps
    # Visit node, check bounds/visited add frontier to queue
    # Do until max_steps or q empty
    
    while q:
        current = q.pop(0)
        r, c, steps = current
        if steps > max_steps:
            return visited
        if (r, c,steps) in visited:
            pass
        else:
            visited.add((r, c,steps))
            steps += 1
            for f in frontier:
                rr = r + f[0]
                cc = c + f[1]
                if rr in range(len(garden)) and cc in range(len(garden[0])) and garden[rr][cc] != '#':
                    q.append((rr, cc, steps))
        
    return visited
        

# brute force DFS
def func():
    garden = read_file()
    row, col = get_start(garden)
    x = wander_garden(row, col, 64, garden)
    s = set()
    # clunky way: visit all possible steps, filter out the even ones
    # more elegant way I am too dumb to do: memoize the even steps, take two steps in any direction, memoize, repeat
    for i in x:
        if i[2]%2 == 0:
            s.add((i[0], i[1]))
    
    print(s, len(s))

func()