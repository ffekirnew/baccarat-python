from entities.banker import Banker
from entities.deck import Deck
from entities.player import Player


class Game:
    def __init__(self):
        self._deck = Deck()
        self._player = None
        self._banker = None

    def deal_hands(self):
        """Deals both hands. Creates a Punto and Banco instance and pops two
        cards from the Shoe instance. Sets the game as open.

        """
        self._player = Player(self._deck.draw_cards(2))
        self._banker = Banker(self._deck.draw_cards(2))

    def draw_thirds(self):
        """Applies the third card drawing rules to draw a possible third card
        for both hands. Closes the game.

        Returns: list with tuples, each tuple contains the hand and card that
            was drawn to which the third card rules were applied.

        """

        third_draws = []
        if self._player.draw_third():
            self._player.add_cards(self._deck.draw_cards(1))
            third_draws.append(["player", self._player.cards[2].__str__()])
            if self._banker.draw_third(self._player.cards[2]):
                self._banker.add_cards(self._deck.draw_cards(1))
                third_draws.append(["banker", self._banker.cards[2].__str__()])
        elif self._banker.draw_third():
            self._banker.add_cards(self._deck.draw_cards(1))
            third_draws.append(["banker", self._banker.cards[2].__str__()])
        self._game_running = False
        return third_draws

    def game_result(self):
        """Checks was is the result of the game.

        Returns:
            str, with the winning hand or 'tie' in case is a tie.

        """
        if self._player.value > self._banker.value:
            return "player"
        elif self._player.value < self._banker.value:
            return "banker"
        else:
            return "tie"
