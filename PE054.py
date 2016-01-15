"""
Project Euler Problem #54
==========================

In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

  * High Card: Highest value card.
  * One Pair: Two cards of the same value.
  * Two Pairs: Two different pairs.
  * Three of a Kind: Three cards of the same value.
  * Straight: All cards are consecutive player_values.
  * Flush: All cards of the same suit.
  * Full House: Three of a kind and a pair.
  * Four of a Kind: Four cards of the same value.
  * Straight Flush: All cards are consecutive values of same suit.
  * Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the
highest value wins; for example, a pair of eights beats a pair of fives
(see example 1 below). But if two ranks tie, for example, both players
have a pair of queens, then highest cards in each hand are compared (see
example 4 below); if the highest cards tie then the next highest cards are
compared, and so on.

Consider the following five hands dealt to two players:

        Hand   Player 1            Player 2              Winner

        1      5H 5C 6S 7S KD      2C 3S 8S 8D TD        Player 2
               Pair of Fives       Pair of Eights
        
        2      5D 8C 9S JS AC      2C 5C 7D 8S QH        Player 1
               Highest card Ace    Highest card Queen
        
        3      2D 9C AS AH AC      3D 6D 7D TD QD        Player 2
               Three Aces          Flush with Diamonds
        
        4      4D 6S 9H QH QC      3D 6D 7H QD QS
               Pair of Queens      Pair of Queens        Player 1
               Highest card Nine   Highest card Seven
        
        5      2H 2D 4C 4D 4S      3C 3D 3S 9S 9D
               Full House          Full House            Player 1
               With Three Fours    with Three Threes

The file poker.txt [http://projecteuler.net/project/poker.txt] contains
one-thousand random hands dealt to two players. Each line of the file contains
ten cards (separated by a single space): the first five are Player 1's cards and
the last five are Player 2's cards. You can assume that all hands are valid (no
invalid characters or repeated cards), each player's hand is in no specific order,
and in each hand there is a clear winner.

How many hands does Player 1 win?
"""

from collections import Counter
from collections import deque


# SUITS: C = Clubs, D = Diamonds, H = Hearts, S = Spades

# The higher the index, the higher the rank:
RANKS = ['2', '3', '4', '5', '6', '7',  
         '8', '9', 'T', 'J', 'Q', 'K', 'A'] # Jack, Queen, King, Ace


def score(hand):
  
    hand_ranks, hand_suits = zip(*hand)

    card_values = sorted([RANKS.index(val) for val in hand_ranks])

    freq_value_pairs = [(freq, RANKS.index(card)) for card, freq in Counter(hand_ranks).items()]

    frequencies = [x[0] for x in freq_value_pairs] 

    tie_breaker_values = [x[1] for x in sorted(freq_value_pairs, reverse=True)]


    # Assign rankings for each combination, from 10 - 1.
    # Break ties by looking at individual cards.
    # Hence, player scores are lists:
    # The hand_score is the first element, followed by 'tie_breaker_values'.

    # Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    if set(hand_ranks) == set('TJQKA') and len(set(hand_ranks)) == 1:
        hand_score = [10] 

    # Straight Flush: All cards are consecutive values of same suit.
    elif card_values[4] - card_values[0] == 4 and \
                    len(set(hand_ranks)) == 5 and \
                    len(set(hand_ranks)) == 1:
        hand_score = [9]

    # Four of a Kind: Four cards of the same value.
    elif 4 in frequencies:
        hand_score = [8]

    # Full House: Three of a kind and a pair. 
    elif 3 in frequencies and 2 in frequencies:
        hand_score = [7]

    # Flush: All cards of the same suit.
    elif len(set(hand_suits)) == 1:
        hand_score = [6]

    # Straight: All cards are consecutive values. 
    elif card_values[4] - card_values[0] == 4 and len(set(hand_ranks)) == 5:
        hand_score = [5]

    # Three of a Kind: Three cards of the same value.
    elif 3 in frequencies:
        hand_score = [4]

    # Two Pairs: Two different pairs.
    elif frequencies.count(2) == 2:
        hand_score = [3]

    # One Pair: Two cards of the same value.
    elif 2 in frequencies:
        hand_score = [2]

    # High Card: Highest value card.
    else:
        hand_score = [1]

    return hand_score + tie_breaker_values



player_one_tally = 0 # 'How many hands does Player 1 win?'

with open('PE054_hands.txt') as f:
    for line in f.readlines():

    # Process file:
    line = line.strip().split()
    player_one, player_two = line[:5], line[5:]

    # Generate scores:
    player_one_score = deque(score(player_one))
    player_two_score = deque(score(player_two))

    # Compare hands:
    while (player_one_score and player_two_score):
        one = player_one_score.popleft()
        two = player_two_score.popleft()

        if one > two: # Player one wins.
            player_one_tally += 1
            break 
        elif one < two: # Player two wins.
            break 
        else: # It's a tie.
            pass 


print 'Player one won', player_one_tally, 'hands.'


     

