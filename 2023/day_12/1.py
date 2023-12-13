import re
import itertools
FILENAME = 'input.txt'

def read_input():
    with open(FILENAME) as f:
        return [(x[0], tuple([int(y) for y in x[1].split(',')])) for x in [ln.strip().split(' ') for ln in f]]


def count_valid_permutations(sequence, arrangements):
    sequence = ["\\.+#{" + str(c) + "}" for c in sequence]
    sequence[0] = sequence[0][3:]
    pattern = rf"^\.*{''.join(sequence)}\.*$"
    count = sum(1 for arrangement in arrangements if re.match(pattern, arrangement))
    return count


def num_arrangements(springs, records):
    wildcard_positions = []
    for ix, s in enumerate(springs):
        if s == '?':
            wildcard_positions.append(ix)
    bag = ["#", "."]
    all_arrangements = itertools.product(bag, repeat=len(wildcard_positions))
    populated_arrangements = []
    for arr in all_arrangements:
        x = list(springs)
        for ix, val in zip(wildcard_positions, arr):
            x[ix] = val
        populated_arrangements.append(''.join(x))
    
    return count_valid_permutations(records, populated_arrangements)
    

def func():
    data = read_input()
    tot = 0
    for elem in data:
        springs, records = elem
        tot += num_arrangements(springs, records)
    print(tot)

func()