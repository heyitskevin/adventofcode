def readfile():
    with open('parsed_input.txt') as f:
        a, b = f.read().split('\n')
        return int(a.strip()), int(b.strip()) # Number of players, Number of marbles
    
# TIL ABOUT DOUBLE ENDED QUEUES
from collections import deque
def main():
    players, marbles = readfile()
    marbles *= 100
    marble_positions = deque([0])
    player_scores = {k:0 for k in range(players)}
    for marb in range(1, marbles + 1):
        if marb % 23 == 0:            
            marble_positions.rotate(7) # Rotating the DEQUE to the right is rotating the view of the marbles to the left, so invert -7
            player_scores[marb % players] += marb + marble_positions.pop()
            marble_positions.rotate(-1)
        else:
            marble_positions.rotate(-1)
            marble_positions.append(marb)

    
    return max(player_scores.values())

print(main())