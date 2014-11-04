"""
Project Euler Problem #54
==========================

In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

  * High Card: Highest value card.
  * One Pair: Two cards of the same value.
  * Two Pairs: Two different pairs.
  * Three of a Kind: Three cards of the same value.
  * Straight: All cards are consecutive values.
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


# Clubs, Diamonds, Hearts, Spades
suits = 'CDHS'

# The higher the index, the higher the value:
cards = ['2', '3', '4', '5', '6', '7',  
         '8', '9', 'T', 'J', 'Q', 'K', 'A'] # Jack, Queen, King, Ace



def score(hand):
  
  hand = hand.split()
  values, suits = map(list, zip(*hand))
  
  # Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
  if set(['T', 'J', 'Q', 'K', 'A']) == set(values) and len(set(suits)) == 1:
      player_score = 10

  # Straight Flush: All cards are consecutive values of same suit.
  elif sorted([cards.index(val) for val in values])[4] - \
       sorted([cards.index(val) for val in values])[0] == 4 and \
       len(set(values)) == 5 and \
       len(set(suits)) == 1:
      player_score = 9

  # Four of a Kind: Four cards of the same value.
  elif 4 in Counter(values).values():
      player_score = 8
    
  # Full House: Three of a kind and a pair. '5C 5D 6H 6S 9S'
  elif 3 in Counter(values).values() and 2 in Counter(values).values():
      player_score = 7
    
  # Flush: All cards of the same suit.
  elif len(set(suits)) == 1:
      player_score = 6

  # Straight: All cards are consecutive values. 5C 5D 5H 8C 9S
  elif sorted([cards.index(val) for val in values])[4] - \
       sorted([cards.index(val) for val in values])[0] == 4 and \
       len(set(values)) == 5:
      player_score = 5

  # Three of a Kind: Three cards of the same value.
  elif 3 in Counter(values).values():
      player_score = 4

  # Two Pairs: Two different pairs.
  elif 2 in Counter(Counter(values).values()).values(): # Explain this!
    player_score = 3

  # One Pair: Two cards of the same value.
  elif 2 in Counter(values).values():
      player_score = 2

  # High Card: Highest value card.
  else:
      player_score = 1 # * max(sorted(cards.index(values)))

  return player_score


# --------------------------------------------------------------
# Tests:

# Suits: Clubs, Diamonds, Hearts, Spades


# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
assert score('TC JC QC KC AC') == 10
assert score('TD JD QD KD AC') != 10

# Straight Flush: All cards are consecutive values of same suit.
assert score('9C TC JC QC KC') == 9
assert score('2C 3C 4C 5C 6H') != 9

# Four of a Kind: Four cards of the same value.
assert score('9D 9S 9H 9C KH') == 8
assert score('9D 9S 9H TC KH') != 8

# Full House: Three of a kind and a pair.
assert score('2H 2D 4C 4D 4S') == 7
assert score('3C 3D 3S 9S 9D') == 7
# assert score('5H AD 6C AH 9C') != 7

# Flush: All cards of the same suit.
assert score('5C 6C 7C 8C KC') == 6
assert score('2C 4C 6C 9C KS') != 6

# Straight: All cards are consecutive values [BUT NOT OF SAME SUITE!].
assert score('5C 6C 7C 8C 9H') == 5
assert score('5C 6C KC 8C 9C') != 5

# Three of a Kind: Three cards of the same value. 
assert score('5C 5D 5H 8C 9S') == 4
assert score('5C 5D 6H 8C 9S') != 4 

# Two Pairs: Two different pairs.
assert score('5C 5D 6H 6S 9S') == 3
assert score('5C 5D 6H 7S 9S') != 3

# One Pair: Two cards of the same value.
assert score('5C 5D 6H 7S 9S') == 2
assert score('2C 5D 6H 7S 9S') != 2

# High Card: Highest value card.
assert score('5C 6D 3H 7S 9S') == 1
assert score('5C 5D 6H 7S 9S') != 1