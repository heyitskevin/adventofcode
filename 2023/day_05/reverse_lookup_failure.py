"""
Operate on tuples of ranges rather than elements?
"""

FILENAME = 'input.txt'

import copy
from collections import OrderedDict

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
        m[(dest, dest+rng, rng)] = source
    return OrderedDict(sorted(m.items(), key=lambda e: e[0]))
    return m

def build_location_intervals(hum_to_loc):
    loc_int = []
    for k, dest in hum_to_loc.items():    
        src, rng = k
        loc_int.append((dest, dest+rng))
    loc_int = sorted(loc_int, key=lambda x: x[0])
    if loc_int[0][0] != 0:
        loc_int = [(0, loc_int[0][0])] + loc_int # prepend interval
    return loc_int

def reverse_lookup(rev, almanac_maps):
    # given a location, find its corresponding seed
    current_map = almanac_maps.pop(0)
    for key, val in current_map.items():
        dest_low, dest_high, r = key
        if rev in range(dest_low, dest_high):
            return val + (rev - dest_low)
    return rev # If no conversion, return the same number

def validate_seed(seed, valid_ranges):
    for rn in valid_ranges:
        if seed in range(rn[0], rn[1]):
            return True
    return False

def go_backwards(start, sorted_maps, valid_ranges):
    elem = start
    sorted_maps_copy = copy.copy(sorted_maps)
    while sorted_maps_copy:
        elem = reverse_lookup(elem, sorted_maps_copy)
    return validate_seed(elem, valid_ranges)

def search_interval(low, high, sorted_maps, valid_ranges):
    print('searching interval: ', low, high)
    if low > high:
        return False
    middle = (high + low) // 2
    check_low = go_backwards(low, sorted_maps, valid_ranges)
    check_high = go_backwards(high, sorted_maps, valid_ranges)
    check_middle = go_backwards(middle, sorted_maps, valid_ranges)
    # print({
    #     'check_low': check_low,
    #     'check_high': check_high,
    #     'check_mid': check_middle
    # })
    print('-----')
    if check_low:
        return low
    elif check_middle: # If low is False and middle is True
        return search_interval(low + 1, middle, sorted_maps, valid_ranges)
    elif check_high: # If low and middle are False and high is True
        return search_interval(middle + 1, high, sorted_maps, valid_ranges)
    else: # if all 3 are False
        print('all false')
        return False

def func():
    seeds, alm = read_almanac()
    almaps = {}
    reverse_map_list = []
    for k, v in alm.items():
        mm = parse_map(v)
        m_rev = reverse_parse_map(v)
        almaps[k] = mm
        reverse_map_list.append(m_rev)
    reverse_map_list = reverse_map_list[::-1]
    location_intervals = build_location_intervals(
        almaps.get('humidity-to-location')
    )
    location_intervals = sorted(location_intervals, key=lambda x: x[0])
    res = []
    
    for loc in location_intervals:
        lo, hi = loc
        a_low_location = search_interval(lo, hi, reverse_map_list, seeds)
        if a_low_location:
            # print(lo, hi, a_low_location)
            # print('going backwards')
            # print(go_backwards(82, reverse_map_list, seeds))
            return a_low_location
        res.append(a_low_location)
    res = [r for r in res if r]
    print(res, min(res))

func()