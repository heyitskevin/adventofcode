import hashlib

DOOR_ID = 'cxdnnyjw'

def func():
    password = ''
    i = 0
    while len(password) < 8:
        next_guess = f"{DOOR_ID}{i}"
        encrypted = hashlib.md5(next_guess.encode('utf-8')).hexdigest()
        if encrypted[:5] == '00000':
            password += encrypted[5]
        i += 1
    print('password', password)

func()