import blackjack
import cards


def test_new_deck_has_52_cards():
    deck = blackjack.BlackjackDeck()
    assert len(deck.cards) == 52


def test_hand_value_with_one_ace():
    class TestDeck(blackjack.BlackjackDeck):
        def __init__(self):
            self.SUITS = ["clubs"]
            self.RANKS = ["ace", "9"]
            self.cards = list()
            self.build()

    deck = TestDeck()
    hand = blackjack.Hand(deck)
    hand.addCard(cards.Card("clubs", "10"))
    assert hand.value() == 20
