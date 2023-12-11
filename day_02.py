"""
Advent Of Code 2023 --- Day 2: Cube Conundrum ---
"""

import aoc_lib as aoc

lines = aoc.lines_from_file('input_02.txt')

# parse the file
games = {}  # key = game ID, value list of (r,g,b) tuples
for line in lines:
    game, draws = line.split(': ')
    game_id = int(game[5:])
    game_draws = []
    for draw in draws.split('; '):
        reds   = 0
        greens = 0
        blues  = 0
        for number_color in draw.split(', '):
            number, color = number_color.split(' ')
            if color == 'red'  : reds   = int(number)
            if color == 'green': greens = int(number)
            if color == 'blue' : blues  = int(number)
        game_draws.append((reds, greens, blues))
    games[game_id] = game_draws
aoc.pprint(games)

# part 1
MAX_RED   = 12
MAX_GREEN = 13 
MAX_BLUE  = 14
sum_game_ids = 0
for game_id, game_draws in games.items():
    impossible = False
    for draw in game_draws:
        if draw[0] > MAX_RED  : impossible = True 
        if draw[1] > MAX_GREEN: impossible = True 
        if draw[2] > MAX_BLUE : impossible = True 
    if not impossible:
        sum_game_ids += game_id
print('Solution part 1: ', sum_game_ids)

# part 2
sum_powers = 0
for game_id, game_draws in games.items():
    max_reds   = 0
    max_greens = 0
    max_blues  = 0
    for draw in game_draws:
        if draw[0] > max_reds   : max_reds   = draw[0]
        if draw[1] > max_greens : max_greens = draw[1]
        if draw[2] > max_blues  : max_blues  = draw[2]
    power = max_reds * max_greens * max_blues
    sum_powers += power
print("Solution part 2: ", sum_powers)

