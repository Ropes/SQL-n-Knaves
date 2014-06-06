from __future__ import print_function, unicode_literals


class Card(object):
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __unicode__(self):
        return '{rank} of {suit}'.format(rank=self.rank, suit=self.suit)
