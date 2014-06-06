from __future__ import print_function, unicode_literals

import unittest

from cards.card import Card

class TestCards(unittest.TestCase):
    
    def test_init(self):
        suit = 'Spades'
        
        c = Card('Spades', 'Ace')

        self.assertEqual(c.suit, 'Spades')
        self.assertEqual(c.rank, 'Ace')
        self.assertEqual(unicode(c), 'Ace of Spades')
