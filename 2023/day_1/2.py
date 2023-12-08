word_digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

number_map = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}

def get_first_occurrences(s):
    # the index of the array is basically number - 1
    first_occurrences = [(len(s), -1) for x in range(9)] 
    for d in range(1, 10): # 1- 10
        first_occurrences[d-1] = (min(first_occurrences[d-1][0], s.find(number_map[d])), number_map[d])
    return first_occurrences

def firsts(s):
    first_occurrence_indexes = get_first_occurrences(s)
    for ix, chara in enumerate(s):
        if chara.isnumeric():
            min_ix, min_val = min(first_occurrence_indexes, key=lambda t: t[0] if t[0]> -1 else len(s))
            if min_ix > -1 and min_ix < ix:
                return word_digits[min_val]
            else:
                return chara

def get_last_occurrences(s):
    last_occurrences = [(-1, -1) for x in range(9)]
    for d in range(1, 10):
        last_occurrences[d-1] = (max(last_occurrences[d-1][0], s.rfind(number_map[d])), number_map[d])
    return last_occurrences

def lasts(s):
    last_occurrence_indexes = get_last_occurrences(s)
    for ix, chara in enumerate(s[::-1]):
        if chara.isnumeric():
            flipped = len(s) - ix - 1
            max_ix, max_val = max(last_occurrence_indexes, key=lambda t: t[0])
            if max_ix > flipped:
                return word_digits[max_val]
            else:
                return chara

def func():
    tot = 0
    with open('./input.txt') as f:
        for ln in f:
            ln = ln.rstrip()
            if ln:
                first = firsts(ln)
                last = lasts(ln)
                num_str = first + last
                tot += int(num_str)
    return tot

print(func())
