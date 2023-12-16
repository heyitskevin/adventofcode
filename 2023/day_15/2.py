FILENAME = 'input.txt'

def read_file():
    with open(FILENAME) as f:
        return f.readline().split(',')
    
def hash_algo(input):
    current_val = 0
    for chara in input:
        ascii_val = ord(chara)
        current_val += ascii_val
        current_val *= 17
        current_val = current_val % 256
    return current_val

def do_lens_thing(data):
    boxes = {k: [] for k in range(256)}
    for instruction in data:
        if '=' in instruction:
            lens_label, lens = instruction.split('=')
            
            box_ix = hash_algo(lens_label)
            lenses = boxes[box_ix]
            lens_ix = -1
            for ix, l in enumerate(lenses):
                if lens_label in l.split(' '):
                    lens_ix = ix
                    break
            if lens_ix != -1:
                lenses[lens_ix] = f"{lens_label} {lens}"
            else:
                lenses.append(f"{lens_label} {lens}")
            boxes[box_ix] = lenses
        elif '-' in instruction:
            lens_label = instruction.split('-')[0]
            box_ix = hash_algo(lens_label)
            lenses = boxes[box_ix]
            lens_ix = -1
            for ix, l in enumerate(lenses):
                if lens_label in l.split(' '):
                    lens_ix = ix
                    break
            if lens_ix != -1:
                lenses.pop(lens_ix)
            boxes[box_ix] = lenses
    return boxes

def score(boxes):
    score = 0
    for k, v in boxes.items():
        if len(v) > 0:
            for ix, lens in enumerate(v):
                focal_length = int(lens.split(' ')[1])
                score += (k + 1) * (ix + 1) * focal_length
    return score


def func():
    data = read_file()
    res = do_lens_thing(data)
    s = score(res)
    print(s)

func()
