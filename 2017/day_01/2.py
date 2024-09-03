FILENAME = "input.txt"

def read_file():
    with open(FILENAME) as f:
        return f.read().strip()
    
def func():
    s = read_file()
    res = 0
    z = len(s)
    for ix in range(z):
        nx = s[(ix + (z//2)) % z]
        if nx == s[ix]:
            res += int(s[ix])
    return res

print(func())