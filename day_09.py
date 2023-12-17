"""
Advent Of Code 2023 --- Day 9: Mirage Maintenance ---
"""

import aoc_lib as aoc

# parse the input
#lines = aoc.lines_from_file('example_input_09.txt')
lines = aoc.lines_from_file('input_09.txt')

# Part 1

solution_1 = 0
solution_2 = 0

for line in lines:
    rows = []
    numbers = [int(s) for s in line.split(' ')]
    rows.append(numbers)
    while True:
        numbers = [b - a for a,b in zip(numbers[:-1], numbers[1:])]
        rows.append(numbers)
        if all([n == 0 for n in numbers]):
            break
    print(rows)
    rows.reverse()
    
    post_fix_number = 0
    pre_fix_number = 0

    for row in rows[1:]:
        last = row[-1]
        first = row[0]
        post_fix_number = post_fix_number + last
        pre_fix_number = first - pre_fix_number
        print(pre_fix_number, post_fix_number)
    solution_1 += post_fix_number
    solution_2 += pre_fix_number
    
print('Solution part 1:', solution_1)

# Part 2
print('Solution part 2:', solution_2)

