FILENAME = 'input.txt'

# from z3 import *
from itertools import combinations, product
def readfile():
    d = {}
    with open(FILENAME) as f:
        for ln in f.read().split('\n'):
            cookie, stats = ln.split(':')
            d[cookie.strip()] = {}
            for s in stats.split(','):
                attr, val = s.strip().split(' ')
                d[cookie.strip()][attr.strip()] = int(val)
    return d

def func():
    data = readfile()
    sol = 0
    range_values = range(1, 98)

    c = product(range_values, repeat=4)
    valid_arrangements = [cc for cc in c if sum(cc) == 100]
    print(f'found {len(valid_arrangements)}')
    for arr in valid_arrangements:
        sugar, sprinkles, candy, chocolate = arr
        capacity = (data['Sugar']['capacity'] * sugar) + (data['Sprinkles']['capacity'] * sprinkles) + (data['Candy']['capacity'] * candy) + (data['Chocolate']['capacity'] * chocolate)
        durability = (data['Sugar']['durability'] * sugar) + (data['Sprinkles']['durability'] * sprinkles) + (data['Candy']['durability'] * candy) + (data['Chocolate']['durability'] * chocolate)
        flavor = (data['Sugar']['flavor'] * sugar) + (data['Sprinkles']['flavor'] * sprinkles) + (data['Candy']['flavor'] * candy) + (data['Chocolate']['flavor'] * chocolate)
        texture = (data['Sugar']['texture'] * sugar) + (data['Sprinkles']['texture'] * sprinkles) + (data['Candy']['texture'] * candy) + (data['Chocolate']['texture'] * chocolate)
        calories = (data['Sugar']['calories'] * sugar) + (data['Sprinkles']['calories'] * sprinkles) + (data['Candy']['calories'] * candy) + (data['Chocolate']['calories'] * chocolate)
        if capacity <= 0 or durability <= 0 or flavor <= 0 or texture <= 0 or calories != 500:
            continue
        else:
            new_sol = capacity*durability*flavor*texture
            sol = max(sol, new_sol)
    print('final total score', sol)


func()
