"""
Advent Of Code 2023 --- Day 8: Haunted Wasteland ---
"""

import aoc_lib as aoc

# parse the input
lines = aoc.lines_from_file('input_08.txt')
Node = aoc.namedtuple("Node", "left right")

left_rights = lines[0]

location_map = {}
for line in lines[2:]:
    # lets use indexes... 
    location_map[line[0:3]] = Node(line[7:10], line[12:15])

# Part 1

def next_position(position, direction):
    if direction == 'L':
        return location_map[position].left
    else:
        return location_map[position].right
    
current_position = 'AAA'
steps = 0
while current_position != 'ZZZ':
    for direction in left_rights:
        current_position = next_position(current_position, direction)
        steps += 1

print("Solution part 1:", steps)

# Part 2

if False: # this simple method below took too long.... 

    current_positions = []
    for pos in location_map.keys():
        if pos.endswith('A'):
            current_positions.append(pos)

    def are_end_positions():
        for pos in current_positions:
            if not pos.endswith('Z'):
                return False
        return True

    steps = 0
    while True:
        for direction in left_rights:
            current_positions = [next_position(pos, direction) for pos in current_positions]
            steps += 1
            print(steps, current_positions)
            if are_end_positions():
                break

# a more clever solution....

start_positions = []
for pos in location_map.keys():
    if pos.endswith('A'):
        start_positions.append(pos)

print('Start positions:', start_positions, 'len:', len(start_positions))

first_end_points  = []
second_end_points = []

for pos in start_positions:
    print('Start pos', pos)
    steps = 0
    cont = True
    first_end_point = None
    seconds_end_point = None
    while cont:
        for direction in left_rights:
            pos = next_position(pos, direction)
            steps += 1
            if pos.endswith('Z'):
                if not first_end_point:
                    print(pos, steps)
                    first_end_point = steps
                else:
                    print(pos, steps)
                    second_end_point = steps
                    cont = False
                    break
    first_end_points.append(first_end_point)
    second_end_points.append(second_end_point)

# ok each start pos reaches an end point and than revisits the same end
# after some steps reaches the same end point

delta_end_points = [(end - start) for end, start in zip(second_end_points, first_end_points)]

print('First  : ', first_end_points)
print('Second : ', second_end_points)
print('Delta  : ', delta_end_points)

# hmm, delta and first are equal, this must be a coincidence
print('First == Delta :', first_end_points == delta_end_points)

# are these prime numbers...?
def is_prime(n):
    for i in range(2, n-2):
        if n % i == 0:
            return False
    return True

for i in delta_end_points:
    print(is_prime(i))

# no, lets pull in some Python power (least common multiple)
from math import lcm
print("Solution part 2:", lcm(*delta_end_points))

