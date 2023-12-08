
import sys
sys.path.append("..") 
import aoc_lib as aoc

# parse the file
lines = aoc.lines_from_file('input.txt')
cards = {}
for line in lines:
    part_1, part_2 = line.split(':')
    _, card_no_str = part_1.split()
    card_no = int(card_no_str)
    winning_numbers_str, my_numbers_str = part_2.split('|')
    winning_numbers = aoc.numbers_from_str(winning_numbers_str)
    my_numbers      = aoc.numbers_from_str(my_numbers_str)
    cards[card_no] = {'win' : winning_numbers, 'my' : my_numbers}


# part 1:
total_points = 0
for k,v in cards.items():
    winners = set(v['win']).intersection(set(v['my']))
    n_winners = len(winners)
    if n_winners:
        total_points += 2 ** (n_winners - 1)

print('Solution part 1:', total_points)

# part 2:

if False: # cool, nu wordt het leuk, deze naieve oplossing duurde te lang....

    unprocessed_cards = list(range(1, len(cards)+1))  # copies will be added
    processed_cards = []
    while unprocessed_cards:
        card_no = unprocessed_cards.pop(0)
        processed_cards.append(card_no)
        winners = set(cards[card_no]['win']).intersection(set(cards[card_no]['my']))
        for i in range(len(winners)):
            unprocessed_cards.append(card_no + i + 1)
        print(card_no, len(unprocessed_cards), len(processed_cards))

    print('Solution part 2:', len(processed_cards))

# we moeten een beter plan verzinnen...
# - cachen ?
# - achteraan beginnen...

card_nos          = list(range(1, len(cards)+1))
card_nos_reversed = list(range(len(cards), 0, -1))

card_copies = {}
for card_no in card_nos:
        winners = set(cards[card_no]['win']).intersection(set(cards[card_no]['my']))
        card_copies[card_no] = [card_no + i + 1 for i in range(len(winners))]

card_no_processed = {}
for card_no in card_nos_reversed:
    cards = 1 # the original
    for card in card_copies[card_no]:
        cards += card_no_processed[card]
    card_no_processed[card_no] = cards
    
print('Solution part 2:', sum(card_no_processed.values()))

