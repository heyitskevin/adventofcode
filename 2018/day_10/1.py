def readfile():
    r = []
    max_x = 0
    max_y = 0
    min_x = 1
    min_y = 1
    with open('input.txt') as f:
        for ln in f.readlines():
            p, v = ln.split('velocity=')
            px, py = p.split('position=')[-1].strip()[1:-1].split(',')
            vx, vy = v.strip()[1:-1].strip().split(',')
            px, py = int(px), int(py)
            vx, vy = int(vx), int(vy)
            max_x = max(px, max_x)
            max_y = max(py, max_y)
            min_x = min(px, min_x)
            min_y = min(py, min_y)
            r.append((
                (px, py),
                (vx, vy)
            ))
    return r, (max_x, max_y), (min_x, min_y)

def get_all_orphans(current_coords): # False: No Orphans, True: One Orphan
    orphans = False
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for x, y in current_coords:
        for dx, dy in dirs:
            if ((x + dx), (y + dy)) in current_coords:
                break
            else:
                return True
    return orphans

def make_time_step(coords, velocity, time_step=1):
    px, py = coords
    vx, vy = velocity
    n_x = px + (vx * time_step)
    n_y = py + (vy * time_step)

    return (n_x, n_y)

def get_height_minmax(points):
    min_y = 10000000000
    max_y = 0
    max_x = 0
    min_x = 10000000000
    for x, y in points:
        min_y = min(min_y, y)
        max_y = max(max_y, y)
        max_x = max(max_x, x)
        min_x = min(min_x, x)
    return max_y, min_y, max_x, min_x

def plot_points(min_x, max_x, min_y, max_y, pts):
    width = max_x - min_x
    height = max_y - min_y
    res = [[' ' for _ in range(width + 1)] for __ in range(height + 1)]
    for x, y in pts:
        res[y - min_y][x - min_x] = "*"
    return '\n'.join(''.join(r) for r in res)

def main():
    data, max_coords, min_coords = readfile()
    size = len(data)
    pos, vel = [], []
    for dp, dv in data:
        pos.append(dp)
        vel.append(dv)
    time = 1
    height_diff = max_coords[1] - min_coords[1]
    maxy, miny, maxx, minx = 0,0,0,0
    for t in range(1,20000):
        arr = [
            make_time_step(pos[ix], vel[ix], t) for ix in range(size)
        ]
        maxy, miny, maxx, minx = get_height_minmax(arr)
        new_height_diff = maxy - miny
        if new_height_diff < height_diff:
            height_diff = new_height_diff
        else:
            print('min found', t)
            s = plot_points(minx, maxx, miny, maxy, arr)
            print(s)
            break
    print(plot_points(minx, maxx, miny, maxy, [
            make_time_step(pos[ix], vel[ix], t - 1) for ix in range(size)
        ]))
    return time
# I hated this problem so much so I'm not gonna clean it up
print(main())