import pytest
import cards


def test_cards_blackjackValue_ace():
    card = cards.Card("clubs", "ace")
    assert card.blackjackValue() == 11


@pytest.mark.parametrize("rank", ["jack", "queen", "king"])
def test_cards_blackjackValue_jack_queen_king(rank):
    card = cards.Card("diamonds", rank)
    assert card.blackjackValue() == 10


@pytest.mark.parametrize("rank", ["2", "3", "4", "5", "6", "7", "8", "9", "10"])
def test_cards_blackjackValue_number_cards(rank):
    card = cards.Card("hearts", rank)
    assert card.blackjackValue() == int(rank)
