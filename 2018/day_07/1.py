from collections import defaultdict
# It's a DAG

def readfile():
    res = []
    with open('input.txt') as f:
        for ln in f.read().split('\n'):
            l, r = ln.strip().split('must be finished before step')
            l = l.strip().split(' ')[1]
            r = r.strip().split(' ')[0]
            res.append((l, r))
    return res # Tuples (X, Y) such that X -> Y (Y depends on X)

def get_parents(dependency_graph):
    parents = set()
    children = set()

    for p, c in dependency_graph:
        parents.add(p)
        children.add(c)

    return parents - children # assume nice data

def get_children(dependency_graph):
    parents = set()
    children = set()

    for p,c in dependency_graph:
        parents.add(p)
        children.add(c)
    
    return children - parents

def make_dependency_dict(dependency_list):
    d = defaultdict(list)
    for p, c in dependency_list:
        d[p].append(c)
    return d

def make_inverted_dependency_dict(dependency_list):
    d = defaultdict(list)
    for p, c in dependency_list:
        d[c].append(p)
    return d

def main():
    d = readfile()
    child_to_parent = make_inverted_dependency_dict(d)
    parent_to_child = make_dependency_dict(d)
    roots = get_parents(d)
    
    order = []
    
    q = list(sorted(roots))
    visited = set()
    while q:
        next_element = q.pop(0)
        order.append(next_element)
        visited.add(next_element)
        next_children = parent_to_child[next_element]
        ready = []
        for child in next_children:
            if all(par in visited for par in child_to_parent[child]) and child not in visited:
                ready.append(child)
        q += ready
        q = sorted(q) # That was diabolical for the problem LOL

    return ''.join(order)

print(main())