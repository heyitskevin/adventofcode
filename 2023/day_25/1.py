FILENAME = 'edit_input.txt'

import networkx as nx # NETWORKX LIB OFFERS MINIMUM EDGE CUT BUT WE JUST EDIT THE INPUT FILE AFTER EYEBALLING
import matplotlib.pyplot as plt

def read_file():
    with open(FILENAME) as f:
        return [ln.strip().split(':') for ln in f.read().split('\n')]

def make_dict(list_of_lists):
    d = {}
    for elem in list_of_lists:
        k, v = elem
        v = v.strip().split(' ')
        d[k] = v
    return d

def dfs(graph):
    # Hard code based on examination
    left = nx.dfs_edges(graph, source='slf')
    right = nx.dfs_edges(graph, source='sbz')

    lc = set()
    rc = set()
    for edge in left:
        a, b = edge
        lc.add(a)
        lc.add(b)
    for edge in right:
        a, b = edge
        rc.add(a)
        rc.add(b)

    print(len(lc), len(rc))
    print(len(lc)*len(rc))

def func():
    dat = read_file()
    d = make_dict(dat)
    # rjs, mrd, ncg, gmr, gsk, ntx
    
    g = nx.from_dict_of_lists(d)
    dfs(g)
    # nx.draw_networkx(g, linewidths=2)
    # plt.show()
    # print(d)

func()