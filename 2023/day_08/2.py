FILENAME = 'input.txt'

def read_input():
    with open(FILENAME) as f:
        directions, rest = f.read().split('\n\n')

        adjacency = {}
        for elem in rest.split('\n'):
            k, v = elem.split('=')
            adjacency[k.strip()] = [x.strip() for x in v.strip()[1:-1].split(',')]
        return directions, adjacency

def get_start_nodes(nodes):
    # return list of all nodes that end with A
    res = []
    for k in nodes:
        if k[-1]  == 'A':
            res.append(k)
    return res

def get_end_nodes(nodes):
    res = []
    for k in nodes:
        if k[-1] == 'Z':
            res.append(k)
    return res


def direction_transform(directions):
    return [0 if c=='L' else 1 for c in directions]

def build_route_maps(number_directions, neighbors):
    routes = {}
    for start in neighbors:
        node = start
        route = []
        for i in range(len(number_directions)):
            next_node = neighbors[node][number_directions[i]]
            route.append(next_node)
            node = next_node
        routes[start] = route
    return routes

def z_check(arr):
    for e in arr:
        if e[-1] != 'Z':
            return False
    return True

# def traverse_by_routes(starts, neighbors, routes):
#     steps = 0
#     big_steps = len(routes)
#     route_set = {k: set(v) for k, v in routes.items()} # Faster lookup 
#     z_end = get_end_nodes(neighbors)
#     nodes = starts

#     while not z_check(nodes):
#         print('starting', nodes)
#         curr_routes = [routes[n] for n in nodes]
#         curr_route_sets = [route_set[n] for n in nodes]
#         z_ix = [-1 for z in z_end]
#         for cr in curr_routes:
#             # Look in each route for Z vals
#             for ix, z in enumerate(z_end):
#                 try:
#                     z_ix[ix] = cr.index(z)
#                 except ValueError:
#                     z_ix[ix] = -1
#         # Check z_ix to see if all same
#         print(z_ix)
#         if len(set(z_ix)) == 1 and z_ix[0] != -1:
#             return steps + z_ix[0]
#         # Advance all nodes by their routes
#         new_nodes = []
#         for n in nodes:
#             route_end = routes[n][-1]
#             new_nodes.append(route_end)
#         steps += big_steps
#         nodes = new_nodes
#         if steps > 1000000:
#             return 0

            
# def find_by_shift(starters, directions, routes, shift): # GENERAL SOLUTION, BIG TIME COMPLEXITY
#     steps = 0
#     big_step = len(directions)
#     iters = 0
#     nodes = starters

#     def shift_check(nx, rts, sft):
#         for n in nx:
#             if rts[n][sft][-1] != 'Z':
#                 return False
#         return True
    
#     def end_check(nx, rts):
#         for n in nx:
#             if rts[n][-1][-1] != 'Z':
#                 return False
#         return True
    
#     while not (shift_check(nodes, routes, shift) or end_check(nodes, routes)):
#         new_nodes = []
#         for node in nodes:
#             new_nodes.append(routes[node][-1])
#         nodes = new_nodes
#         steps += big_step
#         iters += 1
#         print(iters)
#     return steps + shift

# def big_step_traverse(starters, step_size, routes): # IGNORE THIS
#     def end_check(nx, rts):
#         for n in nx:
#             print([rts[n][-1]])
#             if rts[n][-1][-1] != 'Z':
#                 return False
#         return True
#     nodes = starters
#     iters = 0
#     while end_check(nodes, routes):
#         new_nodes = [routes[n][-1] for n in nodes]
#         nodes = new_nodes
#         iters += 1
#     return step_size * iters

import math
def func():
    directions, neighbors = read_input()
    number_directions = direction_transform(directions)
    routes = build_route_maps(number_directions, neighbors)
    a_starts = get_start_nodes(neighbors)
    

    x = a_starts
    iters = [0 for i in x]
    for ix, xx in enumerate(x):
        ii = 0
        loc = xx
        while loc[-1] != 'Z':
            loc = routes[loc][-1]
            ii += 1
        iters[ix] = ii
    print(math.lcm(*iters))
    print(iters)
    print(math.lcm(*iters) * len(directions))
    
func()

