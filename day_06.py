"""
Advent Of Code 2023 --- Day 6: Wait For It ---
"""

import aoc_lib as aoc
from math import ceil, floor

# copied instead of reading input file
times     = [  46,   85,   75,   82 ]
distances = [ 208, 1412, 1257, 1410 ]

# Part 1
n_possibilties = []
for total_time, record_distance in zip(times, distances):
    wins = 0
    for charge_time in range(0, total_time+1):
        sailing_time = total_time - charge_time
        speed = charge_time
        sailed_distance = sailing_time * speed
        if sailed_distance > record_distance:
            wins += 1
    n_possibilties.append(wins)

total_n_possibilties = 1
for n in n_possibilties:
    total_n_possibilties *= n

print('Solution part 1:', total_n_possibilties)

# part 2
# oke,... 
game_time = 46857582
record_distance = 208141212571410

# from the example input
# game_time = 71530
# record_distance = 940200

# sailing_distance is een parabool met nul punten x=0 en `game_time`
# hoe vaak zijn de interger punten boven `record_distance`

def sailing_distance_minus_record(time):
    return float(float(time) * float(game_time - time) - float(record_distance))


low  = ceil (aoc.simple_newton_zero_finding(sailing_distance_minus_record, game_time * 0.25, epsilon=.1, dx=.1))
high = floor(aoc.simple_newton_zero_finding(sailing_distance_minus_record, game_time * 0.75, epsilon=.1, dx=.1))
# hmm needed some tuning of epsilon and dx... (dunno why)

print('Solution part 2:', 1 + high - low)






