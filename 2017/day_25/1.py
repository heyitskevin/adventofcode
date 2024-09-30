CHECKSUM = 12919244
from collections import defaultdict
def func():
    tape = defaultdict(int)
    state = 'A'
    steps = 0
    ix = 0
    while steps < CHECKSUM:
        val = tape[ix]
        if state == 'A':
            if val == 0:
                tape[ix] = 1
                ix += 1
                state = 'B'
            else:
                tape[ix] = 0
                ix -= 1
                state = 'C'
        elif state == 'B':
            if val == 0:
                tape[ix] = 1
                ix -= 1
                state = 'A'
            else:
                tape[ix] = 1
                ix += 1
                state = 'D'
        elif state == 'C':
            if val == 0:
                tape[ix] = 1
                ix += 1
                state = 'A'
            else:
                tape[ix] = 0
                ix -= 1
                state = 'E'
        elif state == 'D':
            if val == 0:
                tape[ix] = 1
                ix += 1
                state = 'A'
            else:
                tape[ix] = 0
                ix += 1
                state = 'B'
        elif state == 'E':
            if val == 0:
                tape[ix] = 1
                ix -= 1
                state = 'F'
            else:
                tape[ix] = 1
                ix -= 1
                state = 'C'
        elif state == 'F':
            if val == 0:
                tape[ix] = 1
                ix += 1
                state = 'D'
            else:
                tape[ix] = 1
                ix += 1
                state = 'A'
        
        steps += 1
    return sum(tape.values())

print(func())