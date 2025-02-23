from datetime import datetime
from collections import defaultdict

def readfile():
    res = []
    with open('input.txt') as f:
        for ln in f.read().split('\n'):
            d, state = ln.split(']')
            d = d.strip()[1:]
            state = state.strip()
            d, t = d.split(' ')
            hr, mn = t.strip().split(':')
            yr, mth, dy = d.split('-')
            dt_blob = {
                "year": int(yr),
                "month": int(mth),
                "day": int(dy),
                "hour": int(hr),
                "minute": int(mn)
            }
            res.append((datetime(**dt_blob), state))
                
    return sorted(res, key = lambda x: x[0])


def main():
    d = readfile()
    guards = defaultdict(list)
    guard_mins = defaultdict(int)
    for i in d:
        dt, state = i
        if 'begins shift' in state:
            curr_guard = int(state.split('#')[1].split(' ')[0].strip())
            awake = True
            continue
        else:
            if state == 'falls asleep':
                if dt.hour != 0:
                    sleep_time = datetime.datetime(
                        year=dt.year, 
                        month=dt.month, 
                        day=dt.day + 1, 
                        hour=0, 
                        minute=0
                    )
                else:
                    sleep_time = dt
                awake = False
            if state == 'wakes up':
                awake = True
                time_range = [t for t in range(sleep_time.minute, dt.minute)]
                guards[curr_guard].append(time_range)
                guard_mins[curr_guard] += len(time_range)
    g = max(guard_mins, key=guard_mins.get)
    ct = defaultdict(int)
    for mins in guards[g]:
        for m in mins:
            ct[m] += 1
    mm = max(ct, key=ct.get)
    return g * mm


print(main())
