"""
The fewest number of cubes of each color is just the max seen cubes per color
"""
def get_balls_in_round(rnd):
    balls_by_color = rnd.split(',')
    red = 0
    blue = 0
    green = 0
    for b in balls_by_color:
        count, color = b.strip().split(' ')
        count = int(count)
        if color == 'green':
            green = count
        elif color == 'blue':
            blue = count
        elif color == 'red':
            red = count
    return red, blue, green



def get_maxes(rounds):
    reds = []
    blues = []
    greens = []
    for rnd in rounds.split(';'):
        r, b, g = get_balls_in_round(rnd)
        reds.append(r)
        blues.append(b)
        greens.append(g)
    return max(reds), max(blues), max(greens)


def func():
    tot = 0
    with open('input.txt') as f:
        for ln in f:
            ln = ln.rstrip()
            game_string, ball_string = ln.split(':')
            game_id = game_string.split(' ')[1]
            p = get_maxes(ball_string)
            prod = 1
            for elem in p:
                prod *= int(elem)
            tot += prod
    return tot

print(func())