from __future__ import print_function, unicode_literals

from cards.card import Card, suits, ranks, wild

class Deck(object):
    '''Deck with handle Card creation, shuffling, and dealing.

    Attributes:
    cards(list[Card]): List of card objects to operate from

    Args:
        jokers(bool, int): False if no jokers to be put in deck else num to add
    
    '''

    def __init__(self, jokers=False):
        self.cards = []
        for suit, ranks in suits.items():
            if suit != 'Wild':
                for rank in ranks:
                    self.cards.append(Card(suit, rank)) 
            elif suit == 'Wild' and jokers:
                self.cards.extend(\
                        [ Card('Wild', 'Joker') for x in range(jokers)])
        
    def contains(self, card):
        '''Check if card is contained in deck.
        Args:
            card (Card): value to be searched for
        
        Returns:
            True if Card found else False'''
        for c in self.cards:
            if c == card:
                return True
        return False
        
    def shuffle(self):
        #TODO
        pass

    def deal(self, num=1):
        #TODO
        pass
