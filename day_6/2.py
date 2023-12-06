FILENAME = 'input.txt'

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

def func():
    times, distances = parse()
    one_time = int(''.join(times))
    one_dist = int(''.join(distances))
    print(times, distances, one_time, one_dist)
    res = get_ways_to_win(one_time, one_dist)
    print(res)

func()