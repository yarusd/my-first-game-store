
class Guess_The_Word:
    def __init__(self):
        self.secret_word= "SONG"
        print("GUESS THE WORD")
        print("Find the secret word!")
        print("The game will tell you if letters are correct. 🔑")
        print("Type 'HINT' to get a clue.")

    def guess_game(self):
        while(1):
         user=input("Guess the word: ").upper()
         if user=="EXIT":
             return
         if user==self.secret_word:
            print("🎉 You WON! great job! 🎉")
            break
         if user=="HINT".upper():
             print(f"Secret Word is {len(self.secret_word)} letters")
             continue
         else:
           total_char = 0
           for char in set(user):
            if char in self.secret_word:
                 total_char+=1
         if total_char == 1:
             print("CLOSE! 1 character is correct")
         elif total_char == 2:
             print("CLOSER! 2 characters correct")
         elif total_char >= 3:
             print("VERY CLOSE! 3+ characters correct")

        input("\nPress Enter to return to the main menu...")




