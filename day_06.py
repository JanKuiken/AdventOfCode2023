"""
Advent Of Code 2023 --- Day 6: Wait For It ---
"""

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
game_time = 40857582
record_distance = 208141212571410

game_time = 71530
record_distance = 940200


# sailing_distance is een parabool met nul punten x=0 en 40857582
# hoe vaak zijn de interger punten boven 208141212571410
#
# In [9]: sqrt(208141212571410)
# Out[9]: 14427099.936279986
ongeveer_min = game_time // 2 - 14427099
ongeveer_max = game_time // 2 + 14427099

def win(time):
    return time * (game_time - time) - record_distance > 0

 
for i in range(-2, +2):
    x = ongeveer_min + i
    print(x, x * ( game_time -x) - record_distance)




