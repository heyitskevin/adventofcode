import math
from collections import defaultdict

NUM_PRESENTS = 29000000

def get_presents_by_house_number(h):
    p = 0
    for divisor in range(1, int(math.sqrt(h))+1):
        if h % divisor == 0:
            # Janky if logic here that makes sense at the time b/c I built it out iteratively
            # Can be flattened for sure
            if not (h > (50 * divisor)):
                p += divisor
            if not (h > (50 * (h // divisor))):
                p += h // divisor
    return p * 11


def func(min_presents):
    house = int(math.sqrt(min_presents)) # arbitrary guess
    while get_presents_by_house_number(house) < min_presents:
        house += 1
    print(house)


func(NUM_PRESENTS)

