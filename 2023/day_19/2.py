FILENAME = 'input.txt'

import copy
import pprint


class Part:
    def __init__(self, x, m ,a ,s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s
    def get_part_val_by_operand(self, operand):
        match operand:
            case 'x':
                return self.x
            case 'm':
                return self.m
            case 'a':
                return self.a
            case 's':
                return self.s

def read_file():
    with open(FILENAME) as f:
        workflows, parts = f.read().split('\n\n')

        return workflowify(workflows.split('\n'))
    
def workflowify(workflows):
    d = {}
    for w in workflows:
        name, instructions = w.split('{')
        instructions = instructions[:-1].split(',')
        d[name] = instructions
    return d

def partsify(parts):
    all_parts = []
    for p in parts:
        p = p[1:-1]
        p = p.split(',')
        args = []
        for elem in p: # Elements are always in XMAS order
            args.append(int(elem.split('=')[1]))
        all_parts.append(Part(*args))
    return all_parts

def search(workflows):
    base = {
        'x': (1, 4000),
        'm': (1, 4000),
        'a': (1, 4000),
        's': (1, 4000)
    }
    q = [(base, 'in')]

    a = []
    r = []

    def process_as_tuples(workflow_instructions, part_blob):
        result = []
        blob_data, workflow_key = part_blob
        if workflow_key in ['A', 'R']:
            return [part_blob]
        for instruction in workflow_instructions:
            if len(instruction) > 1 and instruction[1] in ['<', '>']:
                operator = instruction[1]
                operand = instruction.split(operator)[0]
                scalar, dest = instruction.split(operator)[1].split(':')
                
                scalar = int(scalar)

                lower, upper = blob_data[operand]

                if operator == '>': # EX: a > 123
                    valid = (scalar + 1, upper)
                    invalid = (lower, scalar)
                else: # EX: x < 456
                    valid = (lower, scalar - 1)
                    invalid = (scalar, upper)
                
                v_dict = copy.deepcopy(blob_data)

                v_dict[operand] = valid
                blob_data[operand] = invalid

                result.append((v_dict, dest))
            else:
                result.append((blob_data, instruction))
        return result


    while q:
        curr, next_workflow_key = q.pop(0)
        workflow_instructions = workflows.get(next_workflow_key, [next_workflow_key])
        next_blobs = process_as_tuples(workflow_instructions, (curr, next_workflow_key))
        for nb in next_blobs:
            data, dest = nb
            if dest == 'A':
                a.append(data)
            elif dest == 'R':
                r.append(data)
            else:
                q.append(nb)
    return a

def func():
    w = read_file()
    total = 0
    a = search(w)
    for i in a:
        x = 1
        for k, v in i.items():
            x *= (v[1] - v[0] + 1)
        total += x
    print('TOT', total)


func()

# 167245503449662 mine
# 167195399930385
# 167409079868000 theirs
# 167409079868000

# 256000000000000 
# 255668504097785
