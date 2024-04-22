FILENAME = 'input.txt'

def read_file():
    r = []
    with open(FILENAME) as f:
        for ln in f.read().split('\n'):
            instruction, arguments = ln.split(' ', maxsplit=1)
            a = [x.strip() for x in arguments.split(',')]
            r.append(tuple([instruction, tuple(a)]))
    return r

class Computer:
    def __init__(self, instructions):
        self.reg_a = 0
        self.reg_b = 0
        self.instructions = instructions
        self.current_ix = 0

    def jump(self, args):
        offset = int(args[0][1:])
        if args[0] == '-':
            offset = offset * -1
        if offset + self.current_ix >= len(self.instructions):
            # Out of bounds
            return False
        else:
            next_instruction = self.instructions[self.current_ix + offset]
            self.current_ix = self.current_ix + offset
            return next_instruction

    def read_instruction(self, ins, args):
        if self.current_ix > len(self.instructions) - 1:
            return
        match ins:
            case 'hlf':
                if args[0] == 'a':
                    self.reg_a = self.reg_a / 2
                else:
                    self.reg_b = self.reg_b / 2
                self.current_ix += 1
                self.read_instruction(*self.instructions[self.current_ix])
            case 'tpl':
                if args[0] == 'a':
                    self.reg_a = self.reg_a * 3
                else:
                    self.reg_b = self.reg_b * 3
                self.current_ix += 1
                self.read_instruction(*self.instructions[self.current_ix])
            case 'inc':
                if args[0] == 'a':
                    self.reg_a += 1
                else:
                    self.reg_b += 1
                self.current_ix += 1
                self.read_instruction(*self.instructions[self.current_ix])
            case 'jmp':
                j = self.jump(args)
                if j:
                    self.read_instruction(*j)
            case 'jie':
                jx = False
                if args[0] == 'a':
                    if self.reg_a % 2 == 0:
                        jx = True
                else:
                    if self.reg_b % 2 == 0:
                        jx = True
                if jx:
                    jj = self.jump(args[1:])
                    if jj:
                        self.read_instruction(*jj)
                else:
                    self.current_ix += 1
                    self.read_instruction(*self.instructions[self.current_ix])
            case 'jio':
                jx = False
                if args[0] == 'a':
                    if self.reg_a % 2 == 1:
                        jx = True
                else:
                    if self.reg_b % 2 == 1:
                        jx = True
                if jx:
                    jj = self.jump(args[1:])
                    if jj:
                        self.read_instruction(*jj)
                else:
                    self.current_ix += 1
                    self.read_instruction(*self.instructions[self.current_ix])

def shortcut(a, b):
    print(a, b)
    if a == 1:
        return b
    b += 1
    if a % 2 == 0:
        a = a // 2
    else:
        a = a * 3
        a += 1

    shortcut(a, b)


def func():
    # with A starts at 0 we do all the first few instructions and then jump into the loop on line 42
    shortcut(9663, 0) # part 1
    # with A starts at 1 we start at line 20 and then the loop at 42
    shortcut(77671, 0)    


func()