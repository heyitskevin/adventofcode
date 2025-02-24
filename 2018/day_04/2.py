from datetime import datetime
from collections import defaultdict, Counter

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
    
    for i in d:
        dt, state = i
        if 'begins shift' in state:
            curr_guard = int(state.split('#')[1].split(' ')[0].strip())
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
            if state == 'wakes up':
                time_range = [t for t in range(sleep_time.minute, dt.minute)]
                guards[curr_guard].append(time_range)
                
    # of all guards which asleep the most on the same minute
    max_min = -1
    max_ct = -1
    max_guard = None
    for g, m in guards.items():
        
        ct = Counter()
        for mm in m:
            ct.update(mm)
        
        mx = max(ct, key=ct.get)
        
        if max_ct < ct[mx]:
            max_min = mx
            max_guard = g
            max_ct =ct[mx]
    return max_guard * max_min


print(main())
