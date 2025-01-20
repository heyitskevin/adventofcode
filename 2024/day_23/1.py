from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

def readfile():
    with open('input.txt') as f:
        return [
            tuple(ln.strip().split('-')) for ln in f.read().split('\n')
        ]
    

def main():
    conns = readfile()
    
    adj = defaultdict(list)
    G = nx.Graph() # We kitchen sink this sucker
    s = set()
    for l, r in conns:
        G.add_edge(l, r)
        adj[l].append(r)
    
    for elem in nx.simple_cycles(G, length_bound=3):
        for e in elem:
            if e[0] == 't':
                s.add(frozenset(elem))
                break
    return len(s)
    

print(main())
