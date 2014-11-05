#376
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

from collections import deque
from collections import Counter



suits = 'CDHS' # Clubs, Diamonds, Hearts, Spades

# The higher the index, the higher the value:
cards = ['2', '3', '4', '5', '6', '7',  
         '8', '9', 'T', 'J', 'Q', 'K', 'A'] # Jack, Queen, King, Ace



def score(hand):
  
  hand = hand.split()
  values, suits = map(list, zip(*hand))
  
  # Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
  if set(['T', 'J', 'Q', 'K', 'A']) == set(values) and len(set(suits)) == 1:
      player_score = (10) 
      print 'Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.'


  # Straight Flush: All cards are consecutive values of same suit.
  elif sorted([cards.index(val) for val in values])[4] - \
       sorted([cards.index(val) for val in values])[0] == 4 and \
       len(set(values)) == 5 and \
       len(set(suits)) == 1:
      player_score = (9, sorted([cards.index(val) for val in values])[4])
      print 'Straight Flush: All cards are consecutive values of same suit.'


  # Four of a Kind: Four cards of the same value.
  elif 4 in Counter(values).values():
      player_score = (8, [val for val, count in Counter(values).items() if count == 4][0], [val for val, count in Counter(values).items() if count == 1][0])
      print 'Four of a Kind: Four cards of the same value.'

  # Full House: Three of a kind and a pair. 
  elif 3 in Counter(values).values() and 2 in Counter(values).values():
      player_score = (7, [val for val, count in Counter(values).items() if count == 3][0], [val for val, count in Counter(values).items() if count == 2][0])
      print 'Full House: Three of a kind and a pair.'

  # Flush: All cards of the same suit.
  elif len(set(suits)) == 1:
      player_score = (6, sorted([cards.index(val) for val in values])[4],
                         sorted([cards.index(val) for val in values])[3],
                         sorted([cards.index(val) for val in values])[2],
                         sorted([cards.index(val) for val in values])[1],
                         sorted([cards.index(val) for val in values])[0])
      print 'Flush: All cards of the same suit.'

  # Straight: All cards are consecutive values. 
  elif sorted([cards.index(val) for val in values])[4] - \
       sorted([cards.index(val) for val in values])[0] == 4 and \
       len(set(values)) == 5:
      player_score = (5, max([cards.index(val) for val in values]))
      print 'Straight: All cards are consecutive values.'

  # Three of a Kind: Three cards of the same value.
  elif 3 in Counter(values).values():
      player_score = (4, [val for val, count in Counter(values).items() if count == 3][0], max([val for val, count in Counter(values).items() if count == 1]), min([val for val, count in Counter(values).items() if count == 1]))
      print 'Three of a Kind: Three cards of the same value.'
  
  # Two Pairs: Two different pairs.
  elif 2 in Counter(Counter(values).values()).values(): # Explain this!
    player_score = (3, max([val for val, count in Counter(values).items() if count == 2]), min([val for val, count in Counter(values).items() if count == 2]), [val for val, count in Counter(values).items() if count == 1][0])
    print 'Two Pairs: Two different pairs.'
  
  # One Pair: Two cards of the same value.
  elif 2 in Counter(values).values():

      player_score = (2, cards.index([val for val, count in Counter(values).items() if count == 2][0])) + tuple(reversed(sorted([cards.index(val) for val, count in Counter(values).items() if count == 1])))

        # sorted([cards.index(val) for val in values])[2], 
        #                 sorted([cards.index(val) for val in values])[2], 
        #                 sorted([cards.index(val) for val in values])[1],
        #                 sorted([cards.index(val) for val in values])[0])
      print 'One Pair: Two cards of the same value.'

  # High Card: Highest value card.
  else:
      player_score = (1, max([cards.index(val) for val in values]))
      print 'High Card: Highest value card.'

  return player_score


player_one_tally = 0
with open('PE054_hands.txt') as f:
  for line in f.readlines():
    player_one = line[:14].strip()
    player_two = line[14:].strip().strip('\n')
    print 
    print '*'*20
    player_one_score = deque(score(player_one))
    player_two_score = deque(score(player_two))

    while (player_one_score and player_two_score):
      one = player_one_score.popleft()
      two = player_two_score.popleft()
      #temp = raw_input()
      if one > two:
        player_one_tally += 1
        print "Player 1 wins:    ", player_one, '      ', player_two
        break 
      elif one < two: 
        print "Player 2 wins:    ", player_one, '      ', player_two 
        break 
      else: 
        continue



print player_one_tally


     

