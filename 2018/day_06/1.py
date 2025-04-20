from collections import defaultdict
# IDK why but this problem fucky wucky with my head
# copying some reddit solution 
def readfile():
    r = set()
    max_x, max_y = -1, -1
    with open('input.txt') as f:
        for ln in f.read().split('\n'):
            x, y = ln.split(',')
            x = int(x)
            y = int(y)
            max_x = max(x, max_x)
            max_y = max(y, max_y)
            r.add((x, y))
    return r, max_x, max_y


def main():
    nodes, rows, cols = readfile()
    node_lookup = {node_id: coords for node_id, coords in enumerate(nodes, start=1)}
    
    region_sizes = defaultdict(int)
    inf_ids = set()
    
    for r in range(rows + 1):
        for c in range(cols + 1):
            min_dist = sorted(
                [(abs(r - rr) + abs(c - cc), c_id ) for c_id, (rr, cc) in node_lookup.items()]
            )
            
            if len(min_dist) == 1 or min_dist[0][0] != min_dist[1][0]:
                coord_id = min_dist[0][1]
                region_sizes[coord_id] += 1
                
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    # if at edge of zone, it's infinte
                    inf_ids.add(coord_id)
    
    return max(size for c_id, size in region_sizes.items() if c_id not in inf_ids)

print(main())