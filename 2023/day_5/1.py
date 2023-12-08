def parse_map(map_block):
    m = {}
    for ln in map_block:
        dest, source, rng = ln
        m[(source, rng)] = dest
    return m


def convert_source_to_dest(source, m): # don't want to shadow map func
    for k, v in m.items():
        if source in range(k[0], k[0]+k[1]):
            return source + (v - k[0])
    return source

def read_almanac():
    almanac = {}
    with open('input.txt') as f: # regex parsing im kms
        txt = f.read()
    groups = txt.split('\n\n')
    for g in groups:
        key, vals = g.split(':')
        almanac_key = key.split(' ')[0]
        data = []
        for v in vals.strip().split('\n'):
            data.append([
                int(vv.strip()) for vv in v.split(' ')
            ])
        almanac[almanac_key] = data
    # clean up seeds
    almanac['seeds'] = almanac['seeds'].pop()
    return almanac

import collections, sys

def func():
    alm = read_almanac()
    seeds = alm.pop('seeds')
    maps = collections.OrderedDict()
    for k, v in alm.items():
        maps[k] = parse_map(v)
    a = [] 
    a_min = sys.maxsize
    for s in seeds:
        base = s
        for k, v in maps.items():
            base = convert_source_to_dest(base, v)
        a_min = min(a_min, base)
        a.append(base)
    print(a_min)

func()