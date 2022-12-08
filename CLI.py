from game_objects import Game, PlayerObject, ComputerPlayer


class CLInterface:

    def __init__(self):
        self.game = Game()
        ...

    def set_up(self):
        self.game.add_human_player()
        self.game.add_computer_player()

        self.player0 = self.game.players[0]
        self.player1 = self.game.players[1]

    def input_max_rounds(self):
        self.game.set_max_rounds(int(input("Rounds:\n")))

    def get_choices(self):
        h_object = input("\nChoice:\n")
        self.player0.choose_object(h_object)
        self.player1.choose_object()

    def run_game(self):
        self.set_up()

        self.get_choices()
        self.game.find_winner()

        print(self.game.report_round())
        print(f"{self.player0.name} {self.player0.score} - {self.player1.score} {self.player1.name}")

    def run_sequence(self):
        ...


if __name__ == "__main__":
    cli = CLInterface()
    cli.run_game()

