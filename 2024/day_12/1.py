def readfile():
    grid = []
    with open("input.txt") as f:
        for ln in f.read().split('\n'):
            grid.append(list(ln))
    return grid


def traverse(grid):
    visited = set()
    height = len(grid)
    width = len(grid[0])
    
    dirs = [(-1, 0),(0, 1), (1, 0), (0, -1),] 
    q = [(0,0)]
    
    price = 0

    while q:
        r, c = q.pop(0)
        if (r, c) in visited:
            continue
        else:
            # explore the region
            visited.add((r, c))
            r_area = 0
            r_perimeter = 0
            region = set()
            plant = grid[r][c]
            region_q = [(r,c)]
            while region_q:
                rr, rc = region_q.pop(0)
                if (rr, rc) in region:
                    continue
                else:
                    region.add((rr, rc))
                    r_area += 1
                    edges = 4
                    for d in dirs:
                        y, x = d
                        nr, nc = rr + y, rc + x
                        if 0 <= nr < height and 0 <= nc < width:
                            if grid[nr][nc] == plant:
                                edges -= 1
                                region_q.append((nr, nc))
                            else:
                                # Some other region to visit
                                q.append((nr, nc))
                    r_perimeter += edges
            visited |= region
            
            price += (r_area * r_perimeter)

    return price


def main():
    grid = readfile()
    
    price = traverse(grid)
    return price


print(main())