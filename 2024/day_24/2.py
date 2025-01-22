from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

def readfile():
    initial_state = {}
    connectivity = {}
    zeds = {}
    G = defaultdict(list)
    with open('input.txt') as f:
        init, conn = f.read().split('\n\n')
        for i in init.strip().split('\n'):
            k, v = i.split(':')
            initial_state[k.strip()] = int(v)
        for c in conn.strip().split('\n'):
            logic, out = c.split('->')
            connectivity[out.strip()] = logic.strip()
            left, _, right = logic.strip().split(' ')
            G[left.strip()].append(out.strip())
            G[right.strip()].append(out.strip())
            if 'z' == out.strip()[0]:
                zeds[out.strip()] = None
    return initial_state, connectivity, zeds, G

# No coded solution today. The problem statement says that the behavior of the network is designed to be a binary adder.
# We introspect the input by hand looking for discrepancies in the expected adder structure
# First search anomolies on the XOR output digit, then on the XOR inputs and the AND inputs
# Then use the below script to introspect more intermediate adder state discrepancies.

def main():
    init, conn, zeds, gr = readfile()
    xors = []
    for k, v in conn.items():
        if 'XOR' in v and 'x' in v and 'y' in v:
            xors.append((k, v))
    assert len(xors) == len(zeds) - 1
    lookup = defaultdict(list)
    for x in xors:
        output, _ = x
        for k, v in conn.items():
            if output in v:
                lookup[output].append((k, v))
    for k, v in lookup.items():
        print(k, v)
print(main())

