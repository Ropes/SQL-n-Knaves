from __future__ import print_function, unicode_literals

from pprint import pformat
from random import shuffle

from cards.card import Card, suits, ranks, wild

class Deck(object):
    '''Deck with handle Card creation, shuffling, and dealing.

    Attributes:
    cards(list[Card]): List of card objects to operate from

    Args:
        jokers(bool, int): False if no jokers to be put in deck else num to add
        shuffle(bool): Shuffle deck after initialization
    '''

    def __init__(self, jokers=False, shuffle=True):
        self.cards = []
        for suit, ranks in suits.items():
            if suit != 'Wild':
                for rank in ranks:
                    self.cards.append(Card(suit, rank)) 
            elif suit == 'Wild' and jokers:
                self.cards.extend(\
                        [ Card('Wild', 'Joker') for x in range(jokers)])
        self.shuffle()

    def __unicode__(self):
        c_str = '\n'.join([ unicode(c) for c in self.cards ])
        return 'Deck:\n{}'.format(c_str)
        
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
        '''Shuffles list of cards in place
        Attribute shuffled: self.cards
        '''
        shuffle(self.cards)

    def deal(self):
        '''Deal a card from the deck.
        If no cards left in deck None is returned.
        '''
        return self.cards.pop()  if len(self.cards) > 0 else None

