SUITS = ["hearts", "spades", "clubs", "diamonds"]
RANKS = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"]

SUITS_TYPE = type(SUITS)
RANKS_TYPE = type(RANKS)


class Card:
    """Playing card

    Args:
        rank: int or string, the rank of the card.
        suit: string, the suit of the card.

    Attributes:
        value: int, baccarat value of the card.
        rank: int or string, the rank of the card.
        suit: string, the suit of the card.

    Raises:
        ValueError: On invalid card rank or suit.
    """

    def __init__(self, rank: RANKS_TYPE, suit: SUITS_TYPE):
        if rank not in RANKS:
            raise ValueError("Invalid card rank.")
        if suit not in SUITS:
            raise ValueError("Invalid card suit.")
        self._rank = rank
        self._suit = suit
        self._value = (
            self._rank
            if self._rank in range(2, 10)
            else 1
            if self._rank == "ace"
            else 0
        )

    @property
    def value(self) -> int:
        """Get card value."""
        return self._value

    @property
    def rank(self) -> RANKS_TYPE:
        """Get card rank."""
        return self._rank

    @property
    def suit(self) -> SUITS_TYPE:
        """Get card suit."""
        return self._suit

    def __add__(self, other: "Card") -> int:
        """Add the value of the card to another value."""
        return (self._value + other) % 10

    __radd__ = __add__

    def __repr__(self) -> str:
        """Return the representation string as if the object was
        called when creating a new instance.
        """
        if isinstance(self._rank, str):
            return f"Card('{self._rank}', '{self._suit}')"
        elif isinstance(self._rank, int):
            return f"Card({self._rank}, '{self._suit}')"

    def __str__(self) -> str:
        """Return a string with the rank and suit of the card."""
        return f"Card: {self._rank} of {self._suit}"
