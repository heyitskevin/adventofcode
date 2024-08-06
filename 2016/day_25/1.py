import re

def func(x):
    a = 0
    c = 2
    b = x
    while b:
        b = b - 1
        c = c  - 1
        if c == 0:
            a = a + 1
            c = 2
    b = 2
    while c:
        b = b -1
        c = c - 1
    
    return b

# floor divide odd emits one, floor divide even emits zero
# want something that starts floor divide even, ends floor divide odd

def count_thingies():
    adder = 1
    base = 15 * 170
    toggle = 0
    arr = []
    while True:
        t = adder + base
        while func(t) == toggle:
            arr.append(str(func(t)))
            t = t // 2
            if toggle == 1:
                toggle = 0
            else:
                toggle = 1
        if t == 0 or t == 1:
            break
        adder += 1
    print(t, adder, adder +  base)
    print("".join(arr))
# count_thingies()

# for i in range(20):
#     print(i, func(i))

def string_like_matcher(start_number):
    s = ""
    while start_number > 0:
        if start_number % 2 == 1:
            s += '1'
        else:
            s += '0'
        start_number = start_number // 2
    return s

ix = 15*170
s = string_like_matcher(ix)

while not re.match(r'^(01)*$', s):
    ix += 1
    s = string_like_matcher(ix)
print(ix, ix - (15 * 170))
    

# string_like_matcher(5)