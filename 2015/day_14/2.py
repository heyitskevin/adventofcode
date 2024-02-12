FILENAME = 'input.txt'

def readfile():
    r = {}
    with open(FILENAME) as f:
        for ln in f.read().split('\n'):
            name, rest = ln.split('can fly')
            name = name.strip()
            rest = rest.strip().split('for')
            speed = rest[0].strip().split(' ')[0]
            stop_duration = rest[-1].strip().split('.')[0].split(' ')[0]
            uptime = rest[1].strip().split(',')[0].strip().split(' ')[0]
            
            r[name] = {
                'speed': int(speed),
                'stop_duration': int(stop_duration),
                'uptime': int(uptime)
            }
    return r

def travel_x(speed, stop_duration, uptime, travel_time):
    dist = speed * uptime
    total_duration = uptime + stop_duration
    full_cycles = travel_time // total_duration
    time_remaining = travel_time - (full_cycles * total_duration)
    total_dist = dist * full_cycles
    if uptime <= time_remaining:
        total_dist += dist
    else:
        total_dist += (speed * time_remaining)
    return total_dist

def func():
    data = readfile()
    race_time  = 2503
    scores = {n: 0 for n in data.keys()}
    for second in range(race_time):
        # Increment travel distances then add scores
        max_dist = 0
        reindeers = []
        for name in data.keys():
            dist = travel_x(
                data[name]['speed'],
                data[name]['stop_duration'],
                data[name]['uptime'],
                second+1
            )
            reindeers.append((name, dist))
            max_dist = max(max_dist, dist)
        for n, d in reindeers:
            if d == max_dist:
                scores[n] += 1
    print(scores)
        
# 1085 too high
func()