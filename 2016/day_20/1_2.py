MIN_INT = 0
MAX_INT = 4294967295

FILENAME = "input.txt"

def read_file():
    with open(FILENAME) as f:
        return [
            tuple(int(v) for v in ln.strip().split('-')) for ln in f.read().split('\n')
        ]
    
def get_allows(ip_list):
    allows = []
    ip = MIN_INT
    while ip <= MAX_INT:
        while ip <= MAX_INT:
            found_next_value = False
            for low, high in ip_list:
                if low <= ip and ip <= high:
                    ip = high + 1
                    found_next_value = True
                    break
            if not found_next_value:
                allows.append(ip)
                ip += 1
                break
    return allows
        

def func():
    data = read_file()
    a = get_allows(data)
    print(len(a), min(a))

func()