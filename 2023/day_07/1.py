card_priority = [
    'A','K','Q','J','T','9','8','7','6','5','4','3','2',
]

from collections import Counter

FILENAME = 'input.txt'

def read_card_data():
    cards = []
    with open(FILENAME) as f:
        for ln in f:
            hand, bid = ln.split(' ')
            cards.append((hand.strip(), int(bid.strip())))
    return cards


def left_is_greater_than_right(left, right):
    count_left = Counter(left[0])
    count_right = Counter(right[0])
    if len(count_left) > len(count_right):
        return False
    if len(count_left) < len(count_right):
        return True
    if sorted(list(count_left.values())) == sorted(list(count_right.values())):
        # Hands have the same shape
        for ix in range(len(left[0])):
            e_left = left[0][ix]
            e_right = right[0][ix]
            if card_priority.index(e_left) ==  card_priority.index(e_right):
                # index should always return
                continue
            else:
                return card_priority.index(e_left) < card_priority.index(e_right)
            
    else:
        common_left = count_left.most_common()
        common_right = count_right.most_common()
        while common_left and common_right:
            ll = common_left.pop(0)[1]
            rr = common_right.pop(0)[1]
            if ll > rr:
                return True
            if rr > ll:
                return False

def mergeSort(deck):
    if len(deck) > 1:
        mid = len(deck) // 2
        left = deck[:mid]
        right = deck[mid:]
        
        mergeSort(left)
        mergeSort(right)

        # Counters
        c_left = 0
        c_right = 0
        c_all = 0
        while c_left < len(left) and c_right < len(right):
            if not left_is_greater_than_right(left[c_left], right[c_right]):
                deck[c_all] = left[c_left]
                c_left += 1
            else:
                deck[c_all] = right[c_right]
                c_right += 1
            c_all += 1
        while c_left < len(left):
            deck[c_all] = left[c_left]
            c_left += 1
            c_all += 1
        while c_right < len(right):
            deck[c_all] = right[c_right]
            c_right += 1
            c_all += 1
    return deck
        

def func():
    deck = read_card_data()
    ordered = mergeSort(deck)
    # print(ordered)
    tot = 0
    for ix, val in enumerate(ordered):
        tot += (ix+1) * val[1]
    print(tot)

func()