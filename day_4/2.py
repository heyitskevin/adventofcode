def read_card(card_line):
    card_id, card_data = card_line.strip().split(':')
    card_number = int(card_id.split(' ')[-1].strip())
    winners, candidates = card_data.strip().split('|')
    winners = [w for w in winners.strip().split(' ') if w]
    candidates = [c for c in candidates.strip().split(' ') if c]
    return card_number, winners, candidates

def get_winners(winners, candidates):
    num_winners = 0
    for c in candidates:
        if c in winners:
            num_winners += 1
    return num_winners

def eval_card_pile(pile): # Worst case factorial time but idgaf
    total = len(pile)
    bonus_rounds = {
        1: 0
    }
    for card in pile:
        card_number, winners, candidates = read_card(card)
        rounds = bonus_rounds.get(card_number, 0)
        for r in range(0, rounds+1):
            num_winners = get_winners(winners, candidates)
            total += num_winners
            next_card = card_number + 1
            for c in range(next_card, next_card+num_winners):
                if c > len(pile):
                    break
                if c not in bonus_rounds:
                    bonus_rounds[c] = 1
                else:
                    bonus_rounds[c] += 1
    return total

def make_pile():
    with open('input.txt') as f:
        arr = [ln for ln in f]
    return arr

def func():
    pile = make_pile()
    total = eval_card_pile(pile)
    print(total)

def faster_eval(pile):
    rounds = {}
    for card in pile:
        card_number, winners, candidates = read_card(card)
        num_winners = len([x for x in candidates if x in winners])
        if card_number in rounds:
            rounds[card_number] += 1
        else:
            rounds[card_number] = 1
        mult =rounds[card_number]
        next_card = card_number + 1
        for x in range(next_card, next_card + num_winners):
            if x in rounds:
                rounds[x] += mult
            else:
                rounds[x] = mult
    # print(rounds)
    return sum(rounds.values())

def the_cooler_func():
    pile = make_pile()
    total = faster_eval(pile)
    print(total)


import cProfile

cProfile.run('the_cooler_func()')
print('-----')
cProfile.run('func()')
