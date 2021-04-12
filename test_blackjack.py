import blackjack

def test_new_deck_has_52_cards():
    deck = blackjack.BlackjackDeck()
    assert len(deck.cards) == 52

