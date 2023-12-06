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


def convert_source_to_dest(input, m): # don't want to shadow map func
    for dest, src, rng in m:
        if input in range(src, src+rng):
            return input + (dest - src)
    return input

def convert_source_to_dest_as_range(base_start, base_end, m): # don't want to shadow map func
    split_out_ranges = []
    ranges_to_slice = [(base_start, base_end)]
    while ranges_to_slice:
        start, end = ranges_to_slice.pop(0)
        end = end - 1
        for dest, src, rng in m:
            offset = dest - src
            src_end = src + rng
            dest_start = -1
            dest_end = -1
            if start in range(src, src_end) and end in range(src, src_end): # Fully inside this interval
                dest_start = start + offset
                dest_end = end + offset
                split_out_ranges.append((dest_start, dest_end))
                break
            elif start < src and end in range(src, src_end): # Left side out of interval
                dest_start = src + offset
                dest_end = end + offset
                split_out_ranges.append((dest_start, dest_end))
                ranges_to_slice.append((start, src))
                break
            elif start in range(src, src_end) and end > src_end: # Right side out of interval
                dest_start = start + offset
                dest_end = src_end + offset
                split_out_ranges.append((dest_start, dest_end))
                ranges_to_slice.append((src_end, end))
                break
            elif start < src and end >= src_end: # Straddle interval
                dest_start = src + offset
                dest_end = src_end + offset
                split_out_ranges.append((dest_start, dest_end))
                ranges_to_slice.append((start, src))
                ranges_to_slice.append((src_end, end))
                break
        if dest_start == dest_end == -1:
            split_out_ranges.append((start, end))
            break
    return split_out_ranges


def map_all_down(range_start, range_end, almanac):
    alm_data = list(almanac.values())
    input_ranges = [(range_start, range_end)]
    while alm_data:
        curr_alm = alm_data.pop(0)
        new_ir = []
        for ir in input_ranges:
            new_ir += convert_source_to_dest_as_range(ir[0], ir[1], curr_alm)
        input_ranges = new_ir
    return input_ranges



def func():
    seed, almanac = read_almanac()
    res = []
    for seed_range in seed:
        seed_start, seed_end  = seed_range
        res += map_all_down(seed_start, seed_end, almanac)
    min_res = min(res, key=lambda x: x[0])
    print('min', min_res)
func()