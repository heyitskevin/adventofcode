from itertools import combinations
FILENAME = 'input.txt'


# 3 Partition problem at small size 
def read_file():
    packages = []
    with open(FILENAME) as f:
        for ln in f.read().split('\n'):
            packages.append(int(ln))
    return packages

# For all combinations of size N in packages P check if that combination equals to target T
# if not increment N, otherwise, check the next set of partitions(?)

# Target in the minimal amount of packages requires the summing of the largest components.
# First find the minimal amount of packages to reach target, then validate if the remaining elements can be summed to 2 * Target
# Greedily do this from the back forwards

def greedy(packages):
    total = sum(packages)
    target = total // 3
    rev = [x for x in reversed(sorted(packages))] # Sorting is trivial for the given input but matters if our input is unsorted
    base_length = False
    for i in range(1, len(packages) - 1):
        for v in combinations(rev, i):
            if sum(v) < target:
                break
            else:
                base_length = i
        if base_length:
            break
    # With base_length as the starting bucket size, enumerate all valid solutions at base_length
    # If solution doesn't exist at base_length, increment and repeat until we find the first valid solution at length L
    # If multiple solutions at size L use tiebreaker method to resolve
    solutions = []
    
    while not solutions:
        print('working', base_length)
        for combo in combinations(rev, base_length):
            if sum(combo) == target: # First bucket found
                quantum = 1
                for pp in combo:
                    quantum *= pp
                solutions.append((list(combo), quantum))
        base_length += 1
    solutions = sorted(solutions, key= lambda x: x[1])
    print(solutions[0])


# Turnsout NP hard problem is a lot easier when they guarantee existence of a solution
    
def func():
    p = read_file()
    greedy(p)

func()