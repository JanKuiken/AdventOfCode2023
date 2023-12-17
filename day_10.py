"""
Advent Of Code 2023 --- Day 10: Pipe Maze ---
"""

import aoc_lib as aoc

# parse the input
matrix = aoc.matrix_from_file('input_10.txt')

# make it a bit more beautiful to print (and do some admin)
n_rows = len(matrix)
n_cols = len(matrix[0])
for row in range(n_rows):
    for col in range(n_cols):
        c = matrix[row][col]
        c = c.translate(str.maketrans('F7LJ-|', '╭╮╰╯─│'))
        matrix[row][col] = c
        if c == 'S':
            start_row = row
            start_col = col

aoc.print_matrix(matrix)

print('Size :', n_rows, n_cols)
print('Start :', start_row, start_col)

new_direction_map = {
    ('→', '╯') : '↑', 
    ('→', '─') : '→', 
    ('→', '╮') : '↓', 
    ('←', '╰') : '↑', 
    ('←', '─') : '←', 
    ('←', '╭') : '↓', 
    ('↑', '╮') : '←', 
    ('↑', '│') : '↑', 
    ('↑', '╭') : '→', 
    ('↓', '╯') : '←', 
    ('↓', '│') : '↓', 
    ('↓', '╰') : '→', 
}


# visually checked that we go east to start
row = start_row
col = start_col
direction = '→'
pipe = []
while True:
    pipe.append((row, col))
    if   direction == '→' : col += 1
    elif direction == '←' : col -= 1
    elif direction == '↑' : row -= 1
    elif direction == '↓' : row += 1
    else: raise ValueError('wrong direction')
    symbol = matrix[row][col]
    if symbol == 'S':
        break
    direction = new_direction_map[(direction, symbol)]

print('Solution part 1:', len(pipe)//2)

# Part 2

pipe = set(pipe)                   # makes it a bit faster
matrix[start_row][start_col] = '─' # makes it consistent
inside = 0

for row in range(n_rows):
    outside = True
    border = ''
    for col in range(n_cols):
        current_at_pipe = (row,col) in pipe
        if current_at_pipe:
            if matrix[row][col] != '─':
                border += matrix[row][col]
                if border == '│' or border == '╭╯' or border == '╰╮':
                    outside = not outside
                    border = ''                 
                if border == '╰╯' or border == '╭╮':
                    border = ''                 
        else:
            if outside:
                matrix[row][col] = ' '
            else:
                matrix[row][col] = '╳'
                inside += 1

aoc.print_matrix(matrix)
print('Solution part 2:', inside)

