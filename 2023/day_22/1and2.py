FILENAME = 'input.txt'

import itertools
import pprint
from collections import defaultdict

def read_file():
    r = []
    with open(FILENAME) as f:
        x = [ln.strip().split('~') for ln in f.read().split('\n')]

        for e in x:
            e1, e2 = e
            e1 = tuple([int(y) for y in e1.split(',')])
            e2 = tuple([int(z) for z in e2.split(',')])
            r.append((e1, e2))
    return r

def build_block_graph(block_list):
    map_supported = {block: set() for block in block_list} # Key supports all values
    for ix, b in enumerate(block_list):
        s, e = b
        # Take advantage of nice formatting so we don't have to check pos/neg range
        
        xy = itertools.product(range(s[0], e[0]+1), range(s[1], e[1]+1))
        xy = {
            k: False for k in xy
        } # Hash map for each coordinate of the block in the XY plane and if it has or does not have elements directly above it
        
        for above_block in block_list[ix+1:]:
            ss, ee = above_block
            above_xy = itertools.product(range(ss[0], ee[0]+1), range(ss[1], ee[1]+1))
            for coord in above_xy:
                if all([v for v in xy.values()]):
                    break # This block is full go next
                elif coord in xy and not xy[coord]:
                    xy[coord] = above_block
            if all([v for v in xy.values()]):
                # Duplicate check? IDK
                break # This block is full go next
        for k, v in xy.items():
            if v:
                map_supported[b].add(v)
    return map_supported

def get_zappable(support_map):
    # A block is zappable if for each of its supports some other block is supporting it
    # OR It is supporting no blocks
    zappable = 0
    for k, v in support_map.items():
        if len(v) == 0:
            zappable += 1
            continue
        all_zappable = [False for _ in range(len(v))]
        for ix, above_block in enumerate(v):
            for kk, vv in support_map.items():
                if k[0][2] > kk[0][2]:
                    continue
                if k == kk: # Hit identical block, ignore
                    continue 
                if above_block in vv:
                    all_zappable[ix] = True
                    break
            
        if all(all_zappable):
            zappable += 1
    print('zap1', zappable)

def idk(supported_by, supporter_of):
    z = set()
    for k, v in supporter_of.items():
        if len(v) == 0:
            z.add(k)
        else:
            supp = True
            for b in v:
                # print('sdfs', supported_by.get(b))
                if len(supported_by.get(b, [])) < 2:
                    supp = False
            if supp:
                z.add(k)
    print('zappable2idk', len(z))


def make_supported_by_mapping(support_map):
    # Reverse the support map. The key is the block, the v is all blocks that support it
    new_map = {k: set() for k in support_map}
    for k in new_map:
        for kk, v in support_map.items():
            if k in v:
                new_map[k].add(kk)
    return new_map

# WITH HELP FROM REDDIT
def drop_block(tallest, block):
    s, e = block
    coords = itertools.product(range(s[0], e[0] + 1), range(s[1], e[1] + 1))
    highest_z = max(
        tallest[c] for c in coords
    )
    z_diff = max(s[2] - highest_z - 1, 0)
    return (s[0], s[1], s[2] - z_diff), (e[0], e[1], e[2] - z_diff)

def drop_block_list(block_list): 
    tallest_at_coordinate = defaultdict(int)
    new_tower = []
    drops = 0
    for b in block_list:
        block_start, block_end = drop_block(tallest_at_coordinate, b)
        if block_start != b[0]:
            drops += 1
        new_tower.append((block_start, block_end))
        coords = itertools.product(range(b[0][0], b[1][0] + 1), range(b[0][1], b[1][1] + 1))
        for xy in coords:
            tallest_at_coordinate[xy] = block_end[2]
    return drops, new_tower



def func():
    bl = read_file()
    # Input is nice in that the lower Z axis end always is in the first element
    # The data set B is formatted nicely such that every second coordinate is strictly larger than every first
    bl = sorted(bl, key=lambda x: x[0][2]) # Sort in ascending Z axis from 1 -> max

    _, new_tower = drop_block_list(bl)
    z = 0
    p2 = 0 # Part 2 
    for ix in range(len(new_tower)):
        tower_with_removed_block = new_tower[:ix] + new_tower[ix+1:]
        new_num_drops , _ = drop_block_list(tower_with_removed_block)
        if not new_num_drops:
            z += 1
        else:
            p2 += new_num_drops
    print(z, p2)

func()
