FILENAME = 'input.txt'
# You will not encounter any strings containing numbers.
import json

def read_file():
    with open(FILENAME) as f:
        return json.loads(f.read())

def recursive_items(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield from recursive_items(value)
        else:
            yield (key, value)

def func():
    tot = 0
    start_ix = 0
    next_ix = start_ix + 1
    with open(FILENAME) as f:
        str_data = f.read()
    while start_ix < len(str_data) - 1:
        ch = str_data[start_ix:next_ix]
        if ch.isnumeric():
            next_ix += 1
        else:
            if next_ix - 1 - start_ix > 0:
                p = int(str_data[start_ix:next_ix - 1])
                if str_data[start_ix - 1] == '-':
                    p = -1 * p
                tot += p
            start_ix = next_ix
            next_ix = start_ix + 1
    print(tot)
func()