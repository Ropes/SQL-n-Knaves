from __future__ import print_function, unicode_literals

import unittest

from cards.deck import Deck

class TestDeck(unittest.TestCase):

    def test_init(self):
        d = Deck(jokers=False)
        self.assertEqual(len(d.cards), 52)

    def test_init_jokers(self):
        d = Deck(jokers=2)
        self.assertEqual(len(d.cards), 54)

