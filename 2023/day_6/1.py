"""
Count the number of ways you can beat the given race record
"""
import math
FILENAME = 'input.txt'

def parse():
    with open(FILENAME) as f:
        lns = f.readlines()
        times = [int(x) for x in lns[0].split(':')[1].split(' ') if x]
        distances = [int(y) for y in lns[1].split(':')[1].split(' ') if y]
    return times, distances, len(times)

def get_ways_to_win(t, d):
    # You win the race if charge_time * remaining_time > current_distance
    # Because charge_time = boat_speed and speed * time = distance
    res = 0
    for charge_time in range(t+1):
        tot = charge_time ** 2 - t*charge_time + d
        if tot < 0:
            res += 1
    return res


def quadratic(t, d):
    root = math.sqrt(t**2 - 4*d)
    solns = (t + root)/ 2 , (t - root) / 2
    return int(math.floor(solns[0]) - math.ceil(solns[1])) + 1

def func():
    times, distances, races = parse()
    res = 1
    quad = 1
    for ix in range(races):
        q = quadratic(times[ix], distances[ix])
        r = get_ways_to_win(times[ix], distances[ix])
        quad *= q
        res *= r
    print(res, quad)

func()

