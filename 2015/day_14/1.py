FILENAME = 'input.txt'

def readfile():
    r = []
    with open(FILENAME) as f:
        for ln in f.read().split('\n'):
            name, rest = ln.split('can fly')
            name = name.strip()
            rest = rest.strip().split('for')
            speed = rest[0].strip().split(' ')[0]
            stop_duration = rest[-1].strip().split('.')[0].split(' ')[0]
            uptime = rest[1].strip().split(',')[0].strip().split(' ')[0]
            r.append((name, int(speed), int(stop_duration), int(uptime)))
    return r

def func():
    data = readfile()
    total_time = 2503
    distance_travelled = 0
    for row in data:
        name, speed, stop_duration, uptime = row
        dist = speed * uptime
        total_duration = uptime + stop_duration
        full_cycles = total_time // total_duration
        time_remaining = total_time - (full_cycles * total_duration)
        total_dist = dist * full_cycles
        if uptime <= time_remaining:
            total_dist += dist
        else:
            total_dist += (speed * time_remaining)
        distance_travelled = max(distance_travelled, total_dist)
        print(name, full_cycles, time_remaining, total_dist)
    print('max dist', distance_travelled)


func()

