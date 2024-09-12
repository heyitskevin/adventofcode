FILENAME = 'input.txt'

def read_file():
    with open(FILENAME) as f:
        return [int(x) for x in f.read().strip().split(',')]
    
def func():
    numbers = [i for i in range(256)]
    current_pos = 0
    skip = 0
    lengths = read_file()
    
    for l in lengths:
        if l > len(numbers):
            continue
        end = current_pos + l
        if end > len(numbers):
            sub = numbers[current_pos:] + numbers[:end - len(numbers)]
            sub = sub[::-1]
            
            numbers = numbers[:current_pos] + sub
            trunc = numbers[256:]
            numbers = trunc + numbers[len(trunc):256]
        else:
            sub = numbers[current_pos:end][::-1]
            numbers = numbers[:current_pos] + sub + numbers[end:]
        
        current_pos = (end + skip) % len(numbers)
        skip += 1
    print(len(numbers))
    return numbers[0] * numbers[1]

print(func())