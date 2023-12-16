FILENAME = 'input.txt'

from collections import defaultdict

def read_file():
    with open(FILENAME) as f:
        return [list(ln) for ln in f.read().split('\n')]
    
def transpose(arr):
    # short circuits at shortest nested list if table is jagged:
    return list(map(list, zip(*arr)))

def tilt_array_north(arr):
    copy_arr = [['.' for _ in range(len(arr[0]))] for __ in range(len(arr))]
    
    for column_index in range(len(arr[0])):
        current_base = 0
        for row_index in range(len(arr)):
            element = arr[row_index][column_index]
            if element == 'O':
                copy_arr[current_base][column_index] = element
                current_base += 1
            elif element == '#':
                current_base = row_index + 1
                copy_arr[row_index][column_index] = element
    return copy_arr

def score_array(arr):
    score = 0
    dist = len(arr)
    for ix, row in enumerate(arr):
        for col in row:
            if col == 'O':
                score += dist - ix
    return score


def func():
    data = read_file()
    arr = tilt_array_north(data)
    score = score_array(arr)
    print(score)

func()