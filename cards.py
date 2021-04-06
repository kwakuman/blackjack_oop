# cards.py, a module containing cards and deck to play card games with

# sett suits and ranks that cards can be made from
SUITS = ["clubs", "diamonds", "spades", "hearts"]
RANKS = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]


class CardException(Exception):
    """The card module raises this when the module is misused."""

    pass


class Card:
    def __init__(self, suit, rank):
        """Create a card object with given suit and rank"""
        self.suit = suit.lower()
        self.rank = rank.lower()

    def blackjackValue(self):
        """Returns value of the card object in blackjack."""
        NUMBERRANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
        FACECARDS = ["jack", "queen", "king"]
        ACE = ["ace"]
        if self.rank in NUMBERRANKS:
            return int(self.rank)
        elif self.rank in FACECARDS:
            return 10
        elif self.rank in ACE:
            return 11

    @property
    def suit(self):
        """Returns the suit of the card object."""
        return self._suit

    @suit.setter
    def suit(self, value):
        if value.lower() not in SUITS:
            raise CardException(
                "A card can only be one of four suits "
                + str(SUITS)
                + " not a "
                + value.__class__.__qualname__
            )
        self._suit = value

    @property
    def rank(self):
        """Returns the rank of the card object"""
        return self._rank

    @rank.setter
    def rank(self, value):
        if value.lower() not in RANKS:
            raise CardException(
                "A card must be one of allowed ranks "
                + str(RANKS)
                + "not a "
                + value.__class__.__qualname__
            )
        self._rank = value

    def __repr__(self):
        """Returns a string of an expression that re-creates this object."""
        return (
            f"{self.__class__.__qualname__}({self.rank.title()} of {self.suit.title()})"
        )

    def __str__(self):
        """Returns human readable expression of the card object."""
        return f"{self.rank.title()} of {self.suit.title()}"
