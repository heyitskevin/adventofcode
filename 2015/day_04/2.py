PUZZLE_INPUT = 'iwrupvqb'

import hashlib
import time

def func():
    post = 0
    s = ''
    # six zeroes instead of 5
    while s[:6] != '000000':
        new_str = f'{PUZZLE_INPUT}{post}'
        print(new_str)
        s = hashlib.md5(str.encode(new_str)).hexdigest()
        post += 1
    print(post - 1)


print('start naive')
s = time.time()
# func()
e = time.time()
print('end naive', e - s)

# ans : 9958218

import multiprocessing

def parallel_approach(block_start, block_end):
    s = ''
    for i in range(block_start, block_end + 1):
        if s[:6] == '000000':
            print('found', i - 1)
            multiprocessing.Process.terminate()
        else:
            new_str = f'{PUZZLE_INPUT}{i}'
            s = hashlib.md5(str.encode(new_str)).hexdigest()


# This multithreading p fucky wucky
# def multi():
#     num_cpu = multiprocessing.cpu_count() - 1
#     pool = multiprocessing.Pool(processes=num_cpu)
#     pool.starmap(func=parallel_approach, iterable=[
#         ((i-1)*10000000,i*10000000) for i in range(1000)
#     ])
#     pool.close()

# if __name__ == "__main__":
#     print('multithreading')
#     s = time.time()
#     multi()
#     e = time.time()
#     print('end multi', e - s)