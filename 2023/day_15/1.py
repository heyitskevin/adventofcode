FILENAME = 'input.txt'

def read_file():
    with open(FILENAME) as f:
        return f.readline().split(',')
    
def soln(input):
    current_val = 0
    for chara in input:
        ascii_val = ord(chara)
        current_val += ascii_val
        current_val *= 17
        current_val = current_val % 256
    return current_val

def func():
    dat = read_file()
    res = 0
    for elem in dat:
        res +=  soln(elem)
    print(res)

func()