def get_input(filename):
    with open(filename) as f:
        return int(f.read().strip())
    

def main():
    serial_number = get_input('input.txt')
    
    gridmap = {}
    # build
    for y_ix in range(300):
        for x_ix in range(300):
            x = x_ix + 1
            y = y_ix + 1
            assert x != 0 and y != 0
            rack_id = x + 10
            v = ((rack_id * y) + serial_number) * rack_id
            hundreds = int(str(v // 100)[-1])
            gridmap[(x, y)] = hundreds - 5
    # calc
    most_power = -1000000000
    cellx, celly = (1, 3)
    from_top_left_diff = [(1, 0), (2, 0), (0, -1), (0, -2), (1, -1), (1, -2), (2, -1), (2, -2)]
    for y_coord in range(300, 2, -1):
        for x_coord in range(1, 299):
            new_power = gridmap[(x_coord, y_coord)]
            for dx, dy in from_top_left_diff:
                new_power += gridmap[(x_coord + dx, y_coord + dy)]
            if new_power > most_power:
                most_power = new_power
                cellx = x_coord
                celly = y_coord
    print(gridmap[(cellx, celly)])
    for ddx, ddy in from_top_left_diff:
        print(gridmap[(cellx + ddx, celly + ddy)])
    # subtract b/c of the way we orient our grid
    return most_power, cellx, celly - 2 

print(main())