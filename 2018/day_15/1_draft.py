from collections import deque
# I know that we don't package our code to be as succinct as possible and we repeat a lot of routines but this problem sucks so deal with it
class Creature: # ABC
    def __init__(self, id, row, col):
        self.id = id
        self.row = row
        self.col = col
        self.hp = 200

    def take_hit(self):
        self.hp = self.hp - 3


class Goblin(Creature):
    def __init__(self, id, row, col):
        super().__init__(id, row, col)
        self.type = 'G'

class Elf(Creature):
    def __init__(self, id, row, col):
        super().__init__(id, row, col)
        self.type = 'E'


class GameGrid:
    def __init__(self, grid_array):
        self.grid = []
        self.elves = {}
        self.goblins = {}
        self.dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)] # U R D L
        e_id = 1
        g_id = 1
        steps = 0
        for rix, row in enumerate(grid_array):
            r = []
            for cix, col in enumerate(row):
                if col == 'E':
                    self.elves[e_id] = Elf(e_id, rix, cix)
                    e_id += 1
                elif col == 'G':
                    self.goblins[g_id] = Goblin(g_id, rix, cix)
                    g_id += 1
                r.append(col)
            self.grid.append(r)
    
    def is_done(self):
        return len(self.elves) == 0 or len(self.goblins) == 0
    
    def get_turn_order(self):
        order = []
        for k, v in self.elves.items():
            order.append((k, v.row, v.col, 'E'))
        for k, v in self.goblins.items():
            order.append((k, v.row, v.col, 'G'))

        return sorted(order, key=lambda x: (x[1], x[2]))
    
    def find_path(self, start_row, start_col, end_row, end_col):
        visited = set()
        q = [([], start_row, start_col)]
        
        while q:
            path, r, c = q.pop(0)
            print((r, c), (end_row, end_col))
            if r == end_row and c == end_col:
                return path
            if (r, c) in visited:
                continue
            visited.add((r, c))
            for dr, dc in self.dirs:
                nr, nc  = r + dr, c + dc
                if self.grid[nr][nc] == '.':
                    q.append((path + [(nr, nc)], nr, nc))
        
    def all_shortest_paths(self, start_row, start_col, end_row, end_col): # Some GPT slop to do all shortest paths bc im dying
        rows, cols = len(self.grid), len(self.grid[0])
        start = (start_row, start_col)
        end = (end_row, end_col)

        # Only '.' are walkable
        def neighbors(r, c):
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and self.grid[nr][nc] == ".":
                    yield (nr, nc)

        # BFS to compute shortest distances
        dist = {start: 0}
        q = deque([start])
        while q:
            r, c = q.popleft()
            if (r, c) == end:
                break
            for nr, nc in neighbors(r, c):
                if (nr, nc) not in dist:
                    dist[(nr, nc)] = dist[(r, c)] + 1
                    q.append((nr, nc))

        if end not in dist:
            return []  # No path exists

        shortest_len = dist[end]

        # Backtracking to collect all paths
        results = []
        def dfs(path):
            r, c = path[-1]
            if (r, c) == end:
                results.append(path[:])
                return
            for nr, nc in neighbors(r, c):
                # Only move to neighbors that are exactly +1 in distance
                if dist.get((nr, nc), float('inf')) == dist[(r, c)] + 1:
                    path.append((nr, nc))
                    dfs(path)
                    path.pop()

        dfs([start])
        return results


    def round(self):
        turn_order = self.get_turn_order()
        for id, unit_row, unit_col, unit_type in turn_order:
            if self.is_done():
                return
            if unit_type == 'E':
                enemy_type = 'G'
                unit = self.elves.get(id)
            else:
                enemy_type = 'E'
                unit = self.goblins.get(id)
            if unit is None:
                continue
            # Check adjacent
            adjacent = []
            for dr, dc in self.dirs:
                if self.grid[unit_row + dr][unit_row + dc] == enemy_type:
                    adjacent.append((unit_row + dr, unit_col + dc))
            if adjacent:
                adj_target = sorted(adjacent, key=lambda x: (x[0], x[1]))[0]
                if enemy_type == 'G':
                    for g in self.goblins:
                        if self.goblins[g].row == adj_target[0] and self.goblins[g].col == adj_target[1]:
                            self.goblins[g].take_hit()
                            if self.goblins[g].hp <= 0:
                                self.grid[g.row][g.col] = '.'
                                self.goblins.pop(g)

                                if self.is_done():
                                    return
                else:
                    for e in self.elves:
                        if self.elves[e].row == adj_target[0] and self.elves[e].col == adj_target[1]:
                            self.elves[e].take_hit()
                            if self.elves[e].hp <= 0:
                                self.grid[e.row][e.col] = '.'
                                self.elves.pop(e)

                                if self.is_done():
                                    return
                continue # An adjacent enemy and attack means the turn is over
            # No adjacent means movement

            closest_r, closest_c = None, None
            if enemy_type == 'G':
                open_squares = []
                
                for k, e in self.goblins.items():
                    for dr, dc in self.dirs:
                        nr, nc = e.row + dr, e.col + dc
                        if self.grid[nr][nc] == '.':
                            open_squares.append((nr, nc))
                min_path_len = 9999
                path_options = []
                for orr, occ in open_squares:
                    paths = self.all_shortest_paths(unit_row, unit_col, orr, occ)
                    if len(paths[0]) < min_path_len:
                        min_path_len = len(paths[0])
                for orr, occ in open_squares:
                    paths = self.all_shortest_paths(unit_row, unit_col, orr, occ)
                    if len(paths[0]) == min_path_len:
                        path_options += paths
                path_first_steps = [p[0] for p in path_options]
                closest_r, closest_c = sorted(path_first_steps, key=lambda x: (x[0], x[1]))[0]
                # do movement
                self.grid[unit_row][unit_col] = '.'
                self.grid[closest_r][closest_c] = 'E'
                self.elves[id].row = closest_r
                self.elves[id].col = closest_c
            else:
                open_squares = []
                
                for k, e in self.elves.items():
                    for dr, dc in self.dirs:
                        nr, nc = e.row + dr, e.col + dc
                        if self.grid[nr][nc] == '.':
                            open_squares.append((nr, nc))
                min_path_len = 9999
                path_options = []
                for orr, occ in open_squares:
                    paths = self.all_shortest_paths(unit_row, unit_col, orr, occ)
                    if paths and len(paths[0]) < min_path_len:
                        min_path_len = len(paths[0])
                for orr, occ in open_squares:
                    paths = self.all_shortest_paths(unit_row, unit_col, orr, occ)
                    if paths and len(paths[0]) == min_path_len:
                        path_options += paths
                path_first_steps = [p[0] for p in path_options]
                closest_r, closest_c = sorted(path_first_steps, key=lambda x: (x[0], x[1]))[0]
                # do movement
                self.grid[unit_row][unit_col] = '.'
                self.grid[closest_r][closest_c] = 'G'
                self.goblins[id].row = closest_r
                self.goblins[id].col = closest_c
            # RECheck adjacent
            adjacent = []

            for dr, dc in self.dirs:
                if self.grid[closest_r][closest_c] == enemy_type:
                    adjacent.append((closest_r, closest_c))
            if adjacent:
                adj_target = sorted(adjacent, key=lambda x: (x[0], x[1]))[0]
                if enemy_type == 'G':
                    for g in self.goblins:
                        if self.goblins[g].row == adj_target[0] and self.goblins[g].col == adj_target[1]:
                            self.goblins[g].take_hit()
                            if self.goblins[g].hp <= 0:
                                self.grid[g.row][g.col] = '.'
                                self.goblins.pop(g)
                                if self.is_done():
                                    return
                else:
                    for e in self.elves:
                        if self.elves[e].row == adj_target[0] and self.elves[e].col == adj_target[1]:
                            self.elves[e].take_hit()
                            if self.elves[e].hp <= 0:
                                self.grid[e.row][e.col] = '.'
                                self.elves.pop(e)
                                if self.is_done():
                                    return
        self.steps += 1
                    

            

def readfile():
    g = []
    with open('example.txt') as f:
        for ln in f.readlines():
            g.append(list(ln.strip()))
    return g


def main():
    gg = GameGrid(readfile())
    
    while not gg.is_done():
        gg.round()
    print(gg.steps)

main()

