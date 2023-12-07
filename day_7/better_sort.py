# ONLY FOR PART 2

card_priority = [
    'A','K','Q','T','9','8','7','6','5','4','3','2','J'
]

cards_by_low_to_high= "J23456789TQKA"

from collections import Counter

FILENAME = 'input.txt'

def read_card_data():
    cards = []
    with open(FILENAME) as f:
        for ln in f:
            hand, bid = ln.split(' ')
            cards.append((hand.strip(), int(bid.strip())))
    return cards

def get_hand_strength(hand):
    c = Counter(hand)
    jokers = c.pop('J', 0)
    hand_counts = [0] if jokers == 5 else sorted(c.values())
    hand_counts[-1] += jokers
    match hand_counts:
        case *_, 5:
            return 7
        case *_, 4:
            return 6
        case *_, 2, 3:
            return 5
        case *_, 3:
            return 4
        case *_, 2, 2:
            return 3
        case *_, 2:
            return 2
    return 1

def func():
    cards = read_card_data()
    strength = [(*c, get_hand_strength(c[0])) for c in cards]
    strength = sorted(
        strength, # Sort in ascending order from lowest hand strength, then by card priority on low-to-high string
        key=lambda x: (x[2], *map(cards_by_low_to_high.index, x[0]))
    )

    print(
        sum(
            ix * hand[1] for ix, hand in enumerate(strength, start=1)
        )
    )

func()