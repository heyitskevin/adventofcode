import copy

def readfile():
    rob = []
    with open('input.txt') as f:
        for ln in f.read().split('\n'):
            pos, vel = ln.split(' ')
            px, py = pos.strip().split('=')[1].split(',')
            vx, vy = vel.strip().split('=')[1].split(',')
            rob.append(((int(px), int(py)), (int(vx), int(vy))))
    return rob


def do_step(config, curr_rob, width, height):
    new_rob = {}
    for robot, position in curr_rob.items():
        new_rob[robot] = {
            "pc": (position["pc"] + config[robot]['vc']) % width,
            "pr": (position["pr"] + config[robot]['vr']) % height
        }
        
    return new_rob


def listify(d):
    res = []
    for k, v in d.items():
        res.append((v['pc'], v['pr']))
    return res

def show_bots_on_grid(grid_width, grid_height, bot_positions, pprint=False):
    g = [['.' for _ in range(grid_width)] for __ in range(grid_height)]
    for k, bot in bot_positions.items():
        row = bot['pr']
        col = bot['pc']
        g[row][col] = 'X'
    if pprint:
        for row in g:
            print(''.join(row))
    return '\n'.join([''.join(r) for r in g])
    
def count_steps(grid_state):
    s = set()
    for k, v in grid_state.items():
        s.add((v['pc'], v['pr']))
    return len(s)

def main():
    data = readfile()
    robots = {}
    start = {}
    for ix in range(len(data)):
        robots[ix] = {
            "pc": data[ix][0][0],
            "pr": data[ix][0][1],
            "vc": data[ix][1][0],
            "vr": data[ix][1][1]
        }
        start[ix] = {
            "pc": data[ix][0][0],
            "pr": data[ix][0][1],
        }
    height = 103
    width = 101
    steps = 0

    # From reddit: Every bot is in a unique position. This was a whacky problem
    while count_steps(start) != len(robots):
        start = do_step(robots, start, width, height)
        steps += 1
    


    return steps

print(main())

