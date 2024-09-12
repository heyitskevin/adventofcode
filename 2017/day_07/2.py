FILENAME = 'input.txt'

def read_file():
    res = {}
    weights = {}
    with open(FILENAME) as f:
        for ln in f.read().split('\n'):
            if ' -> ' in ln:
                k, v = ln.split(' -> ')
                parent, w = k.split(' (')

                children = v.split(', ')
                res[parent] = children
                weights[parent] = int(w[:-1])
            else:
                n, w = ln.split(' (')
                
                weights[n.strip()] = int(w[:-1])
    return res, weights

def get_root(d):
    p = set(d.keys())
    c = set()
    for v in d.values():
        for vv in v:
            c.add(vv)
    return list(p-c)[0]

def func():
    parent_child_lookup, weight_lookup = read_file()
    
    found_weights = {}
    root = get_root(parent_child_lookup)
    q = [root]
    while q:
        curr_node = q.pop(0)
        children = parent_child_lookup.get(curr_node, [])
        if len(children) == 0:
            found_weights[curr_node] = weight_lookup[curr_node]
        else:
            all_children = True
            for child in children:
                if child not in found_weights:
                    q.append(child)
                    all_children = False
            if all_children:
                c_weights = [found_weights[c] for c in children]
                found_weights[curr_node] = sum(c_weights)
            else:
                q.append(curr_node)
    
    q = [root]
    while q:
        curr_node = q.pop(0)
        children = parent_child_lookup.get(curr_node, [])
        s = sum([found_weights[c] for c in children]) // len(children)
        for c in children:
            if found_weights[c] != s:
                print(curr_node, found_weights[curr_node])
                return [(cc, found_weights[cc]) for cc in children]
            else:
                q.append(c)

    

# print(func())

# FROM REDDIT
import networkx as nx
import collections
graph = nx.DiGraph()

# Build the graph of programs
with open(FILENAME) as f:
    for line in f.read().split('\n'):
        name = line.split()[0]

        graph.add_node(name, weight=int(line.split()[1].strip('()')))

        if '->' in line:
            children = [n.strip() for n in line.split('->')[1].split(',')]

            for child in children:
                graph.add_edge(name, child)

# Topological sort to find the root of the tree
ordered = list(nx.topological_sort(graph))

print('PART 1:', ordered[0])

# Keep track of each node's total weight (itself + its children)
weights = {}

# Going backwards (starting from the leaves)
for node in reversed(ordered):
    # Start with this nodes own weight
    total = graph.nodes[node]['weight']

    counts = collections.Counter(weights[child] for child in graph[node])
    unbalanced = None

    for child in graph[node]:
        # If this child's weight is different than others, we've found it
        if len(counts) > 1 and counts[weights[child]] == 1:
            unbalanced = child
            break

        # Otherwise add to the total weight
        val = weights[child]
        total += weights[child]

    if unbalanced:
        # Find the weight adjustment and the new weight of this node
        diff = weights[unbalanced] - val
        print('PART 2:', graph.nodes[unbalanced]['weight'] - diff)
        break

    # Store the total weight of the node
    weights[node] = total
