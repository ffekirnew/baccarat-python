from entities.hand import Hand


class Player(Hand):
    """Player (punto) hand of baccarat. Adds the third card check for
    the player. Subclass of Hand.
    """

    def __init__(self, cards):
        Hand.__init__(self, cards)

    def draw_third(self):
        """Verifies the need of a third card draw.

        Returns:
            bol, True if there is need to a third card draw,
                False otherwise.
        """
        if len(self._cards) == 2:
            if 0 <= self.value <= 5:
                return True
        return False
