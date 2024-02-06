INPUT = 'hepxcrrq'
alpha = 'abcdefghijklmnopqrstuvwxyz'

import re

def character_adder(s: str):
    ix_last = alpha.index(s[-1])
    ix_next = ix_last + 1
    if ix_next == 26:
        # z character, build in reverse
        carry = True
        new_string = 'a'
        while carry:
            curr_chara = s[-(len(new_string) + 1)]
            if curr_chara == 'z':
                new_string = 'a' + new_string
            else:
                carry = False
                new_chara = alpha[alpha.index(curr_chara) + 1]
                new_string = new_chara + new_string
                new_string = s[:-(len(new_string))] + new_string
        return new_string
    else:
        return s[:-1] + alpha[ix_next]

def checker(pw):
    if 'i' in pw or 'o' in pw or 'l' in pw:
        return False
    double_pattern = r'(?:(\w)\1.*(\w)\2)|(?:(\w)\3.*(\w)\4)'
    if not re.search(double_pattern, pw):
        return False
    for window in range(0, 24):
        sub = alpha[window: window+3]
        if sub in pw:
            return True
    return False

def func():
    test = INPUT
    while not checker(test):
        test = character_adder(test)
    print(test)

# func()
# Part 2: Splitting this out for readability
def func2():
    test = character_adder('hepxxyzz')
    while not checker(test):
        test = character_adder(test)
    print(test)

func2()