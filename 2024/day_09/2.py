import copy
def readfile():
    with open('input.txt') as f:
        return f.read().strip()
    

def flatten(filestring):
    res = []
    for arr in filestring:
        for ch in arr:
            res.append(ch)
    return res

def stack(flattened):
    res = []
    ix = 0
    while ix < len(flattened) - 1:
        curr = flattened[ix]
        arr = []
        while ix < len(flattened) and flattened[ix] == curr:
            arr.append(curr)
            ix += 1
        res.append(arr)
    return res

# Some giga long running fuckery pain peko
def attempt_to_move(stacked_list, file_id):
    for s_ix, st in enumerate(stacked_list[::-1]):
        if st[0] == file_id:
            st_l = len(st)
            flat_ix = 0
            for ix, dots in enumerate(stacked_list):
                diff = len(stacked_list) - s_ix
                if ix >= diff:
                    # No valid location
                    return stacked_list
                if dots[0] == '.' and len(dots) >= st_l:
                    # Valid swap location
                    end_ix = flat_ix + st_l
                    f = flatten(stacked_list)
                    arr = f[:flat_ix] + st + f[end_ix:]
                    back_ix_start = sum([len(ss) for ss in stacked_list[:len(stacked_list) - s_ix -1]])
                    
                    for aa in range(back_ix_start, back_ix_start + st_l):
                        arr[aa] = '.'
                    
                    return stack(arr)
                flat_ix += len(dots)


    return stacked_list


def main():
    d = readfile()
    disk_id = 0
    is_file = True
    filestring = []
    for c in d:
        a = []
        if is_file:
            for _ in range(int(c)):
                a.append(str(disk_id))
            disk_id += 1
            
        else:
            for _ in range(int(c)):
                a.append('.')
        is_file = not is_file
        if a:
            filestring.append(a)
    
    k = copy.deepcopy(filestring)
    for did in range(disk_id, -1, -1):
        k = attempt_to_move(k, str(did))
    
    checksum = 0
    for ix, v in enumerate(flatten(k)):
        if v != '.':
            pass
            checksum += (ix * int(v))

    return checksum


print(main())