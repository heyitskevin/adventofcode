# A game is considered impossible if the number of seen cubes is greater than the amount that is in the bag
# We know the bag contains 12 red cubes, 13 green cubes, and 14 blue cubes
# It's important to note that the cubes are replaced into the bag after every round

RED_CUBES_IN_BAG = 12
GREEN_CUBES_IN_BAG = 13
BLUE_CUBES_IN_BAG = 14

"""
For each game string
    - split by ":" character
    - consequently the first element of the array contains the game ID and the second the actual game data
    - split the second element by the ";" character
    - For each element in the split string:
        - Consider the cubes revealed
        - If the number of cubes revealed is larger than previously seen, update what the max cubes is
        - If the number of cubes of a certain color seen all at once is GT the stated number of cubes in bag, this is an impossible scenario
    - If a game is impossible do not add it to the total, otherwise add
"""

def is_valid_round(balls):
    balls_by_color = balls.split(',')
    for b in balls_by_color:
        count, color = b.strip().split(' ')
        if color == 'green':
            if int(count) > GREEN_CUBES_IN_BAG:
                return False
        elif color == 'blue':
            if int(count) > BLUE_CUBES_IN_BAG:
                return False
        elif color == 'red':
            if int(count) > RED_CUBES_IN_BAG:
                return False
    return True

def game_impossible(ball_rounds):
    for round in ball_rounds.split(';'):
        if not is_valid_round(round):
            return True
    return False

def func():
    tot = 0
    with open('input.txt') as f:
        for ln in f:
            ln = ln.rstrip()
            game_string, ball_string = ln.split(':')
            game_id = game_string.split(' ')[1]
            if not game_impossible(ball_string):
                tot += int(game_id)
            else:
                print(game_id, ball_string)
    return tot

print(func())