def readfile():
    initial_state = {}
    connectivity = {}
    zeds = {}
    with open('input.txt') as f:
        init, conn = f.read().split('\n\n')
        for i in init.strip().split('\n'):
            k, v = i.split(':')
            initial_state[k.strip()] = int(v)
        for c in conn.strip().split('\n'):
            logic, out = c.split('->')
            connectivity[out.strip()] = logic.strip()
            if 'z' == out.strip()[0]:
                zeds[out.strip()] = None
    return initial_state, connectivity, zeds

def make_graph_mapping(connections):
    g = {}
    for k, v in connections.items():
        s = v.strip().split(' ')
        assert len(s) == 3
        g[k] = {
            # Left and right are arbitrary just be consistent
            'L': s[0],
            'R': s[2],
            'O': s[1] # The operation OR, XOR, etc.
        }
    return g

def calculate(path, init, gr):
    final = path[-1]



def main():
    init, conn, zeds = readfile()
    g = make_graph_mapping(conn)
    for k in g.keys():
        if k not in init:
            init[k] = None
    # Brute force I guess
    while None in init.values():
        for k, v in g.items():
            L = init.get(v['L'])
            R = init.get(v['R'])
            if L is None or R is None:
                continue
            else:
                res = None
                match v['O']:
                    case 'AND':
                        res = L & R
                    case 'OR':
                        res = L | R
                    case 'XOR':
                        res = L ^ R
                assert res is not None
                init[k] = res
    sln = ''
    for zk in sorted(zeds.keys())[::-1]:
        sln += str(init[zk])
    return int(sln, 2)

print(main())