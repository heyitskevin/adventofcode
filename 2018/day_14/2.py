"""
Make the next two ints and append to end
if the next two ints progresses the cursor, advance the cursor
Else reset the cursor
if the cursor hits the end, return the length of the string?
"""

def main():
    with open('input.txt') as f:
        target = f.read().strip()
    cursor = 0
    
    rec_str = '37'
    elf1 = 0
    elf2  = 1

    while True:
        if cursor == len(target):
            return rec_str.find(target)
        next_vals = str(int(rec_str[elf1]) + int(rec_str[elf2]))
        rec_str += next_vals
        if cursor == 0:
            for i in range(len(next_vals)):
                if target[i] == next_vals[i]:
                    cursor += 1
                else:
                    cursor = 0
        elif cursor < len(target):
            for v in next_vals:
                if cursor == len(target):
                    return rec_str.find(target)
                if v == target[cursor]:
                    cursor += 1
                else:
                    cursor = 0
        
        e1_steps = int(rec_str[elf1]) + 1
        e2_steps = int(rec_str[elf2]) + 1

        elf1 = (e1_steps + elf1) % len(rec_str)
        elf2 = (e2_steps + elf2) % len(rec_str)

        
print(main())