"""
Advent Of Code 2023 --- Day 7: Camel Cards ---
"""

import aoc_lib as aoc
from collections import Counter

# parse the input
# lines = aoc.lines_from_file('example_input_07.txt')
lines = aoc.lines_from_file('input_07.txt')

# we gaan h.e.e.a. maar in een list of dicts bewaren
hands = []
for line in lines:
    hand, bid = line.split()
    hands.append({'hand' : hand, 'bid' : int(bid)})

# map of types to ordered numbers
MAP_TYPE = {
    (5,)         : 7,  #  FIVE_OF_A_KIND,
    (4,1,)       : 6,  #  FOUR_OF_A_KIND,
    (3,2,)       : 5,  #  FULL_HOUSE,
    (3,1,1,)     : 4,  #  THREE_OF_A_KIND,
    (2,2,1,)     : 3,  #  TWO_PAIR,
    (2,1,1,1,)   : 2,  #  ONE_PAIR,
    (1,1,1,1,1,) : 1,  #  HIGH_CARD, 
}

# map of card to ordered numbers
MAP_CARD = {
    'A' : 14, 
    'K' : 13, 
    'Q' : 12, 
    'J' : 11, 
    'T' : 10, 
    '9' : 9, 
    '8' : 8, 
    '7' : 7, 
    '6' : 6,
    '5' : 5, 
    '4' : 4, 
    '3' : 3, 
    '2' : 2,
}

# Part 1

def determine_type(hand):
    c = Counter(hand)
    most_common_numbers = [mc[1] for mc in c.most_common()]
    return MAP_TYPE[tuple(most_common_numbers)]

def determine_value(hand, hand_type):
    return                            MAP_CARD[hand[4]]  \
           + 20 *                     MAP_CARD[hand[3]]  \
           + 20 * 20 *                MAP_CARD[hand[2]]  \
           + 20 * 20 * 20 *           MAP_CARD[hand[1]]  \
           + 20 * 20 * 20 * 20 *      MAP_CARD[hand[0]]  \
           + 20 * 20 * 20 * 20 * 20 * hand_type

# Add 'type' number and 'value' number to a hand.
# The value number is some what arbitrary but reflects the hand...
for hand in hands:
    hand['type']  = determine_type(hand['hand']) 
    hand['value'] = determine_value(hand['hand'], hand['type'])

def determine_total_winnings():
    # sorteren van hoog naar laag
    hands.sort(key=lambda h: h['value'])

    total_winnings = 0
    for number, hand in enumerate(hands):
        total_winnings += (number+1) * hand['bid']
    
    return total_winnings

print('Solution part 1:', determine_total_winnings())

# Part 2

# although a 'Python constant' we have to change this...
MAP_CARD['J'] = 1

def determine_best_type_with_jokers(hand):
    best_type_so_far = 1 # HIGH_CARD, maw laagste waarde
    for card in MAP_CARD.keys():
        replaced_hand = hand.replace('J', card)
        possible_type = determine_type(replaced_hand)
        if possible_type > best_type_so_far:
            best_type_so_far = possible_type
    return best_type_so_far

# Dit moeten we opnieuw doen maar dan iets anders
for hand in hands:
    hand['type']  = determine_best_type_with_jokers(hand['hand']) 
    hand['value'] = determine_value(hand['hand'], hand['type'])

print('Solution part 2:', determine_total_winnings())

