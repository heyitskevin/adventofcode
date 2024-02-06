input = '1113122113'
# I did this problem before so I'm just copy/pasting

def ones(base, levels):
    prev = base
    print(base)
    for i in range(levels):
        splits = []
        start = 0
        for ix, ch in enumerate(prev):
            if ix > 0:
                if ch != prev[ix-1]:
                    splits.append(prev[start:ix])
                    start = ix
        splits.append(prev[start:])
        nn = ''
        for bunch in splits:
            group = f'{len(bunch)}{bunch[0]}'
            nn += group
        
        print('-----')
        # print(nn)
        prev = nn
        print(len(nn))


# Part 1
# ones(input, 40)
# Part 2
ones(input, 50)