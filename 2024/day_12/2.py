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
            r_sides = 0
            region = set()
            
            plant = grid[r][c]
            region_q = [(r,c)]

            frontier = set()
            while region_q:
                rr, rc = region_q.pop(0)
                if (rr, rc) in region:
                    continue
                else:
                    region.add((rr, rc))
                    r_area += 1
                    for d in dirs:
                        y, x = d
                        nr, nc = rr + y, rc + x
                        if 0 <= nr < height and 0 <= nc < width:
                            if grid[nr][nc] == plant:
                                region_q.append((nr, nc))
                            else:
                                # Some other region to visit
                                frontier.add((rr, rc))
                                q.append((nr, nc))
                        if not (0 <= nr < height and 0 <= nc < width):
                            # edges
                            frontier.add((rr, rc))
            diags = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
            for f in region:
                fr, fc = f
                # convex corners
                corners = set()
                for ix, d1 in enumerate(dirs):
                    for d2 in [dirs[(ix + 1) % 4], dirs[(ix - 1) % 4]]:
                        r1, c1 = fr + d1[0], fc + d1[1]
                        r2, c2 = fr + d2[0], fc + d2[1]
                        if (r1, c1) not in region  and (r2, c2) not in region:
                            # corner found
                            corners.add(tuple(sorted([(r1, c1), (r2, c2)])))                            

                r_sides += len(corners)
                
                # concave corners:
                for diag in diags:
                    rd, cd = fr + diag[0], fc + diag[1]
                    if (rd, cd) not in region:
                        if (fr + diag[0], fc) in region and (fr, fc + diag[1]) in region:
                            r_sides += 1
                
            
            visited |= region
            if len(frontier) == 0:
                r_sides = 4
            
            price += (r_area * r_sides)

    return price


def main():
    grid = readfile()
    price = traverse(grid)
    return price


print(main())