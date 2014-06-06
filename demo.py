#!/usr/bin/python2.7
from __future__ import print_function, unicode_literals

import random

from cards.card import Card
from cards.deck import Deck

random.seed(5)

def get_cards(deck, number):
    return [ deck.deal() for i in range(number) ]

if __name__ == '__main__':
    d = Deck(jokers=2)
    print(unicode(d))

    #Shuffle the deck again
    d.shuffle()
    print("\nPost shuffling again:")
    print(unicode(d))

    #Get a hand of cards from the deck
    print('\nDealt Hand:')
    hand = get_cards(d, 5)
    for c in hand:
        print(unicode(c))

    #Make sure one of the cards dealt is no longer in the deck
    check_card = hand[1]
    print('\n{} in deck? {}'.format(unicode(check_card),\
                                    d.contains(check_card)))

    #Check if a card is still in the deck
    print('\nJoker in deck? {}'.format(d.contains(Card('Wild', 'Joker'))))

