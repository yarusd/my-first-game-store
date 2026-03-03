import random

class RockPaperScissors:
    def __init__(self):
        self.options = ["Rock", "Paper", "Scissors"]
        self.user_score = 0
        self.computer_score = 0
        self.rounds = 5

    def get_user_choice(self):
        while True:
            choice = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()
            if choice in self.options:
                return choice
            print(f"{choice} is not a valid choice. Please select from {self.options}.")

    def play_round(self, round_num):
        print(f"\n--- Round {round_num} ---")
        user_choice = self.get_user_choice()
        computer_choice = random.choice(self.options)
        print(f"Computer choice is: {computer_choice}")

        if user_choice == computer_choice:
            print("😶 It's a tie! 😶")
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            print("🏆 Congrats, you win this round! 🏆")
            self.user_score += 1
        else:
            print("😎 The computer wins this round! 😎")
            self.computer_score += 1

    def show_result(self):
        print("\n--- Game Over ---")
        print(f"Your score: {self.user_score}")
        print(f"Computer score: {self.computer_score}")

        if self.user_score > self.computer_score:
            print("🎉 Congratulations! You are the overall winner! 🏆")
        elif self.user_score < self.computer_score:
            print("💻 The computer wins the game! 💻")
        else:
            print("🤝 It's a draw overall!")

        input("\nPress Enter to return to the main menu...")

    def play_game(self):
        print("🔥 Welcome to Rock, Paper, Scissors! 🔥")
        for round_num in range(1, self.rounds + 1):
            self.play_round(round_num)
        self.show_result()
