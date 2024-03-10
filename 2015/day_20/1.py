import math

NUM_PRESENTS = 29000000

def get_presents_by_house(house_number):
    div = int(math.sqrt(house_number)) + 1
    r = 0
    for e in range(1, div):
        if  house_number % e == 0:
            r += 10 * e
            r += 10 * (house_number // e)
    return r

def func(presents):
    # Brute force search starting from arbitrary guesstimate
    h = int(math.sqrt(presents/10)) 
    while get_presents_by_house(h) < presents:
        h += 1
    print(h)


func(NUM_PRESENTS)