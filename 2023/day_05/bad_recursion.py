"""
START FROM LOCATION AND GO BACKWARDS UP THE RELATIONSHIP
THIS SOLUTION WORKS EXCEPT FOR V LARGE NUMBERS SO IT'S NOT VALID
"""

FILENAME = 'input.txt'

import copy
from collections import OrderedDict

def reverse_parse_map(map_block):
    m = {}
    for ln in map_block:
        dest, source, rng = ln
        m[(dest, dest+rng, rng)] = source
    # return OrderedDict(sorted(m.items(), key=lambda e: e[0]))
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

def reverse_lookup(rev, almanac_maps):
    # given a location, find its corresponding seed
    current_map = almanac_maps.pop(0)
    for key, val in current_map.items():
        dest_low, dest_high, r = key
        if rev in range(dest_low, dest_high):
            # print('in', [val + rev - dest_low, val, rev, dest_low])
            return val + (rev - dest_low)
    # print('out', rev)
    return rev # If no conversion, return the same number
    

# start at locaiton 0
# traverse up the list
# if the result is not in the range of valid seeds
# start at location 1

def validate_seed(seed, valid_ranges):
    for rn in valid_ranges:
        if seed in range(rn[0], rn[1]):
            return True
    return False

def go_backwards(start, sorted_maps, valid_ranges):
    # print('start', start)
    elem = start
    sorted_maps_copy = copy.copy(sorted_maps)
    while sorted_maps_copy:
        # print('reverse', elem)
        elem = reverse_lookup(elem, sorted_maps_copy)
    if not validate_seed(elem, valid_ranges):
        # print('recur', elem)
        # return go_backwards(start + 1, sorted_maps, valid_ranges)
        return False, start + 1
    else:
        # print('valid', elem)
        return (elem, start)

def func():
    seeds, alm = read_almanac()
    sorted_maps = [] # reverse order list of maps
    for k, v in alm.items():
        m = reverse_parse_map(v)
        sorted_maps = [m] + sorted_maps
    located_seeds = []
    print(seeds)
    # 195554894
    base = 195454894
    finished = False
    while not finished:
        print(base)
        finished, base = go_backwards(base, sorted_maps, seeds)
    
    # a = go_backwards(base, sorted_maps, seeds)
    ###
    # sorted_maps_copy = copy.copy(sorted_maps)
    # reverse = 0
    # while sorted_maps_copy:
    #     print('reverse', reverse)
    #     reverse = reverse_lookup(reverse, sorted_maps_copy)
    # if reverse not in valid_seed_ranges:

    ###

    located_seeds.append((finished, base))
    print('-------')
    return (located_seeds)

print(func())