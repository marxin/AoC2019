#!/usr/bin/env python3

from math import floor

def fuel(weight):
    return floor(weight / 3) - 2

values = [int(l) for l in open('part1.txt').readlines()]

#for v in values:
#    print('%d:%d' % (v, fuel(v)))

print(sum([fuel(v) for v in values]))
