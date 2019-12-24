#!/usr/bin/env python3

data = '''
....#
#..#.
#..##
..#..
#....
'''

data = '''
##.##
.#.##
##..#
#.#..
.###.
'''

moves = ((1, 0), (0, 1), (-1, 0), (0, -1))

bugs = tuple([tuple([x == '#' for x in line]) for line in data.strip().split('\n')])
seen = set()

def neighbors(x, y):
    c = 0
    for m in moves:
        x2 = x + m[0]
        y2 = y + m[1]
        if x2 >= 0 and x2 < 5 and y2 >= 0 and y2 < 5 and bugs[x2][y2]:
            c += 1
    return c

def move():
    result = []
    for x in range(5):
        line = []
        for y in range(5):
            n = neighbors(x, y)
            if bugs[x][y]:
                line.append(n == 1)
            else:
                line.append(n == 1 or n == 2)
        result.append(tuple(line))
    return tuple(result)

def print_bugs(n):
    print('\nAfter %d:' % n)
    for x in range(5):
        for y in range(5):
            print('#' if bugs[x][y] else '.', end = '')
        print()

def diversity():
    s = 0
    for x in range(5):
        for y in range(5):
            if bugs[x][y]:
                s += 2**(5 * x + y)
    return s

i = 0
while True:
    i += 1
    t = bugs
    if t in seen:
        print_bugs(i)
        print(diversity())
        exit(0)
    else:
        seen.add(t)
    bugs = move()
