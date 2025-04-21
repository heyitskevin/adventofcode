from collections import defaultdict
# It's a DAG

# I dont know how I managed to get this first try but whatever
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
    data = readfile()
    num_workers = 5
    workers = {id: (None, 0) for id in range(1, num_workers + 1)}
    child_to_parents = make_inverted_dependency_dict(data)
    parent_to_children = make_dependency_dict(data)
    time = 0
    steps_available = sorted(list(get_parents(data)))
    total = set()
    completed = set()
    for a, b in data:
        total.add(a)
        total.add(b)

    while completed != total:
        time += 1
        for k, v in workers.items():
            if v[1] == 1:
                completed.add(v[0])
                for cc in parent_to_children[v[0]]:
                    if all(p in completed for p in child_to_parents[cc]):
                        steps_available.append(cc)
                workers[k] = (None, 0)
            elif v[0] is not None:
                workers[k] = (v[0], v[1] - 1)
        steps_available = sorted(steps_available)
        available_workers = [w for w, v in workers.items() if v[1] == 0]
        for aw in range(len(available_workers)):
            if len(steps_available) > 0:
                s = steps_available.pop(0)
                workers[available_workers[aw]] = (s, 60 + ord(s) - ord('A') + 1)
        
    return time - 1


print(main())