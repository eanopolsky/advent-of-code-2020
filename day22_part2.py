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


def score_deck(player_deck):
    total_score = 0
    for i in range(len(player_deck)):
        total_score += (i+1)*player_deck[i]
    return total_score

def play_recursive_combat(player_1_deck, player_2_deck):
    """
    Returns a tuple: (winner, score). Winner may be 1 or 2 to indicate which player won.
    Score is the winner's score.
    """
    this_game_history = set() # contains tuples of deck content tuples: tuple(tuple(deck1),tuple(deck2))
    while True:
        if (tuple(player_1_deck),tuple(player_2_deck)) in this_game_history:
            return (1,score_deck(player_1_deck))
        else:
            this_game_history.add((tuple(player_1_deck),tuple(player_2_deck)))
        if len(player_1_deck) == 0:
            return (2,score_deck(player_2_deck))
        if len(player_2_deck) == 0:
            return (1,score_deck(player_1_deck))
        player_1_top_card = player_1_deck.pop()
        player_2_top_card = player_2_deck.pop()
        if player_1_top_card <= len(player_1_deck) and player_2_top_card <= len(player_2_deck):
            player_1_sub_game_deck = player_1_deck[(-1*player_1_top_card):]
            player_2_sub_game_deck = player_2_deck[(-1*player_2_top_card):]
            results = play_recursive_combat(player_1_sub_game_deck,
                                            player_2_sub_game_deck)
            winner = results[0]
            if winner == 1:
                player_1_deck.insert(0,player_1_top_card)
                player_1_deck.insert(0,player_2_top_card)
            elif winner == 2:
                player_2_deck.insert(0,player_2_top_card)
                player_2_deck.insert(0,player_1_top_card)
            else:
                raise RuntimeError("Two equal cards played against each other.")
        else: # play a regular round
            if player_1_top_card > player_2_top_card:
                player_1_deck.insert(0,player_1_top_card)
                player_1_deck.insert(0,player_2_top_card)
            elif player_2_top_card > player_1_top_card:
                player_2_deck.insert(0,player_2_top_card)
                player_2_deck.insert(0,player_1_top_card)
            else:
                raise RuntimeError("Two equal cards played against each other.")
            
results = play_recursive_combat(player_1_deck,player_2_deck)
print(results[1])
