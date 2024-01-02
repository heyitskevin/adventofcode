FILENAME = 'input.txt'
LOWERBOUND = 200000000000000
UPPERBOUND = 400000000000000
# LOWERBOUND = 7
# UPPERBOUND = 27

import itertools

def read_file():
    with open(FILENAME) as f:
        return [[[int(b) for b in a.strip().split(',')] for a in tuple(ln.split('@'))] for ln in f.read().split('\n')]

def solve_x(x1, x2, y1, y2, m1, m2):
   return ((y2 - m2*x2) - (y1 - m1*x1))/(m1 - m2)

def solve_y_given_x(given_x, x1, y1, m1):
    return m1*(given_x - x1) + y1

def get_intersections(data):
    # Parameterized solutions
    total_in_bounds = 0
    for d, d2 in itertools.combinations(data, 2):
        print(d, d2)
        pos, vel = d
        # Ignore Z
        px, py = pos[:2]
        vx, vy  = vel[:2]
        slope = vy/vx # Input is nice so there's no divide by zero cases here
        pos2, vel2 = d2
        px2, py2  = pos2[:2]
        vx2 , vy2 = vel2[:2]
        slope2 = vy2/vx2
        if slope == slope2: # Parallel lines
            continue
        else:
            x_cross = solve_x(px, px2, py, py2, slope, slope2)
            y_cross = solve_y_given_x(x_cross, px, py, slope)
            timex1 = round((x_cross - px)/vx, 8)
            timey1 = round((y_cross - py)/vy, 8)
            timex2 = round((x_cross - px2)/vx2, 8)
            timey2 = round((y_cross - py2)/vy2, 8)
            if LOWERBOUND <= x_cross <= UPPERBOUND:
                if LOWERBOUND <= y_cross <= UPPERBOUND:
                    if timex1 > 0 and timey1 > 0:
                        if timex2 > 0 and timey2 > 0:
                            total_in_bounds += 1

    print(total_in_bounds)
    return total_in_bounds


def func():
    data = read_file()
    get_intersections(data)
    

func() # 23760