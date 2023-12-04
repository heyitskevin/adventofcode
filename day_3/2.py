"""
    A gear is any * symbol that is adjacent to exactly TWO part numbers
    Its gear ratio is the result of multiplying these two numbers together
    Find the gear ratio of every gear and add them up
"""
import copy

def build_array_from_input():
    arr = []
    with open('input.txt') as f:
        for ln in f:
            arr.append(list(ln.rstrip()))
        f.close()
    return arr


def is_symbol(element):
    return element not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']

def is_gear(element): # Because copy/paste is faster than typing
    return element == '*'

def get_whole_number(r, c, a):
     # Go left and right from r,c in array a and find the where the number stops and mark visited
    # Vistied nodes should be marked with "." character
    digits = [a[r][c]]
    a[r][c] = '.'
    start = c
    # go left
    while start > 0:
        start = start - 1
        elem = a[r][start]
        if not elem.isdigit():
            break
        digits = [elem] + digits
        a[r][start] = '.'
    # go right
    start = c
    while start < len(a[r]) - 1:
        start = start + 1
        elem = a[r][start]
        if not elem.isdigit():
            break
        digits.append(elem)
        a[r][start] = '.'
    return int(''.join(digits))


def peek_neighbors(r, c, ar):
    gears = []
    a = copy.deepcopy(ar) # not mem efficient, we would slice it if we cared
    # go up
    if r > 0 and a[r-1][c].isdigit():
        gears.append(get_whole_number(r-1, c, a))
    # go down
    if r < len(a) - 1 and a[r+1][c].isdigit():
        gears.append(get_whole_number(r+1, c, a))
    # go left
    if c > 0 and a[r][c-1].isdigit():
        gears.append(get_whole_number(r, c-1, a))
    # go right
    if c < len(a[r]) - 1 and a[r][c+1].isdigit():
        gears.append(get_whole_number(r, c+1, a))

    # diagonals
    # go up right
    if r > 0 and c < len(a[r]) - 1 and a[r-1][c+1].isdigit():
        gears.append(get_whole_number(r-1, c+1, a))
    # go up left
    if r > 0 and c > 0 and a[r-1][c-1].isdigit():
        gears.append(get_whole_number(r-1, c-1, a))
    # go down right
    if r < len(a) -1 and c < len(a[r]) - 1 and a[r+1][c+1].isdigit():
        gears.append(get_whole_number(r+1, c+1, a))
    # go down left
    if r < len(a) - 1 and c > 0  and a[r+1][c-1].isdigit():
        gears.append(get_whole_number(r+1, c-1, a))
    
    if len(gears) == 2:
        return gears[1] * gears[0]
    return 0
    
def func():
    arr = build_array_from_input()
    total = 0
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            elem = arr[row][col]
            if is_gear(elem):
                total += peek_neighbors(row, col, arr,)
    print(total)

func()