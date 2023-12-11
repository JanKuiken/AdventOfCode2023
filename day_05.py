"""
Advent Of Code 2023 --- Day 5: If You Give A Seed A Fertilizer ---
"""

import aoc_lib as aoc

# parse the input
lines = aoc.lines_from_file('input_05.txt')

seed_str = lines[0]
_, seed_str = seed_str.split(':')
seeds = aoc.numbers_from_str(seed_str)

map_strs = aoc.split_on_empty_string(lines[2:])
maps = {}
for m in map_strs:
    key = m[0].replace(':', '')
    values = [aoc.numbers_from_str(s) for s in m[1:]]
    maps[key] = values

aoc.pprint(seeds)
aoc.pprint(maps)


# Part 1
def mapper(map_name, source):
    for m in maps[map_name]:
        destination_start = m[0] 
        source_start      = m[1]
        length            = m[2]
        #print(destination_start, source_start, length, ' - ', source)
        if source >= source_start and source < source_start + length:
            return source - source_start + destination_start
    return source


def apply_all_maps(source):
    map_names_in_order = [    
        'seed-to-soil map', 
        'soil-to-fertilizer map', 
        'fertilizer-to-water map', 
        'water-to-light map', 
        'light-to-temperature map', 
        'temperature-to-humidity map', 
        'humidity-to-location map'
    ]
    for map_name in map_names_in_order:
        source = mapper(map_name, source)
    return source

locations = []
for source in seeds:
    locations.append(apply_all_maps(source))

print('Solution part 1: ', min(locations))


# Part 2
# we moeten een soort super-mapper maken.... met ranges naar ranges


