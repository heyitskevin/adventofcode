card_priority = [
    'A','K','Q','T','9','8','7','6','5','4','3','2','J'
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

def j_transform(input_string):
    if input_string == 'JJJJJ':
        return 'AAAAA' # Hard code edge case I guess
    # The optimized J-Transform is one which the largest count gets incremented again
    test_string = input_string.replace('J', '')
    c = Counter(test_string).most_common()
    best_val = c[0]
    if best_val[1] < 3:
        # dupe_count possible
        dupe_count = []
        for tup in c[1:]:
            if tup[1] == best_val[1]:
                dupe_count.append(tup)
        for elem in dupe_count:
            chara = elem[0]
            if card_priority.index(chara) < card_priority.index(best_val[0]):
                best_val = elem
    print('best_val', best_val, input_string)
    j_string = input_string.replace('J', best_val[0])
    return j_string

def left_is_greater_than_right(left, right):
    j_left = j_transform(left[0]) if 'J' in left[0] else left[0]
    jl_count = Counter(j_left)

    j_right = j_transform(right[0]) if 'J' in right[0] else right[0]
    jr_count = Counter(j_right)

    if len(jl_count) > len(jr_count):
        return False
    if len(jl_count) < len(jr_count):
        return True
    if sorted(list(jl_count.values())) == sorted(list(jr_count.values())):
        # Hands have the same shape
        for ix in range(len(left[0])):
            e_left = left[0][ix]
            e_right = right[0][ix]
            if card_priority.index(e_left) ==  card_priority.index(e_right):
                # index should always return
                continue
            else:
                return card_priority.index(e_left) < card_priority.index(e_right)
            
    else: # Differing shapes of the same length
        common_left = jl_count.most_common()
        common_right = jr_count.most_common()
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

        # Index trackers
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
    print(ordered)
    tot = 0
    for ix, val in enumerate(ordered):
        tot += (ix+1) * val[1]
    print(tot)

func()


