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
    accounts = read_file()
    q = list(accounts.values()) # Red doesn't appear at layer 0
    tot = 0
    while q:
        v = q.pop(0)
        if isinstance(v, dict):
            if 'red' in v.values():
                continue
            else:
                q += list(v.values())
        elif isinstance(v, list):
            q += v
        # The only other things are ints and strings
        elif isinstance(v, int):
            tot += v
    print(tot)
    
func()