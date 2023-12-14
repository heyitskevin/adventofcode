FILENAME = 'input.txt'

def read_file():
    with open(FILENAME) as f:
        return [[list(ln.strip()) for ln in blck.split('\n')]for blck in f.read().split('\n\n')]

def transpose(arr):
    # short circuits at shortest nested list if table is jagged:
    return list(map(list, zip(*arr)))

def reflect(arr):
    for ix in range(len(arr)-1):
        c_ix = ix
        curr = arr[c_ix]
        m_ix = ix + 1
        mirror = arr[m_ix]
        while curr == mirror:
            c_ix = c_ix - 1
            m_ix = m_ix + 1
            if c_ix < 0 or m_ix >= len(arr):
                return ix + 1
            curr = arr[c_ix]
            mirror = arr[m_ix]
    return False

def get_reflections(arr):
    trans = transpose(arr)

    r = reflect(arr)
    if r:
        return r, 'rows'
    c = reflect(trans)
    if c:
        return c, 'cols'



def func(): 
    rocks = read_file()
    
    summary = 0
    for r in rocks:
        ct, dir = get_reflections(r)
        if dir == 'rows':
            ct = 100 * ct
        summary += ct
    
    print(summary)
    
func()