PUZZLE_INPUT = 'iwrupvqb'

import hashlib

def func():
    post = 0
    s = ''
    while s[:5] != '00000':
        new_str = f'{PUZZLE_INPUT}{post}'
        print(new_str)
        s = hashlib.md5(str.encode(new_str)).hexdigest()
        post += 1
    print(post - 1)

func()