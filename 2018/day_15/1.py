class GoblinGrid:
    def __init__(self, starting_grid):
        self.grid = starting_grid
        self.elves = self.init_elves()
        self.goblins = self.init_goblins()
        self.dirs = [(-1,0), (0, 1), (1, 0), (0, -1)] # U, R, D, L
        # print("e", self.elves)
        # print("g", self.goblins)
    def reading_order(self, o):
        return sorted(o, key=lambda x: (x['row'], x['col']))
    
    def get_ids_by_turn_order(self):
        s = [[k] + list(v.values()) for k, v in self.elves.items()] + [[k] + list(v.values()) for k, v in self.goblins.items()]

        return sorted(s, key=lambda x: (x[1], x[2]))

    def is_done(self):
        return len(self.elves) == 0 or len(self.goblins) == 0

    def init_elves(self):
        e = {}
        e_id = 1
        for ix, row in enumerate(self.grid):
            for cx, col in enumerate(row):
                if col == 'E':
                    e[e_id] = {
                        'row': ix,
                        'col': cx,
                        'hp': 200,
                        'type': 'E'
                    }
                    self.grid[ix][cx] = '.'
                    e_id += 1
        return e
        
    def init_goblins(self):
        e = {}
        e_id = 1
        for ix, row in enumerate(self.grid):
            for cx, col in enumerate(row):
                if col == 'G':
                    e[e_id] = {
                        'row': ix,
                        'col': cx,
                        'hp': 200,
                        'type': 'G'
                    }
                    self.grid[ix][cx] = '.'
                    e_id += 1
        return e

    def shortest_path(self, start_row, start_col, end_row, end_col):
        visited = set()
        
        q = [([], start_row, start_col)]
        while True:
            dist, r, c = q.pop(0)
            if (r, c) in visited:
                continue
            visited.add((r,c))
            if (r, c) == (end_row, end_col):
                return dist
            for dr, dc in self.dirs:
                next_r = r + dr
                next_c = c + dc
                if (next_r, next_c) == (end_row, end_col):
                    return dist + [(next_r, next_c)]
                if self.grid[next_r][next_c] == '.':
                    q.append((dist + [(next_r, next_c)], next_r, next_c))


    def attack(self, attacker_type, defender_id):
        print(f"{attacker_type} attacking {defender_id}")
        if attacker_type == 'G':
            self.elves.get(defender_id)['hp'] -= 3
            if self.elves.get(defender_id)['hp'] <= 0:
                self.elves.pop(defender_id)
        elif attacker_type == 'E':
            self.goblins.get(defender_id)['hp'] -= 3
            if self.goblins.get(defender_id)['hp'] <= 0:
                self.goblins.pop(defender_id)

    def do_turn(self, current_unit):
        if current_unit is None:
            return False
        if current_unit['type'] == 'E':
            targets = self.goblins
            target_type = 'G'
        else:
            targets = self.elves
            target_type = 'E'
        if not targets:
            # No targets means we're done, maybe account for this at turn level?
            return False
        
        adjacent_enemies = []
        unoccupied_adjacent = []
        for t_id, data in targets.items():
            for dr, dc in self.dirs:
                if self.grid[data['row'] + dr][data['col'] + dc] == '.':
                    unoccupied_adjacent.append((t_id, data['row'] + dr, data['col'] + dc))
            if (data['row'] - current_unit['row'], data['col'] - current_unit['col']) in self.dirs:
                adjacent_enemies.append((t_id, data['row'], data['col']))
        
        if len(adjacent_enemies) > 0:
            # Go straight to attacks
            min_hp = 200
            min_id = -1
            for e_id, e_row, e_col in adjacent_enemies:
                if target_type == 'E':
                    if self.elves[e_id]['hp'] < min_hp:
                        min_hp = self.elves[e_id]['hp']
                        min_id = e_id
                if target_type == 'G':
                    if self.goblins[e_id]['hp'] < min_hp:
                        min_hp = self.goblins[e_id]['hp']
                        min_id = e_id
            if min_id == -1:
                min_id = sorted(adjacent_enemies, key=lambda x: (x[1], x[2]))[-1][0]
            self.attack(current_unit['type'], min_id)
        else:
            # movement
            dist_to_enemy = {
                e[0]: (self.shortest_path(current_unit['row'], current_unit['col'], e[1], e[2]), e[1], e[2]) for e in unoccupied_adjacent
            }
            # Decide movement by finding the shortest path to the shortest enemy and then arranging by row/col for tiebreaker
            closest_enemy_id = -1
            shortest_dist = 99999
            for k, v in dist_to_enemy.items():
                if len(v[0]) < shortest_dist:
                    closest_enemy_id = k
                    shortest_dist = len(v[0])
                elif len(v[0]) == shortest_dist:
                    if v[1] < dist_to_enemy[closest_enemy_id][1]:
                        closest_enemy_id = k
                elif len(v[0]) == shortest_dist and v[1] == dist_to_enemy[closest_enemy_id][1]:
                    if v[2] < dist_to_enemy[closest_enemy_id][2]:
                        closest_enemy_id = k
            # Found location to move to, move one step
            current_unit['row'] = dist_to_enemy[closest_enemy_id][0][0][0]
            current_unit['col'] = dist_to_enemy[closest_enemy_id][0][0][1]
            adj = []
            for t_id, data in targets.items():
                for dr, dc in self.dirs:
                    if (data['row'] - current_unit['row'], data['col'] - current_unit['col']) in self.dirs:
                        adj.append((t_id, data['row'], data['col']))
            min_hp = 200
            min_id = -1
            for e_id, e_row, e_col in adj:
                if target_type == 'E':
                    if self.elves[e_id]['hp'] < min_hp:
                        min_hp = self.elves[e_id]['hp']
                        min_id = e_id
                if target_type == 'G':
                    if self.goblins[e_id]['hp'] < min_hp:
                        min_hp = self.goblins[e_id]['hp']
                        min_id = e_id
            
            if adj and min_id == -1:
                min_id = sorted(adj, key=lambda x: (x[1], x[2]))[-1][0]
            if adj:
                self.attack(current_unit['type'], min_id)


def readfile():
    g = []
    with open('example.txt') as f:
        for ln in f.readlines():
            g.append(list(ln.strip()))
    return g


def main():
    gg = GoblinGrid(readfile())
    
    steps = 0
    while not gg.is_done():
        steps += 1
        turn_order = gg.get_ids_by_turn_order()
        for id, row, col, hp, type in turn_order:
            # if gg.is_done():
            #     break
            if type == 'E':
                gg.do_turn(gg.elves.get(id))
            else:
                gg.do_turn(gg.goblins.get(id))
    
    if gg.elves:
        score = sum([e['hp'] for e in gg.elves.values()])
    else:
        score = sum(e['hp'] for e in gg.goblins.values())
    score = score * (steps - 1)
    print('s', score, steps)

main()