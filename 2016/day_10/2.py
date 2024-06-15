FILENAME = 'input.txt'

def read_file():
    inst = []
    v = []
    with open(FILENAME) as f:
        for ln in f.read().split('\n'):
            if 'value' in ln:
                v.append(ln.strip())
            else:
                inst.append(ln.strip())
    return inst, v


def mapify(bot_dirs):
    m = {}
    mm = {}
    for d in bot_dirs:
        k, rest = d.split(" gives low to ")
        b1, b2 = rest.split(" and high to ")
        m[k] = [b1, b2]
        mm[k] = []
        mm[b1] = []
        mm[b2] = []
    return m, mm


def valuify(vals):
    s = []
    for v in vals:
        x, b = v.split(" goes to ")
        x = int(x.split(" ")[-1])
        s.append((b, x))
    return s


def func():
    bot_dirs, values = read_file()
    lowhigh_map, val_map = mapify(bot_dirs)
    v = valuify(values)
    for b, vv in v:
        val_map[b].append(vv)
    # Hard code the start to bot 17 rather than finding it b/c quicker
    q = ["bot 17"]
    visited = set()
    
    while q:
        bot_id = q.pop(0)
        if bot_id in visited:
            continue
        visited.add(bot_id)
        low = lowhigh_map[bot_id][0]
        high = lowhigh_map[bot_id][1]

        low_val = val_map[bot_id][0]
        high_val = val_map[bot_id][1]
        if low_val > high_val:
            low_val, high_val = high_val, low_val

        val_map[low].append(low_val)
        val_map[high].append(high_val)
        if len(val_map[low]) > 1:
            q.append(low)
        if len(val_map[high]) > 1:
            q.append(high)
    print("propogated")
    print(val_map["output 0"][0] * val_map["output 1"][0] * val_map["output 2"][0] )

func()