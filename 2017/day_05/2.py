FILENAME = 'input.txt'

def readfile():
    with open(FILENAME) as f:
        return [int(x) for x in f.read().split('\n')]

def func():
    instructions = readfile()
    ix = 0
    steps = 0
    while ix < len(instructions):
        jump = instructions[ix]
        if jump >= 3:
            instructions[ix] -= 1
        else:
            instructions[ix] = jump + 1
        
        steps += 1
        ix += jump
    return steps

print(func())