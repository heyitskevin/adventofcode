def readfile():
    with open('input.txt') as f:
        return f.read().strip()
    

def main():
    d = readfile()
    
    disk_id = 0
    is_file = True
    filestring = []
    dots = 0
    for character in d:
        if is_file:
            for _ in range(int(character)):
                filestring.append(str(disk_id))
            disk_id += 1
        else:
            for _ in range(int(character)):
                dots += 1
                filestring.append('.')
        
        is_file = not is_file
        
    back = []
    back_ix = len(filestring) - 1
    while len(back) < dots:
        if filestring[back_ix] != '.':
            back.append(filestring[back_ix])
        back_ix -= 1
    compressed = list(filestring)
    
    while back:
        for ix, v in enumerate(compressed):
            if v == '.':
                compressed[ix] = back.pop(0)
    compressed = compressed[:-dots]
    
    checksum = 0
    for ix, character in enumerate(compressed):
        if character != '.':
            checksum += (ix * int(character))
    
    return checksum

print(main())