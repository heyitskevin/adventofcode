def parse_card(line):
    card_data = line.split(':')[1].strip()
    winning_numbers, numbers_you_have = card_data.split('|')
    wn = [int(e) for e in winning_numbers.strip().split(' ') if e]
    nyh = [int(i) for i in numbers_you_have.strip().split(' ') if i]
    return wn, nyh

def func():
    tot = 0
    with open('input.txt') as f:
        for ln in f:
            points = 0
            winners, candidates = parse_card(ln)
            for c in candidates:
                if c in winners:
                    if points == 0:
                        points = 1
                    else:
                        points = points * 2
            tot += points
    print(tot)

                
func()