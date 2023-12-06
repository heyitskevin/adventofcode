FILENAME = 'input.txt'
import math

def parse():
    with open(FILENAME) as f:
        lns = f.readlines()
        times = [str(x) for x in lns[0].strip().split(':')[1].split(' ') if x]
        distances = [str(y) for y in lns[1].strip().split(':')[1].split(' ') if y]
    return times, distances

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
    times, distances = parse()
    one_time = int(''.join(times))
    one_dist = int(''.join(distances))
    print(times, distances, one_time, one_dist)
    q = quadratic(one_time, one_dist)
    print('----')
    # res = get_ways_to_win(one_time, one_dist)
    # print(res, q)
    print(q)

func()