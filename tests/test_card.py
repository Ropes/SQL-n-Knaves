from __future__ import print_function, unicode_literals

import unittest

from cards.card import Card

class TestCards(unittest.TestCase):
    
    def test_init(self):
        suit = 'Spades'
        rank = 'Ace' 
        c = Card(suit, rank)

        self.assertEqual(c.suit, suit)
        self.assertEqual(c.rank, rank)
        self.assertEqual(unicode(c), 'Ace of Spades')

    def test_incorrect_init(self):

        self.assertRaises(ValueError, Card, 'Batman', 'Joker')
        #TODO: The following should be an error
        #self.assertRaises(ValueError, Card, 'Spades', 'Joker')
        self.assertRaises(ValueError, Card, 'Spades', 'Five')

    def test_equality(self):
        x = Card('Spades', 'Ace')
        y = Card('Diamonds', 'King')
        z = Card('Spades', 'Ace')

        self.assertNotEqual(x,y)
        self.assertEqual(x,z)
        
