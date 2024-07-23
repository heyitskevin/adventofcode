# Only doing this day in python b/c it's a pile of string manip and I've already mastered that in C++
from itertools import permutations
FILENAME = "input.txt"

def read_file():
    with open(FILENAME) as f:
        return [ln.strip() for ln in f.read().split('\n')]
    
def get_nodes(full_file):
    return [[l for l in ln.split(" ") if l]for ln in full_file[2:]]

def count_valid_combos(nodes):
    combos = permutations(nodes, 2)
    count = 0
    for a, b in combos:
        # We don't need everything for part 1 but unball it all
        a_name, a_size, a_used, a_avail, a_per = a
        b_name, b_size, b_used, b_avail, b_per = b
        if a_used == "0T":
            continue
        a_used_val = int(a_used[:-1])
        b_avail_val = int(b_avail[:-1])
        if b_avail_val < a_used_val:
            continue
        count += 1
    return count
    
def func():
    d = read_file()
    nodes = get_nodes(d)
    res = count_valid_combos(nodes)
    return res

print(func())

# 952 too low