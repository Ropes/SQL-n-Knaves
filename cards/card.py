from __future__ import print_function, unicode_literals


ranks = {'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',\
        'Jack', 'Queen', 'King'}
wild = {'Joker'}

suits = {'Spades': ranks, 'Diamonds': ranks, 'Hearts': ranks, 'Clubs':ranks,\
        'Wild': wild}

class Card(object):
    
    def __init__(self, suit, rank):
        try:
            assert suit in suits
            self.suit = suit
        except:
            raise ValueError, 'Suit given not an acceptable value.'

        try:
            assert rank in suits[suit]
            self.rank = rank
        except:
            raise ValueError, 'Rank given not in acceptable ranks.'

    def __unicode__(self):
        return '{rank} of {suit}'.format(rank=self.rank, suit=self.suit)
    
    def __eq__(self, other):
        return True if self.suit == other.suit and \
                self.rank == other.rank else False

