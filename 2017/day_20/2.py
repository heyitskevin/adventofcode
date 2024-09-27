import math
FILENAME = 'input.txt'

def readfile():
    res = []
    with open(FILENAME) as f:
        for ln in f.read().split('\n'):
            a = []
            for v in ln.split(', '):
                a.append(
                    [int(x) for x in v.split('=')[1][1:-1].split(',')]
                )
            res.append(a)
    return res


# For each particle
# Find all integer times GTE zero where it collides with other particle
# hash key integer time to value list of collisions
# For each key (integer time) for each value remove that value from every larger time
# Store annihilated particles by adding current key values to list
# Final output is total - annihilated
"""
p(t) = p + vt + at^2
positions equal at time T

"""    

    

def quad(vec1, vec2):
    a1, b1, c1 = vec1
    a2, b2, c2 = vec2

    a = (a1 - a2) / 2
    b = (b1 - b2) + ((a1 - a2) / 2)
    c = c1 - c2
    
    if a == 0:
        if b == 0:
            return -1, -1
        return (-c / b) , -1
    if (b * b) - (4 * a * c) < 0:
        return -1, -1
    determinant = math.sqrt((b ** 2) - (4 * a * c))

    r1 = (-b - determinant) / (2 * a)
    r2 = (-b + determinant) / (2 * a)

    return r1, r2

def collision_exists(particle1, particle2):
    p1, v1, a1 = particle1
    p2, v2, a2 = particle2
    
    valid_x = [x for x in quad(
        (a1[0], v1[0], p1[0]),
        (a2[0], v2[0], p2[0]),
    )]

    valid_y = [y for y in quad(
        (a1[1], v1[1], p1[1]),
        (a2[1], v2[1], p2[1]),
    )]

    valid_z = [z for z in quad(
        (a1[2], v1[2], p1[2]),
        (a2[2], v2[2], p2[2]),
    )]
    
    for xx in valid_x:
        if xx >= 0:
            if xx in valid_y and xx in valid_z:
                return True
    return False


def func():
    particles = readfile()
    non_collide = set([i for i in range(len(particles))])
    collide = set()

    for i, p1 in enumerate(particles):
        cded = []
        for j, p2 in enumerate(particles):
            if collision_exists(p1, p2):
                if i not in collide:
                    cded.append(i)
                    cded.append(j)
        collide.update(cded)
    return len(non_collide - collide)

print(func())