def get_first_int(s: str) -> str:
    for chara in s: # walk forward
        if chara.isnumeric():
            return chara

def get_last_int(s: str) -> str:
    for chara in s[::-1]: # walk backwards
        if chara.isnumeric():
            return chara

def func():
    tot = 0
    with open('./input.txt') as f:
        for line in f:
            line = line.rstrip()
            if line:
                first = get_first_int(line)
                last = get_last_int(line)
                num_as_str = first + last
                num = int(num_as_str)
                tot += num
    return tot

print(func())