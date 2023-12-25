FILENAME = 'input.txt'
MAX_STEPS =  26501365

import pprint
import itertools
from functools import cache
def read_file():
    with open(FILENAME) as f:
        return [list(ln.strip()) for ln in f.read().split('\n')]

def get_start(garden):
    for ix, row in enumerate(garden):
        for xix, col in enumerate(row):
            if col == 'S':
                return ix, xix

def check_plot(row, col, garden):
    return row in range(len(garden)) and col in range(len(garden[0])) and garden[row][col] != '#'

def infinte_garden(max_steps, garden, sr, sc):
    directions = [(1, 0), (0,1), (-1,0), (0, -1)] # Never step in direction (ix+2)%4
    steps = 0
    height = len(garden)
    width = len(garden[0])
    visited = set()
    q = []
    # Weird initialization for odd/even cases
    if max_steps % 2 == 0:
        q.append((sr, sc))
    else:
        for d in directions:
            rr = sr + d[0]
            cc = sc + d[1]
            if check_plot(rr, cc, garden):
                q.append((rr, cc))
            steps = 1
    while q:
        if steps > max_steps:
            return visited
        current = q.pop(0)
        raw_r, raw_c = current
        r = raw_r % height
        c = raw_c % width
        if (r,c) in visited:
            pass
        else:
            visited.add((r,c))
            steps += 2
            # stepper block
            for d in range(4):
                for d2 in range(4):
                    if d2 != (d + 2) % 4: # there's a bit of double checking the same element here
                        rr = raw_r + directions[d][0]
                        cc = raw_c + directions[d][1]
                        if check_plot(rr % height, cc % width, garden):
                            rr += directions[d2][0]
                            cc += directions[d2][1]
                            if check_plot(rr % height, cc % width, garden):
                                q.append((rr,cc))
    
    return visited

def base_garden_steps(max_steps, garden, sr, sc):
    directions = [(1, 0), (0,1), (-1,0), (0, -1)] # Never step in direction (ix+2)%4
    steps = 0
    visited = set()
    q = []
    # Weird initialization for odd/even cases
    if max_steps % 2 == 0:
        q.append((sr, sc))
    else:
        for d in directions:
            rr = sr + d[0]
            cc = sc + d[1]
            if check_plot(rr, cc, garden):
                q.append((rr, cc))
            steps = 1
    while q:
        current = q.pop(0)
        r, c = current
        if (r, c) in visited:
            pass
        else:
            visited.add((r,c))
            steps += 2
            # stepper block
            for d in range(4):
                for d2 in range(4):
                    if d2 != (d + 2) % 4: # there's a bit of double checking the same element here
                        rr = r + directions[d][0]
                        cc = c + directions[d][1]
                        if check_plot(rr, cc, garden):
                            rr += directions[d2][0]
                            cc += directions[d2][1]
                            if check_plot(rr, cc, garden):
                                q.append((rr, cc))
    return visited

def count_empty(garden):
    ct = 0
    for r in garden:
        for c in r:
            if c != '#':
                ct += 1
    return ct

def func():
    garden = read_file()
    row, col = get_start(garden)
    x = infinte_garden(65 +  2*len(garden), garden, row, col)
    print(x, len(x))

    # 65, 3617
    # 65 + 131, 7334
    # 7334
    # x = base_garden_steps(1, garden, row, col)
    # ep = count_empty(garden)
    # odds = len(x)
    # evens = ep - odds
    # # print(x, len(x), ep)
    # travel = ((MAX_STEPS - (len(garden)//2)) // len(garden)) # Doesn't include base
    
    # e_s = sum(range(1, travel-len(garden) - 1, 2))
    # o_s = sum(range(2, travel-len(garden), 2))
    # k = ((e_s*evens) + (o_s*odds))*4 + odds
    # print(k)
    # # print(one_length * (travel - 2) * 4 - odds*4)
    # print('----')

    # side = ((MAX_STEPS - (len(garden)//2)) // len(garden)) * 2
    # side = side + 1
    # half_side = side // 2
    # area = (side) * (side)
    # aa = area // 2
    # print((aa + 1)*odds + aa*evens)
    # # print((half_side * evens + (half_side * odds) + 1) *  (side))
    # tot = 0
    # print(tot)
    # print(odds, evens)
    # print(len(garden), len(garden[0]), row, col)

# func()
    

# NOTICED THE PATTERN, COULDN'T FIGURE OUT THE ENTIRETY OF THE MATH 
# I MADE A BAD ASSUMPTION THAT IT WAS A SQUARE BUT IT'S ACTUALLY A RHOMBUS
# here's the math for the solution
G = {i+j*1j:c for i,r in enumerate(open('input.txt'))
              for j,c in enumerate(r) if c in '.S'}

done = []
todo = {x for x in G if G[x]=='S'}
cmod = lambda x: complex(x.real%131, x.imag%131)

for s in range(3 * 131):
    if s == 64: print(len(todo))
    if s%131 == 65: done.append(len(todo))

    todo = {p+d for d in {1, -1, 1j, -1j}
                for p in todo if cmod(p+d) in G}

f = lambda n,a,b,c: a+n*(b-a+(n-1)*(c-b-b+a)//2)
print(f(26501365 // 131, *done))
# 14584 base thigny
# 13250683 brute force (wrong) too low
# 128126
# 596854429360000 too low

# 596857397104703 soln
# 596860330060984 too high
# 597672935160000 too high

