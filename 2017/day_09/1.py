FILENAME = 'input.txt'

def readfile():
    with open(FILENAME) as f:
        return f.read().strip()
    
def func():
    stream = readfile()
    score = 0
    curly = []
    angle = False
    ignore = False
    for ix, chara in enumerate(stream):
        if ignore:
            ignore = False
            continue
        if chara == '!':
            ignore = True
            continue
        if not angle:
            if chara == '{':
                curly.append(chara)
            if chara == '}':
                score += len(curly)
                curly.pop(-1)
        if chara == '<':
            if angle:
                continue
            else:
                angle = True
        if chara == '>':
            angle = False
    return score

print(func())