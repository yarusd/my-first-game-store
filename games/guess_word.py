import random

class Guess_The_Word:
    def __init__(self):
        # קורא את קובץ המילים
        with open("words.txt") as f:
            self.words = [line.strip().upper() for line in f.readlines()]
        
        # מערבב את הרשימה כולה
        random.shuffle(self.words)
        
        # בוחר מילה רנדומלית
        self.secret_word = random.choice(self.words)
        
        print("GUESS THE WORD")
        print("Find the secret word!")
        print("The game will tell you if letters are correct. 🔑")
        print("Type 'HINT' to get a clue.")

    def guess_game(self):
        while True:
            user = input("Guess the word: ").upper()
            
            if user == "EXIT":
                return
            
            if user == self.secret_word:
                print("🎉 You WON! Great job! 🎉")
                break
            
            if user == "HINT":
                print(f"Secret Word is {len(self.secret_word)} letters")
                continue
            
            # בודק כמה תווים נכונים
            total_char = 0
            for char in set(user):
                if char in self.secret_word:
                    total_char += 1
            
            if total_char == 0:
                print("No matching characters")
            elif total_char == 1:
                print("CLOSE! 1 character is correct")
            elif total_char == 2:
                print("CLOSER! 2 characters correct")
            else:
                print("VERY CLOSE! 3+ characters correct")
        
        input("\nPress Enter to return to the main menu...")
