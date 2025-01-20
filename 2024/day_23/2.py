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
    G = nx.Graph() 
    s = [] # We know there's one solution
    for l, r in conns:
        G.add_edge(l, r)
    for c in nx.find_cliques(G):
        if len(c) > len(s):
            s = c
    return ','.join(sorted(s))
    

print(main())
