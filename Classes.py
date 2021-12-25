# ---------------------------------------------------------------------------- #
#        This document has all the classes information for this project        #
# ---------------------------------------------------------------------------- #
from random import shuffle


# ----------------------------- global variables ----------------------------- #

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

# --------------------------------------------------------------------------- #

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    
    # ---------------------------- make a deck of card --------------------------- #
    
    def __init__(self):
        self.all_cards = [] 
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
    
    # ---------------------------------------------------------------------------- #                
    
    def __str__(self):
        deck = ''
        for cards in self.deck:
            deck += '\n ' + Card.__str__()
        return 'The deck has:' + deck

    def shuffle_cards(self):
        shuffle(self.all_cards)
        
    def deal_one(self):
        # dealer removes a card.
        card = self.all_cards.pop()
        return card

class Player:
    
    def __init__(self,name):
        self.name = name
        self.all_cards = [] # initialize list
        
    
    def add_cards(self,new_cards):
        self.all_cards.append(new_cards)
    
    
    def __str__(self):
        return f'Player {self.name} has {self.all_cards}.\n'

class Chips:
    
    def __init__(self,total):
        self.bet = 0
        self.total = total

        
    def __str__(self):

        return f'You have ${self.total} in chips.\n'

    def win_turn(self):
        self.total += self.bet


    def lose_turn(self):
        self.total -= self.bet
    
class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_cards(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

    def ace_flip(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# -------------------------------- end of file ------------------------------- #