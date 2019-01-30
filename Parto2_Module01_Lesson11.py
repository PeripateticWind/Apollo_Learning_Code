import sys

p = [0, 1, 0, 0, 0]
n = 5
# for i in range(n):
#     p.append(1. / n)

world = ['green', 'red', 'red', 'green', 'green']
Z = 'green'
measurements = ['green', 'red']
motions = [1, 1]

pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOverShoot = 0.1
pUnderShoot = 0.1


def sense(p, Z):
    q = []
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))
    s = sum(q)
    for i in range(len(p)):
        q[i] = q[i] / s
    return q


def move(p, U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i - U) % len(p)]
        s += pOverShoot * p[(i - U - 1) % len(p)]
        s += pUnderShoot * p[(i - U + 1) % len(p)]
        q.append(s)
    return q


# for k in range(len(measurements)):
#     p = sense(p, measurements[k])
# print(p)
for i in range(1000):
    p = move(p, 1)

for k in range(len(measurements)):
    p = sense(p, measurements[k])
    p = move(p, motions[k])

print(p)
