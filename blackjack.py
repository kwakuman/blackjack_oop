# blackjack.py, a game of blackjack against a CPU

import random
import sys
import cards


def main():
    print(
        'Hello, let\'s play some blackjack, shall we? (type in "yes" to play or "quit" to quit.)'
    )
    playerChoice = input("> ").lower()
    # playerChoice = "y"
    while playerChoice not in ["yes", "quit"]:
        print('Please answer "yes" to play the game or "quit" to end the programme.')
        playerChoice = input("> ").lower()
    if playerChoice.startswith("q"):
        print("Ok, bye bye then")
        sys.exit()
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
            playerHand.addCard(deck.drawCard())
            continue

        # let CPU draw cards, if it wishes to
        if playerHand.value() > CPUHand.value():  # if player has higher score than CPU
            while (
                playerHand.value() <= 21 and CPUHand.value() < 21
            ):  # player is winning at the moment
                CPUHand.addCard(deck.drawCard())
                print(f"CPU has drawed {CPUHand.cards[-1]}")

        print(f"You have {playerHand}")
        print(f"Banker has {CPUHand}")
        # evaluate the results of the round
        playerScore = playerHand.value()
        CPUScore = CPUHand.value()
        if playerScore > 21:
            print("You are bust, you lose.")
            sys.exit()
        if CPUScore > 21:
            print("The banker is bust, you win.")
            sys.exit()
        if playerScore == CPUScore:
            print("It's a tie.")
            sys.exit()
        if playerScore > CPUScore:
            print("You have a higher score, you win.")
            sys.exit()
        if CPUScore > playerScore:
            print("Banker has a higher score, you lose.")
            sys.exit()


class BlackjackDeckException(Exception):
    pass


class BlackjackDeck:
    def __init__(self):
        """Create deck of cards for one game of Blackjack."""
        self.SUITS = ["clubs", "diamonds", "spades", "hearts"]
        self.RANKS = [
            "ace",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "jack",
            "queen",
            "king",
        ]
        self.cards = list()
        self.build()

    def build(self):
        """Builds new deck of cards."""
        # set suits and ranks the deck will be made of
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.cards.append(cards.Card(suit, rank))

    def drawCard(self):
        """Draws a random card from the deck (the card is not returned back to the deck."""
        drawedCard = random.choice(self.cards)
        return self.cards.pop(self.cards.index(drawedCard))

    def __repr__(self):
        return f"{self.__class__.__qualname__}(Deck of {len(self.cards)}/{len(self.SUITS) * len(self.RANKS)} cards.)"

    def __str__(self):
        return f"Deck of cards. {len(self.cards)}/{len(self.SUITS) * len(self.RANKS)} left."


class Hand:
    def __init__(self, deck):
        """Creates a player's hand with two cards from the game card deck."""
        self.cards = list()
        self.cards.append(deck.drawCard())
        self.cards.append(deck.drawCard())

    def addCard(self, card):
        """Adds a card from deck of cards to hand."""
        self.cards.append(card)

    def acesInHand(self):
        """Returns number of Aces(int) in the Hand object."""
        numberOfAces = 0
        for card in self.cards:
            if card.rank == "ace":
                numberOfAces += 1
        return numberOfAces

    def value(self):
        """Returns a value of all the cards in hand."""
        handValue = 0
        for card in self.cards:
            handValue += card.blackjackValue()
        aces = self.acesInHand()
        # check if there are aces to be counted as one instead of eleven
        while aces > 0:
            if handValue > 21:
                handValue -= 10
                aces -= 1
            if handValue < 21:
                break
        return handValue

    def showFirstCard(self):
        """Shows first card in a Hand object in human readable form."""
        return self.cards[0]

    def __str__(self):
        HumanReadableHand = str()
        for card in self.cards:
            HumanReadableHand += f"{card}, "
        HumanReadableHand = HumanReadableHand[:-2]
        return HumanReadableHand


if __name__ == "__main__":
    main()
