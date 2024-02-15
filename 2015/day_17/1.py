MAX_EGGNOG = 150
FILENAME = 'input.txt'

def readfile():
    containers = []
    with open(FILENAME) as f:
        for ln in f.read().split('\n'):
            containers.append(int(ln.strip()))
    return containers
# MISS READ THE PROBLEM DON'T NEED ANY OF THIS BUT KEEPING IT ANYWAY FOR THE FUTURE
# COIN CHANGE MAKING W/ WEIRD VARIABLES B/C I THOUGHT PROBLEM WAS REQUIRING THIS FOR CONTAINERS
# def build_memo_matrix(container_types, r):
#     m = [[0 for _ in range(r+1)] for _ in range(len(container_types) + 1)]
#     for i in range(1, r+1):
#         m[0][i] = float('inf') # default there's no valid config
#     return m

# def make_containers(container_types, target):
#     m = build_memo_matrix(container_types, target)

#     for ix, con in enumerate(container_types, 1): # Start counting from 1 b/c that's what the example is doing
#         for r in range(1, target+1): # Build up solution to target
#             if con == r: # Container is of this size
#                 m[ix][r] = 1
#             elif con > r: # This container is too large for the target
#                 m[ix][r] = m[ix-1][r] # Use the previous solution for making R without the current container
#             else:
#                 # The best way to make this target is the min of using the previous solution for making R or using the solution of making R - container + this one
#                 m[ix][r] = min(m[ix-1][r], 1 + m[ix][r-con]) 
#     return m[-1][-1], m

def get_combos(containers, target):
    valid = []
    def recursive(sub_containers, sub_target, current):
        if sub_target == 0:
            valid.append(current)
        for ix, c in enumerate(sub_containers):
            new_current = current + [c]
            recursive(sub_containers[ix+1:], sub_target-c, new_current)
    recursive(containers, target, [])
    return valid


def func():
    containers = sorted(readfile(), reverse=True)
    combos = get_combos(containers, MAX_EGGNOG)
    # 1 and 2 in the same file
    min_combo = min([len(c) for c in combos])
    min_total = 0
    for cc in combos:
        if len(cc) == min_combo:
            min_total += 1
    print('mt', min_total)
func()