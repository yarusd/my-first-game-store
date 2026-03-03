
class Battle_Game:
    def __init__(self):
        self.player_name = ""
        self.start_hp = 140
        self.after_hp=self.start_hp
        self.attack_options = [10, 20, 30, 40, 50]

    def start_game(self):
        print("battle Game!")
        self.player_name = input("Enter your character name: ")
        print(f"\nHey {self.player_name}!")
        print("You have 5 chances to defeat the enemy.")
        print("Your goal: bring the enemy HP exactly to 0!")
        print("Attack options: 10, 20, 30, 40, 50\n")


    def attack_action(self):
        try_count = 5
        while self.after_hp > 0 and try_count > 0:
            attack = int(input("Choose your attack: "))

            if attack not in self.attack_options:
                print("invalid option. choose between 10-50")
                continue
            self.after_hp -= attack
            try_count -= 1

            if self.after_hp > self.start_hp / 2:
                print("GO STRONGER")
            elif self.after_hp == self.start_hp / 2:
                print("You're halfway there")
            elif 0 < self.after_hp < 50:
                print("BE CAREFUL")

        if self.after_hp == 0:
            print("🎉 CHAMPION! 🎉 ENEMY IS DEAD 🎉")

        elif self.after_hp < 0:
            print(" OH NO❌! You overkilled the rival❌")

        else:
            print("😔 YOU LOST! ENEMY SURVIVED 😔")

        input("\nPress Enter to return to the main menu...")












