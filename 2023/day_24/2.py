FILENAME = 'input.txt'
LOWERBOUND = 200000000000000
UPPERBOUND = 400000000000000
# LOWERBOUND = 7
# UPPERBOUND = 27

import itertools

# Matrix Helpers
def matrix_transpose(m):
    return list(map(list, zip(*m)))

def matrix_minor(m, i, j):
    return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

def matrix_det(m):
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c) * m[0][c] * matrix_det(matrix_minor(m, 0, c))

    return determinant

def matrix_inverse(m):
    determinant = matrix_det(m)
    cofactors = []

    for r in range(len(m)):
        row = []

        for c in range(len(m)):
            minor = matrix_minor(m, r, c)
            row.append(((-1)**(r + c)) * matrix_det(minor))

        cofactors.append(row)

    cofactors = matrix_transpose(cofactors)

    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] /= determinant

    return cofactors

def matrix_mul(m, vec):
    res = []

    for row in m:
        res.append(sum(r * v for r, v in zip(row, vec)))

    return res

def get_equation_matricies(pos1, vel1, pos2, vel2):
    diff_pos_x = pos1[0] - pos2[0]
    diff_pos_y = pos1[1] - pos2[1]
    diff_pos_z = pos1[2] - pos2[2]
    
    diff_vel_x = vel1[0] - vel2[0]
    diff_vel_y = vel1[1] - vel2[1]
    diff_vel_z = vel1[2] - vel2[2]
    # Preprocessing determinants
    A = [ 
        [0, -diff_vel_z, diff_vel_y, 0 , -diff_pos_z, diff_pos_y],
        [diff_vel_z, 0, -diff_vel_x, diff_pos_z, 0, -diff_pos_x],
        [-diff_vel_y, diff_vel_x, 0, -diff_pos_y, diff_pos_x, 0]
    ]

    B = [
        pos2[1]*vel2[2] - pos2[2]*vel2[1] - (pos1[1]*vel1[2] - pos1[2]*vel1[1]),
        pos2[2]*vel2[0] - pos2[0]*vel2[2] - (pos1[2]*vel1[0] - pos1[0]*vel1[2]),
        pos2[0]*vel2[1] - pos2[1]*vel2[0] - (pos1[0]*vel1[1] - pos1[1]*vel1[0])
    ]

    return A, B

def read_file():
    with open(FILENAME) as f:
        return [[[int(b) for b in a.strip().split(',')] for a in tuple(ln.split('@'))] for ln in f.read().split('\n')]

# Three Hailstione collisions makes a line, so just take the first three and solve
def solution(data):
    (h1, vh1), (h2, vh2), (h3, vh3) = data[:3]
    print(h1, vh1, h2, vh2, h3, vh3)
    a12, b12 = get_equation_matricies(h1, vh1, h2, vh2)
    a13, b13 = get_equation_matricies(h1, vh1, h3, vh3)

    a123 = a12 + a13
    b123 = b12 + b13

    soln = matrix_mul(matrix_inverse(a123), b123)
    # We want integer values
    print(soln)
    print(sum(
        map(round, soln[:3])
    ))
    


def func():
    data = read_file()
    
    solution(data)

# func()

# 888708704663411 too low


data = [[int(i) for i in l.replace('@',',').split(',')]
                for l in open('input.txt')]


def solve(a, b):
    m = [a+[b] for a,b in zip(a, b)]
    m = [[a-b  for a,b in zip(a, m[4])] for a in m[:4]]

    for i in range(len(m)):
        m[i] = [m[i][k]/m[i][i] for k in range(len(m[i]))]

        for j in range(i+1, len(m)):
            m[j] = [m[j][k]-m[i][k]*m[j][i] for k in range(len(m[i]))]

    for i in reversed(range(len(m))):
        for j in range(i):
            m[j] = [m[j][k]-m[i][k]*m[j][i] for k in range(len(m[i]))]

    return [r[-1] for r in m]


def cols(a, b, c, d):
    A = [[r[c], -r[d], r[a], r[b]] for r in data]
    B = [r[b] * r[c] - r[a] * r[d] for r in data]
    return A, B

x, y, *_ = solve(*cols(0, 1, 3, 4))
z,    *_ = solve(*cols(1, 2, 4, 5))

print(x+y+z)