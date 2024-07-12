# Python only b/c MD5 hashing sigh
import hashlib

open_doors = 'bcdef'
locked_doors = 'a1234567890'
VAULTSIZE = 4

FILENAME = 'input.txt'

def read_file():
    with open(FILENAME) as f:
        return f.read().strip()
    
def func(p_input):
    initial_len = len(p_input)
    target = (VAULTSIZE-1, VAULTSIZE-1)
    q = [(p_input, (0,0))]
    LETTERS = ['U', 'D', 'L', 'R']
    mv = [(0, -1), (0, 1), (-1, 0), (1,0)]
    res = []
    while q:
        current, xy = q.pop(0)
        if xy == target:
            res.append((len(current) - initial_len, current[initial_len:]))
            continue
        s = hashlib.md5(str.encode(current)).hexdigest()
        dirs = s[:4]
        for (ix, c) in enumerate(dirs):
            if c in open_doors:
                new_path = current + LETTERS[ix]
                x = xy[0] + mv[ix][0]
                y = xy[1] + mv[ix][1]
                if x in range(0,VAULTSIZE) and y in range(0, VAULTSIZE):
                    q.append((new_path, (x,y)))
    return max(res, key= lambda x: x[0])
        
        


p = read_file()
print(func(p))