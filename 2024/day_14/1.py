def readfile():
    rob = []
    with open('input.txt') as f:
        for ln in f.read().split('\n'):
            pos, vel = ln.split(' ')
            px, py = pos.strip().split('=')[1].split(',')
            vx, vy = vel.strip().split('=')[1].split(',')
            rob.append(((int(px), int(py)), (int(vx), int(vy))))
    return rob


def safety(robot_start, steps, width, height):
    new_rob = []
    
    for r in robot_start:
        p, v = r
        p_col, p_row = p
        v_col, v_row = v
        pcol_final, prow_final = (p_col + (steps * v_col)) % width, (p_row + steps * (v_row)) % height
        new_rob.append((pcol_final, prow_final))
    
    quadrants = [0, 0, 0, 0]
    for nr in new_rob:
        col, row = nr
        if col < width // 2:
            if row > (height) // 2:
                quadrants[2] += 1
            elif row < height // 2:
                quadrants[0] += 1
        elif col > width // 2:
            if row > (height) // 2:
                quadrants[3] += 1
            elif row < height // 2:
                quadrants[1] += 1

    fact = 1
    
    for q in quadrants:
        fact *= q
    return fact


def main():
    robots = readfile()
    width = 101
    height = 103

    res = safety(robots, 100, width, height)

    return res


print(main())
