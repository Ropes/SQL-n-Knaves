from __future__ import print_function, unicode_literals

import unittest
from collections import defaultdict
import random

from cards.deck import Deck
from cards.card import Card

class TestDeck(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        random.seed(5)

    def test_init(self):
        d = Deck(jokers=False)
        self.assertEqual(len(d.cards), 52)
        self.assertFalse(d.contains(Card('Wild', 'Joker')))

    def test_init_jokers(self):
        d = Deck(jokers=2)
        self.assertEqual(len(d.cards), 54)
        self.assertTrue(d.contains(Card('Wild', 'Joker')))

    def test_deck_contains_ace_of_hearts(self):
        d = Deck()
        c = Card('Hearts', 'Ace')

        self.assertTrue(d.contains(c))

    def test_deck_unicode(self):
        d = Deck()
        s = unicode(d)
        print(s)

        self.assertEqual(type(s),unicode)

    def test_deck_deal(self):
        d = Deck()

        c = d.deal()
        self.assertFalse(d.contains(c))

        d2 = Deck()
        self.assertTrue(d2.contains(c))

    def test_shuffle(self):
        d = Deck()

        cards = [ d.deal() for r in range(20) ]
        print(cards)
        print(unicode(d))

        card_count = defaultdict(int)
        for c in cards:
            card_count[c.suit] += 1

        print(card_count)

        self.assertGreater(card_count['Spades'], 4)
        self.assertGreater(card_count['Hearts'], 6)
        self.assertGreater(card_count['Clubs'], 4)

        self.assertEqual(1,2)
