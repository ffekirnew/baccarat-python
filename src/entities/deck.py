from random import shuffle
from typing import List

from entities.card import RANKS, SUITS, Card


class Deck:
    """Deck class. This class contains a list of cards
    and methods to manipulate the deck.

    Attributes:
        _cards: list, list of cards in deck.
    """

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in RANKS for suit in SUITS]
        self.shuffle()

    @property
    def cards(self) -> List[Card]:
        """Returns current list of cards in deck."""
        return self._cards

    def shuffle(self) -> None:
        """Shuffles the deck."""
        shuffle(self._cards)

    def refill_deck(self) -> None:
        """Refills the deck with a new set of cards."""
        self._cards = [Card(rank, suit) for rank in RANKS for suit in SUITS]
        self.shuffle()

    def draw_cards(self, num_cards: int = 2) -> List[Card]:
        """Draws cards from shoe. Refills the shoe when
        it is empty.

        Args:
            num_cards: int, number of cards to be drawn.

        Returns:
            cards_drawn: list, cards drawn from shoe.
        """
        cards_drawn = []
        for i in range(num_cards):
            if len(self._cards) == 0:
                self.refill_deck()
            cards_drawn.append(self._cards.pop())
        return cards_drawn
