
import sys
sys.path.append("..") 
import aoc_lib as aoc

lines = aoc.lines_from_file('input.txt')

from string import digits

# part 1
total = 0
for line in lines:
    ds = [c for c in line if c in digits]
    number_str = ds[0] + ds[-1]
    total += int(number_str)
print('Solution part 1: ', total)

# part 2
d_strs = ['one','two','three','four','five','six','seven','eight','nine']
d_vals = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
total = 0
for line in lines:
    ds = []
    for start in range(len(line)):
        if line[start] in digits:
            ds.append(line[start])
        rest = line[start:]
        for d_str, d_val in zip(d_strs, d_vals):
            if rest.startswith(d_str):
                ds.append(d_val)
    number_str = ds[0] + ds[-1]
    total += int(number_str)
print('Solution part 2: ', total)

