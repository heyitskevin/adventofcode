from collections import defaultdict
from itertools import combinations

def readfile():
    r = []
    with open('input.txt') as f:
        for ln in f.read().split('\n'):
            r.append(list(ln.strip()))
    return r


def make_map(grid):
    m = defaultdict(list)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            v = grid[i][j]
            if v != '.':
                m[v].append((i, j))
    return m


def main():
    data = readfile()
    height = len(data)
    width = len(data[0])
    antinodes = set()
    node_map = make_map(data)
    for n, coords in node_map.items():
        for combi in combinations(coords, 2):
            y1, x1 = combi[0]
            y2, x2 = combi[1]
            dy = y2 - y1
            dx =x2 -x1
            antinodes.add((y1, x1))
            antinodes.add((y2, x2))
            node_y1, node_x1 = y1 - dy, x1 - dx
            node_y2, node_x2 = y2 + dy, x2 + dx

            while 0 <= node_y1 < height and 0 <= node_x1 < width:
                antinodes.add((node_y1, node_x1))
                node_y1 -= dy
                node_x1 -= dx
            while 0 <= node_y2 < height and 0 <= node_x2 < width:
                antinodes.add((node_y2, node_x2))
                node_y2 += dy
                node_x2 += dx
    return len(antinodes)



print(main())