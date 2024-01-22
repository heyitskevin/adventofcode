FILENAME = 'input.txt'

from collections import defaultdict
import itertools

def read_file():
    with open(FILENAME) as f:
        return [ln for ln in f.read().split('\n')]

def make_adjacency(lines):
    g = defaultdict(list)
    
    for l in lines:
        orig, dest = l.split('to')
        dest, cost = dest.split('=')
        cost = int(cost)
        orig = orig.strip()
        dest = dest.strip()
        g[orig].append((dest, cost))
        g[dest].append((orig, cost))
    return g

def brute_force(adj):
    locations = list(adj.keys())
    perms = itertools.permutations(locations)
    dist = []
    for p in perms:
        d = 0
        for ix in range(len(p) - 1):
            curr = p[ix]
            nxt = p[ix+1]
            neighbors = adj[curr]
            for name, cost in neighbors:
                if name == nxt:
                    d += cost
                    break
        dist.append(d)
    return dist


def func():
    lns = read_file()
    adj = make_adjacency(lns)
    d = brute_force(adj)
    print(max(d))
func()
