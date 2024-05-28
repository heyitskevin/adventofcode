TARGET_ROW = 2981
TARGET_COL = 3075

ROOT_VAL = 20151125
MULTIPLIER = 252533
DIVIDER = 33554393

def func():
    triangle_base = TARGET_COL + TARGET_ROW - 1 - 1 # Find the value of N adjusted to be smaller than coordinates
    triangle_start = triangle_base * (triangle_base + 1) // 2 # The Nth triangular number

    val = ROOT_VAL
    for _ in range(triangle_start):
        val = val * MULTIPLIER
        val = val % DIVIDER

    additional = TARGET_COL - 1
    for _ in range(additional):
        val = val * MULTIPLIER
        val = val % DIVIDER

    print(val)

    

func()

# 9132360