import random
import sys
import cards


def main():
    print(
        'Hello, let\'s play some blackjack, shall we? (type in "yes" to play or "quit" to quit.'
    )
    # playerChoice = input('> ')
    playerChoice = "y"
    if playerChoice.lower().startswith("q"):
        print("Ok, bye bye then")
        sys.exit()
    elif not playerChoice.lower().startswith("y"):
        print('Please answer "yes" to play the game or "quit" to end the programme.')
    # create a deck of cards
    deck = BlackjackDeck()
    # create player's and CPU's hand
    playerHand = Hand(deck)
    CPUHand = Hand(deck)
    while True:
        # show players hand and CPUs first card
        print(f"You have: {playerHand}")
        print(f"The banker has: {CPUHand.showFirstCard()}")
        # let player draw cards, if he wishes to
        print('Would you like to draw another card? ("yes" or "no")')
        response = input("> ")
        # if response.lower().startswith('n'):
        #    pass
        if response.lower() not in ["yes", "no"]:
            continue
        if response.lower().startswith("y"):
            playerHand.drawCard(deck)
            continue

        # let CPU draw cards, if it wishes to
        if playerHand.value() > CPUHand.value():  # if player has higher score than CPU
            while (
                playerHand.value() <= 21 and CPUHand.value() <= 21
            ):  # player is winning at the moment
                CPUHand.drawCard(deck)
                print(f"CPU has drawed {CPUHand.cards[-1]}")

        print(f"You have {playerHand}")
        print(f"Banker has {CPUHand}")
        # TODO evaluate the results of the round
        if playerHand.value() > 21:
            print("You are bust, you lose.")
            sys.exit()
        if CPUHand.value() > 21:
            print("The banker is bust, you win.")
            sys.exit()
        if playerHand.value() == CPUHand.value():
            print("It's a tie.")
            sys.exit()
        if playerHand.value() > CPUHand.value():
            print("You have a higher score, you win.")
            sys.exit()
        if CPUHand.value() > playerHand.value():
            print("Banker has a higher score, you lose.")
            sys.exit()


class BlackjackDeck:
    def __init__(self):
        """Create deck of cards for one game of Blackjack."""
        self.cards = list()
        self.build()

    def build(self):
        """Builds new deck of cards."""
        for suit in cards.SUITS:
            for rank in cards.RANKS:
                self.cards.append(cards.Card(suit, rank))

    def drawCard(self):
        """Draws a random card from the deck (the card is not returned back to the deck."""
        drawedCard = random.choice(self.cards)
        return self.cards.pop(self.cards.index(drawedCard))

    def __repr__(self):
        return f"{self.__class__.__qualname__}(Deck of {len(self.cards)}/{len(cards.SUITS) * len(cards.RANKS)} cards.)"

    def __str__(self):
        return f"Deck of cards. {len(self.cards)}/{len(cards.SUITS) * len(cards.RANKS)} left."


class Hand:
    def __init__(self, deck):
        """Creates a player's hand with two cards from the game card deck."""

        self.cards = list()
        self.cards.append(deck.drawCard())
        self.cards.append(deck.drawCard())

    def drawCard(self, deck):
        """Adds a card from deck of cards to hand."""
        self.cards.append(deck.drawCard())

    def aceInHand(self):
        """Returns True if player has an Ace in Hand otherwise returns false."""
        for card in self.cards:
            if card.rank == "ace":
                return True
            else:
                return False

    def value(self):
        """Returns a value of all the cards in hand."""
        handValue = 0
        for card in self.cards:
            handValue += card.blackjackValue()
        return handValue

    def showFirstCard(self):
        """Shows cards in hand in human readable form."""
        return self.cards[0]

    def __str__(self):
        HumanReadableHand = str()
        for card in self.cards:
            HumanReadableHand += f"{card}, "
        HumanReadableHand = HumanReadableHand[:-2]
        return HumanReadableHand


if __name__ == "__main__":
    main()
