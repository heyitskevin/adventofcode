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
    
    output = []

    count = 8 ** 15
    # Solved by examination. 
    # Start with base expectation that since a must divide 8 at least 15 times to get a 16 digit instruction a is at least 8 ^ 15.
    # Then, taking small slices of the output, compare to input and take steps of large size over the search space
    # As output slices become more and more close to input, reduce step size
    # There's a programmatic way to describe this but I just did it by hand
    while output != inst:
        output = []
        a = count
        b = 0
        c = 0
        while a > 0:
            b = a % 8
            b = b ^ 2
            c = int(a / (2 ** b))
            b = b ^ c
            a = int(a / 8)
            b = b ^ 7
            output.append(b % 8)
        assert len(output) == len(inst)
        if output[-1:] == inst[-1:]: # Increase slice size here
            print(count, output)
        else:
            count += 100000000 # decrease step size here
        count += 1
    return count - 1

print(main())
