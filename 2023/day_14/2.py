FILENAME = 'input.txt'


import pprint

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

def tilt_array_south(arr):
    flipped = arr[::-1]
    new_arr = tilt_array_north(flipped)
    return new_arr[::-1]

def tilt_array_east(arr):
    turned = transpose(arr)
    new_arr = tilt_array_south(turned)
    return transpose(new_arr)

def tilt_array_west(arr):
    turned = transpose(arr)
    new_arr = tilt_array_north(turned)
    return transpose(new_arr)

def cycle(arr):
    return tilt_array_east(
        tilt_array_south(
            tilt_array_west(
                tilt_array_north(arr)
            )
        )
    )

def score_array(arr):
    score = 0
    dist = len(arr)
    for ix, row in enumerate(arr):
        for col in row:
            if col == 'O':
                score += dist - ix
    return score

def stringify(arr):
    return '\n'.join([''.join([rr for rr in row]) for row in arr])

def big_cycle(arr):
    position = arr
    s_pos = stringify(position)
    visited = {} # position, counter
    visited[s_pos] = 0
    for i in range(1, 10000000001):
        position = cycle(position)
        stringed = stringify(position)
        if stringed in visited:
            return position, visited[stringed], i, visited
        else:
            visited[stringed] = i

def func():
    arr = read_file()
    arr, first_visit, current_visit, mapping = big_cycle(arr)
    cycle_length = current_visit - first_visit
    bignum = 1000000000
    remainder = (bignum - first_visit) % cycle_length
    mapping = {v: k for k, v in mapping.items()}
    arr_str = mapping[first_visit + remainder]
    final = [list(ln) for ln in arr_str.split('\n')]
    
    score = score_array(final)

    print(score)

func()