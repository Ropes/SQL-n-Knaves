from __future__ import print_function, unicode_literals

import unittest

from cards.deck import Deck
from cards.card import Card

class TestDeck(unittest.TestCase):

    def test_init(self):
        d = Deck(jokers=False)
        self.assertEqual(len(d.cards), 52)

    def test_init_jokers(self):
        d = Deck(jokers=2)
        self.assertEqual(len(d.cards), 54)

    def test_deck_contains_ace_of_hearts(self):
        d = Deck()
        c = Card('Hearts', 'Ace')

        self.assertTrue(d.contains(c))

    def test_deck_unicode(self):
        d = Deck()
        d.shuffle()
        s = unicode(d)
        print(s)

        self.assertEqual(type(s),unicode)

