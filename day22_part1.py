#!/usr/bin/python3

import loader

#inp = loader.string_list("input_day22")
#inp = loader.integer_list("input_day22")
inp = loader.blank_line_delimited("input_day22")
#inp = loader.CharacterGrid("input_day22")


player_1_deck = [int(num) for num in inp[0][1:]]
player_1_deck.reverse() #index 0 is bottom of deck
player_2_deck = [int(num) for num in inp[1][1:]]
player_2_deck.reverse() #index 0 is bottom of deck

def play_one_round():
    player_1_top_card = player_1_deck.pop()
    player_2_top_card = player_2_deck.pop()
    if player_1_top_card > player_2_top_card:
        player_1_deck.insert(0,player_1_top_card)
        player_1_deck.insert(0,player_2_top_card)
    elif player_2_top_card > player_1_top_card:
        player_2_deck.insert(0,player_2_top_card)
        player_2_deck.insert(0,player_1_top_card)
    else:
        raise RuntimeError("Two equal cards played against each other.")

while len(player_1_deck) != 0 and len(player_2_deck) != 0:
    play_one_round()

def score_deck(player_deck):
    total_score = 0
    for i in range(len(player_deck)):
        total_score += (i+1)*player_deck[i]
    return total_score

print(score_deck(player_1_deck)+score_deck(player_2_deck))
