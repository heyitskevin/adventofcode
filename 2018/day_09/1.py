def readfile():
    with open('parsed_input.txt') as f:
        a, b = f.read().split('\n')
        return int(a.strip()), int(b.strip()) # Number of players, Number of marbles
    

def main():
    players, marbles = readfile()
    
    marble_positions = [0]
    curr_marble_ix = 0
    nxt_marble = 1
    player_scores = [0 for _ in range(players)]
    # LTE because of the way the prompt is phrased
    while nxt_marble <= marbles:
        curr_player = nxt_marble % players
        if nxt_marble != 0 and nxt_marble % 23 == 0:
            player_scores[curr_player] += nxt_marble
            rm_marble = marble_positions.pop(curr_marble_ix-7)

            player_scores[curr_player] += rm_marble
            curr_marble_ix -= 7
            curr_marble_ix = curr_marble_ix % len(marble_positions)
        else:
            curr_marble_ix += 2
            if curr_marble_ix == len(marble_positions):
                marble_positions.append(nxt_marble)
            elif curr_marble_ix > len(marble_positions):
                curr_marble_ix = curr_marble_ix % len(marble_positions)
                marble_positions = marble_positions[:curr_marble_ix] + [nxt_marble] + marble_positions[curr_marble_ix:]
            else:
                marble_positions = marble_positions[:curr_marble_ix] + [nxt_marble] + marble_positions[curr_marble_ix:]
        nxt_marble += 1
    
    return max(player_scores)

print(main())