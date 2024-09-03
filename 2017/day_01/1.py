FILENAME = "input.txt"

def read_file():
    with open(FILENAME) as f:
        return f.read().strip()
    
def func():
    s = read_file()
    res = 0
    for ix in range(len(s)):
        if ix == len(s) - 1:
            nx = s[0]
        else:
            nx = s[ix+1]
        if s[ix] == nx:
            res += int(s[ix])
    return res


print(func())