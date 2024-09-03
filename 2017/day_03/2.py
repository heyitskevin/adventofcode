def func():
    target = 265149
    lookup = {}
    x = 0
    y = 0
    val = 1
    steps = 1
    sd = ["r", "u", "l", "d"]
    curr_dir = 0
    lookup[(x,y)] = val

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    while val < target:
        for __ in range(2):
            for _ in range(steps):
                new_val = 0
                if sd[curr_dir] == "r":
                    x += 1
                elif sd[curr_dir] == "u":
                    y += 1
                elif sd[curr_dir] == "l":
                    x -= 1
                elif sd[curr_dir] == "d":
                    y -= 1
                else:
                    raise Exception("didn't hit an expected direction")
                for dx, dy in directions:
                    new_val += lookup.get((x+dx, y+dy), 0)
                
                lookup[(x,y)] = new_val
                val = new_val
            curr_dir = (curr_dir + 1) % 4
        steps += 1
    # Val isn't the answer b/c our solution goes side by side rather than item by item
    return(val, lookup)
            

print(func())