from typing import List

from entities.card import Card


class Hand:
    """A hand of cards to be played. Either from the banker or the player.

    Args:
        cards: list, a list of card objects to be added to the hand
            using the add_cards() method.

    Atributes:
        cards: list, a list of card type objects.
        value: int, the sum of the individual card values according to
            baccarat rules.
    """

    def __init__(self, cards: List[Card]):
        self._cards = []
        self.add_cards(cards)

    @property
    def cards(self):
        """Get hand cards list."""
        return self._cards

    @property
    def value(self):
        """Get hand value."""
        return sum(self._cards)

    def add_cards(self, cards):
        """Add cards to the hand object.

        Args:
            cards: list, a list of card type objects.

        Raises:
            TypeError: when a object different from card is present on the list
                used as argument to the add_card() method.
        """
        for card in cards:
            if not isinstance(card, Card):
                raise TypeError("Not a valid Card type object.")
            self._cards.append(card)

    def is_natural(self):
        """Check if the hand is a natural according to the rules of
        the game.

        Returns:
            bol, True if is a natural, False otherwise.
        """
        if len(self._cards) == 2 and 8 <= self.value <= 9:
            return True
        return False

    def __repr__(self):
        """Return the representation string as if the object was
        called when creating a new instance.
        """
        return f"Hand({self._cards})"

    def __str__(self):
        """Return a string with all the cards on the hand."""
        return ", ".join([card.__str__() for card in self._cards])
