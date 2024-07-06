a = 1
b = 1
c = 7
d = 26
for _ in range(c):
    d += 1
c = a
a += 1
b -= 1
b = c
d -= 1

for i in range(d):
    c = a
    a += 1
    b -= 1
    if b > 0:
        for j in range(b):
            a += 1
    b = c

d = 14
c = 14

for __ in range(c):
    for _ in range(d):
        a += 1


print(a)