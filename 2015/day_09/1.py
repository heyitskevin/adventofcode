FILENAME = 'input.txt'

from collections import defaultdict

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

def traverse(graph):
    # Take advantage of the fact that the graph is undirected and complete (fully connected)
    # For every start position, take the min unvisited neighbor and go there
    # Results in the lowest possible route for every start position
    # The min of these vals is the most desired start position
    route_distances = []
    for start in graph:
        q = []
        visited = set()
        dist = 0
        q.append((start, 0))
        while q:
            loc, cost = q.pop(0)
            print('visiting', loc)
            neighbors = graph.get(loc, [])
            if loc in visited:
                continue
            else:
                visited.add(loc)
                dist += cost
                min_neighbor = sorted(neighbors, key=lambda x: x[1])
                for mn in min_neighbor:
                    if mn[0] not in visited:
                        q.append(mn)
                        break
        route_distances.append(dist)
    print(route_distances, min(route_distances))



def func():
    lns = read_file()
    g = make_adjacency(lns)
    traverse(g)
func()