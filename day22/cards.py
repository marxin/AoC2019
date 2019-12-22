#!/usr/bin/env python3

N = 10007
cards = list(range(N))

def stack(cards):
    return list(reversed(cards))

def cut(cards, n):
    return cards[n:] + cards[:n]

def modulate(cards, n):
    shuffle = [None] * len(cards)
    i = 0
    k = 0
    while True:
        if shuffle[i] != None:
            break
        shuffle[i] = k
        k += 1
        i += n
        if i >= len(cards):
            i -= len(cards)
    return [cards[i] for i in shuffle]

input = '''
deal with increment 15
cut -4394
deal with increment 9
deal into new stack
cut -8068
deal with increment 15
deal into new stack
cut 1470
deal into new stack
cut 4151
deal into new stack
cut -2438
deal into new stack
cut 9852
deal with increment 50
cut -953
deal with increment 8
cut -2836
deal with increment 30
cut -2419
deal into new stack
cut 2759
deal with increment 66
cut 1127
deal with increment 66
cut 2194
deal with increment 48
cut 4710
deal with increment 49
deal into new stack
deal with increment 59
deal into new stack
deal with increment 25
deal into new stack
deal with increment 60
cut -2003
deal with increment 2
cut -6166
deal with increment 26
cut -6179
deal with increment 4
cut 373
deal with increment 53
cut 6849
deal with increment 13
cut 625
deal with increment 68
cut 4084
deal with increment 53
cut -6939
deal into new stack
cut -3416
deal with increment 39
cut -2671
deal with increment 64
deal into new stack
deal with increment 75
cut 7654
deal into new stack
cut -5431
deal with increment 66
cut -370
deal into new stack
cut 3316
deal with increment 31
cut 312
deal with increment 22
cut 71
deal with increment 21
cut 562
deal with increment 27
cut 8611
deal with increment 67
cut 8358
deal with increment 7
cut -2957
deal with increment 71
cut 1740
deal with increment 31
cut -9577
deal with increment 59
cut 6104
deal with increment 40
cut -8862
deal with increment 17
cut 2516
deal with increment 34
cut 9594
deal into new stack
cut 5182
deal with increment 72
cut -2630
deal into new stack
cut -9018
deal with increment 45
cut -1069
deal with increment 28
cut 358
deal into new stack
cut -2244
'''

for operation in input.strip().split('\n'):
    parts = operation.split(' ')
    if parts[0] == 'cut':
        parts = operation.split(' ')
        n = int(parts[1])
        cards = cut(cards, n)
    elif parts[2] == 'increment':
        n = int(parts[3])
        cards = modulate(cards, n)
    elif parts[3] == 'stack':
        cards = stack(cards)
    else:
        assert False

print(cards.index(2019))
print(cards[2019])
