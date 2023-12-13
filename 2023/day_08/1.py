FILENAME = 'input.txt'

def read_input():
    with open(FILENAME) as f:
        directions, rest = f.read().split('\n\n')

        adjacency = {}
        for elem in rest.split('\n'):
            k, v = elem.split('=')
            adjacency[k.strip()] = [x.strip() for x in v.strip()[1:-1].split(',')]
        return directions, adjacency

def func():
    directions, neighbors = read_input()
    current = 'AAA'
    steps = 0
    while current != 'ZZZ':
        curr_direction = directions[steps%len(directions)]
        l_r = 0 if curr_direction == 'L' else 1
        current = neighbors[current][l_r]
        steps += 1
    print(steps)



func()