FILENAME = 'input.txt'

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

        return workflowify(workflows.split('\n')), partsify(parts.split('\n'))
    
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

def evaluate_instructions(instructions, part):
    for inst in instructions:
        if len(inst) > 1 and inst[1] in ['>', '<']:
            # comparator
            part_operand, operator= inst[0], inst[1]
            
            if operator == '>':
                value, result = inst.split('>')[1].split(':')
                value = int(value)
                if part.get_part_val_by_operand(part_operand) > value:
                    return result
                else:
                    continue
            elif operator == '<':
                value, result = inst.split('<')[1].split(':')
                value = int(value)
                if part.get_part_val_by_operand(part_operand) < value:
                    return result
                else: 
                    continue
        else:
            # default situation
            return inst

def process_parts(parts, workflows):
    accepted = []
    rejected = []
    for p in parts:
        result = -1
        in_instruction = workflows['in']
        
        while result not in ['A', 'R']:
            result = evaluate_instructions(in_instruction, p)
            
            if result == 'A':
                accepted.append(p)
                break
            elif result == 'R':
                rejected.append(p)
                break
            else:
                in_instruction = workflows[result]
    return accepted, rejected


def func():
    w, p = read_file()
    a, r = process_parts(p, w)
    # print('ACCEPTED', a)
    # print('REJECTED', r)
    total = 0
    for pp in a:
        total += (pp.x + pp.m + pp.a + pp.s)
    print('TOT', total)
    

func()