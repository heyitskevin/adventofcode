def readfile():
    a = 0
    b = 0
    c = 0
    inst = []
    with open('input.txt') as f:
        for ln in f.read().split('\n'):
            if "Register A" in ln:
                a = int(ln.split(':')[1].strip())
            if "Register B" in ln:
                b = int(ln.split(':')[1].strip())
            if "Register C" in ln:
                c = int(ln.split(':')[1].strip())
            if "Program" in ln:
                inst = [int(x) for x in ln.split(':')[1].strip().split(',')]

    return a, b, c, inst


def main():
    a, b, c, inst = readfile()
    ptr = 0
    # a, b, c = 729, 0, 0
    # inst = [0, 1, 5,4, 3, 0]
    def combo(operand):
        if 0 <= operand <= 3:
            return operand
        if operand == 4:
            return a
        if operand == 5 :
            return b
        if operand == 6:
            return c
        if operand == 7:
            return None
    
    output = []
    while ptr < len(inst) - 1:
        opcode = inst[ptr]
        operand = inst[ptr + 1]
        if opcode == 0:
            operand = combo(operand)
            div = int(a / (2 ** operand))
            a = div
        elif opcode == 1:
            b = b ^ operand
            
        elif opcode == 2:
            b = combo(operand) % 8
        elif opcode == 3:
            if a != 0:
                ptr = operand
                continue
        elif opcode == 4:
            b = b ^ c
            
        elif opcode ==  5:
            output.append(str(combo(operand) % 8))
        elif opcode == 6:
            operand = combo(operand)
            div = int(a / (2 ** operand))
            b = div
        elif opcode == 7:
            operand = combo(operand)
            div = int(a / (2 ** operand))
            c = div
        ptr += 2
    return ','.join(output)

print(main())