from entities.game import Game


class Cli:
    def __init__(self, hands: int):
        self.score = {"player": 0, "banker": 0, "tie": 0}
        self.hands = hands

        self.run_game()

    def run_game(self):
        for hand in range(self.hands):
            game = Game()
            game.deal_hands()
            game.draw_thirds()

            self.score[game.game_result()] += 1

    def print_results(self):
        print(
            f"Player: {self.score['player']} ({self.score['player'] / self.hands * 100:.2f}%)"
        )
        print(
            f"Banker: {self.score['banker']} ({self.score['banker'] / self.hands * 100:.2f}%)"
        )
        print(f"Tie: {self.score['tie']} ({self.score['tie'] / self.hands * 100:.2f}%)")
