from entities.card import Card
from entities.hand import Hand


class Banker(Hand):
    """Banker (banco) hand of baccarat. Adds the third card check for
    the banker. Subclass of Hand.
    """

    def __init__(self, cards):
        Hand.__init__(self, cards)

    def draw_third(self, player_third: Card = None):
        """Verifies the need of a third card draw.

        Args:
            player_third: Card object, third card of the player.

        Returns:
            bool, True if there is need to a third card draw,
                False otherwise.
        """
        third_card_rules = {
            3: [0, 1, 2, 3, 4, 5, 6, 7, 9],
            4: [2, 3, 4, 5, 6, 7],
            5: [4, 5, 6, 7],
            6: [6, 7],
        }

        if len(self._cards) == 2:
            if player_third:
                if not isinstance(player_third, Card):
                    raise TypeError("Player third card not a Card type object.")
                if 0 <= self.value <= 2:
                    return True
                elif 3 <= self.value <= 6:
                    if player_third.value in third_card_rules[self.value]:
                        return True
            else:
                if 0 <= self.value <= 5:
                    return True
        return False
