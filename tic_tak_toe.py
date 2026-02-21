class TicTacToe:
    def __init__(self):
        self.board_game = [" ", " ", " ",
                           " ", " ", " ",
                           " ", " ", " "]
        self.player_1 = "❌"

    def print_board(self):
        print(self.board_game[0], "|", self.board_game[1], "|", self.board_game[2])
        print("--+----+--")
        print(self.board_game[3], "|", self.board_game[4], "|", self.board_game[5])
        print("--+----+--")
        print(self.board_game[6], "|", self.board_game[7], "|", self.board_game[8])

    def move(self, position):
        self.board_game[position - 1] = self.player_1

    def switch_player(self):
        if self.player_1 == "❌":
            self.player_1 = "⭕"
        else:
            self.player_1 = "❌"

    def check_winner(self):
        b = self.board_game
        for i in [0, 3, 6]:
            if b[i] == b[i + 1] == b[i + 2] != " ":
                return True
        for i in [0, 1, 2]:
            if b[i] == b[i + 3] == b[i + 6] != " ":
                return True
        if b[0] == b[4] == b[8] != " ":
            return True
        if b[2] == b[4] == b[6] != " ":
            return True
        return False

    def check_draw(self):
        return " " not in self.board_game

    def start_game(self):
        while True:
            self.print_board()

            while True:
                pos = input(f"🎮 Player {self.player_1}, Please choose a number between 1-9: 🎮")

                if not pos.isdigit():
                    print("❗ Invalid input! Please enter a number from 1 to 9. ❗")
                    continue

                pos = int(pos)

                if not (1 <= pos <= 9):
                    print("❗ Number out of range! Please enter a number from 1 to 9 ❗.")
                    continue

                if self.board_game[pos - 1] != " ":
                    print("🤔 That place is already taken. Try again. 🤔")
                    continue

                break

            self.move(pos)

            if self.check_winner():
                self.print_board()
                print(f"🏆 Player {self.player_1} wins! 🏆")
                break

            if self.check_draw():
                self.print_board()
                print("🤝 It's a draw! 🤝")
                break

            self.switch_player()


        if __name__ == "__main__":
            game = TicTacToe()
            game.start_game()

        input("\nPress Enter to return to the main menu...")
