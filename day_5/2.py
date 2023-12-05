"""
START FROM LOCATION AND GO BACKWARDS UP THE RELATIONSHIP
"""

FILENAME = 'example.txt'

def parse_map(map_block):
    m = {}
    for ln in map_block:
        dest, source, rng = ln
        m[(source, rng)] = dest
    return m

def reverse_parse_map(map_block):
    m = {}
    for ln in map_block:
        dest, source, rng = ln
        m[(dest, rng)] = source
    return m

def read_almanac():
    almanac = {}
    with open(FILENAME) as f: # regex parsing im kms
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
    s = almanac.pop('seeds').pop()
    seed = s[0::2]
    loc = s[1::2]
    seeds = []
    for ix, v in enumerate(seed):
        seeds.append((v, v+loc[ix]))
    return seeds, almanac

def func():
    seeds, alm = read_almanac()
    print(alm)
    al_maps = []
    for k, v in alm.items():
        m = reverse_parse_map(v)

        print(f"REVERSE-{k}", m)
        al_maps = [m] + al_maps
    print(al_maps)

func()