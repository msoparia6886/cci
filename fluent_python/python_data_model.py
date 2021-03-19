from collections import namedtuple
from math import hypot

Card = namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [n for n in range(2, 11)] + list('JKQA')
    suits = 'spades diamonds clubs hearts'.split(' ')
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def __init__(self):
        self._cards = [Card(r, s) for r in self.ranks for s in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    @classmethod
    def spades_high(cls, card):
        """
        This will calculate and return the rank of a card in the deck.
        It can be used as a key to sort the deck,
        e.g. sorted(deck, key=FrenchDeck.spades_high)

        param card: The card for which rank needs to be calculated
        """
        rank_value = cls.ranks.index(card.rank)
        return rank_value * len(cls.suits) + cls.suit_values[card.suit]


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return hypot(self.x, self.y)

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __bool__(self):
        return bool(abs(self))

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
