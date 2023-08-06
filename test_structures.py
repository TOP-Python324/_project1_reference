from itertools import chain


# '   |   | O \n———————————\n   | X |   \n———————————\n   |   | X '

field3 = ' {} | {} | {} \n———————————\n {} | {} | {} \n———————————\n {} | {} | {} '

field4 = (' {} | {} | {} | {} \n'
          '———————————————\n'
          ' {} | {} | {} | {} \n'
          '———————————————\n'
          ' {} | {} | {} | {} \n'
          '———————————————\n'
          ' {} | {} | {} | {} ')


# board = field3.format(' ', ' ', 'O', ' ', 'X', ' ', ' ', ' ', 'X')

# 1.
turns = '  O X   X'
board = field3.format(*turns)

# 2.
turns = [' ', ' ', 'O', ' ', 'X', ' ', ' ', ' ', 'X']
board = field3.format(*turns)

# 3.
empty = dict.fromkeys(range(1, 10), ' ')
turns = {5: 'X', 3: 'O', 9: 'X'}
board = field3.format(*(empty | turns).values())

# 4.
turns = [ [' ', ' ', 'O'],
          [' ', 'X', ' '],
          [' ', ' ', 'X'] ]
board = field3.format(*chain(*turns))



wins3 = [
    'OOO      ',
    '   OOO   ',
    '      OOO',
    'O  O  O  ',
    ' O  O  O ',
    '  O  O  O',
    'O   O   O',
    '  O O O  ',
    'XXX      ',
    '   XXX   ',
    '      XXX',
    'X  X  X  ',
    ' X  X  X ',
    '  X  X  X',
    'X   X   X',
    '  X X X  ',
]

# 1.
turns = '  O X   X'

# 2.
turns = [' ', ' ', 'O', ' ', 'X', ' ', ' ', ' ', 'X']
turns = ''.join(comb)

# 4.
turns = [ [' ', ' ', 'O'],
          [' ', 'X', ' '],
          [' ', ' ', 'X'] ]
turns = ''.join(chain(*turns))

for comb in wins:
    comb == turns



wins3 = [
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9},
    {1, 4, 7},
    {2, 5, 8},
    {3, 6, 9},
    {1, 5, 9},
    {3, 5, 7}
]

# 5.
turns = [5, 3, 9]
crosses = set(turns[::2])
zeros = set(turns[1::2])

# 3.
turns = {5: 'X', 3: 'O', 9: 'X'}
crosses = set(islice(turns, 0, None, 2))
zeros = set(islice(turns, 1, None, 2))

for comb in wins:
    comb <= crosses

for comb in wins:
    comb <= zeros
