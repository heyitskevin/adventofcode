from collections import defaultdict
from itertools import permutations, product


NUMPAD = {
    'A': {
        'A': '',
        '0': '<',
        '1': '^<<',
        '2': '<^',
        '3': '^',
        '4': '^^<<',
        '5': '<^^',
        '6': '^^',
        '7': '^^^<<',
        '8': '<^^^',
        '9': '^^^',
        '^': '<',
        '<': 'v<<',
        'v': '<v',
        '>': 'v'
    },
    '0': {
        'A': '>',
        '0': '',
        '1': '<^',
        '2': '^',
        '3': '^>',
        '4': '<^^',
        '5': '^^',
        '6': '^^>',
        '7': '<^^^',
        '8': '^^^',
        '9': '^^^>'
    },
    '1': {
        'A': '>>v',
        '0': 'v>',
        '1': '',
        '2': '>',
        '3': '>>',
        '4': '^',
        '5': '^>',
        '6': '^>>',
        '7': '^^',
        '8': '^^>',
        '9': '^^>>'
    },
    '2': {
        'A': 'v>',
        '0': 'v',
        '1': '<',
        '2': '',
        '3': '>',
        '4': '<^',
        '5': '^',
        '6': '^>',
        '7': '<^^',
        '8': '^^',
        '9': '^^>'
    },
    '3': {
        'A': 'v',
        '0': 'v<',
        '1': '<<',
        '2': '<',
        '3': '',
        '4': '<<^',
        '5': '<^',
        '6': '^',
        '7': '<<^^',
        '8': '<^^',
        '9': '^^'
    },
    '4': {
        'A': 'vv>>',
        '0': 'vv>',
        '1': 'v',
        '2': 'v>',
        '3': 'v>>',
        '4': '',
        '5': '>',
        '6': '>>',
        '7': '^',
        '8': '^>',
        '9': '^>>'
    },
    '5': {
        'A': 'vv>',
        '0': 'vv',
        '1': '<v',
        '2': 'v',
        '3': 'v>',
        '4': '<',
        '5': '',
        '6': '>',
        '7': '<^',
        '8': '^',
        '9': '^>'
    },
    '6': {
        'A': 'vv',
        '0': '<vv',
        '1': '<<v',
        '2': '<v',
        '3': 'v',
        '4': '<<',
        '5': '<',
        '6': '',
        '7': '<<^',
        '8': '<^',
        '9': '^'
    },
    '7': {
        'A': '>>vvv',
        '0': '>vvv',
        '1': 'vv',
        '2': 'vv>',
        '3': 'vv>>',
        '4': 'v',
        '5': 'v>',
        '6': 'v>>',
        '7': '',
        '8': '>',
        '9': '>>'
    },
    '8': {
        'A': 'vvv>',
        '0': 'vvv',
        '1': '<vv',
        '2': 'vv',
        '3': 'vv>',
        '4': '<v',
        '5': 'v',
        '6': 'v>',
        '7': '<',
        '8': '',
        '9': '>'
    },
    '9': {
        'A': 'vvv',
        '0': '<vvv',
        '1': '<<vv',
        '2': '<vv',
        '3': 'vv',
        '4': '<<v',
        '5': '<v',
        '6': 'v',
        '7': '<<',
        '8': '<',
        '9': ''
    },
    '^': {
        'A': '>',
        '^': '',
        '<': 'v<',
        'v': 'v',
        '>': 'v>'
    },
    '<': {
        'A': '>>^',
        '^': '>^',
        '<': '',
        'v': '>',
        '>': '>>'
    },
    'v': {
        'A': '^>',
        '^': '^',
        '<': '<',
        'v': '',
        '>': '>'
    },
    '>': {
        'A': '^',
        '^': '<^',
        '<': '<<',
        'v': '<',
        '>': ''
    }
}

DPAD = {
    'A': {
        'A': '',
        '^': '<',
        '<': 'v<<',
        'v': '<v',
        '>': 'v'
    },
    '^': {
        'A': '>',
        '^': '',
        '<': 'v<',
        'v': 'v',
        '>': 'v>'
    },
    '<': {
        'A': '>>^',
        '^': '>^',
        '<': '',
        'v': '>',
        '>': '>>'
    },
    'v': {
        'A': '>^',
        '^': '^',
        '<': '<',
        'v': '',
        '>': '>'
    },
    '>': {
        'A': '^',
        '^': '^<',
        '<': '<<',
        'v': '<',
        '>': ''
    }
}


def readfile():
    with open('input.txt') as f:
        return f.read().split('\n')
    

visited = {}


def get_moves(curr, nxt, robot_depth):
    if curr == nxt:
        return 1
    next_seq = NUMPAD[curr][nxt]
    return do_seq(next_seq, robot_depth - 1)

def do_seq(sequence, robot_depth):
    if (sequence, robot_depth) in visited:
        return visited[(sequence, robot_depth)]
    s = 0
    if robot_depth == 0:
        s = len(sequence)
    else:
        curr = 'A'
        for ch in sequence:
            next_seq = get_moves(curr, ch, robot_depth)
            curr = ch
            s += next_seq
    visited[((sequence, robot_depth))] = s
    return s


def calc_score(sequence, robot_depth):
    num_sequence = int(sequence[:-1])
    sequence_length = do_seq(sequence, robot_depth)
    return num_sequence * sequence_length


def main():
    codes = readfile()
    res = 0
    for k, v in NUMPAD.items():
        for x, vv in v.items():
            v[x] = vv + 'A'
    
    for code in codes:
        # res += calc_score(code, 3)
        res += calc_score(code, 26)
    return res


print(main())
