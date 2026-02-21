

from game_Project.battle_game import Battle_Game
from game_Project.guess_word import Guess_The_Word
from game_Project.rock_scissors_paper import RockPaperScissors
from game_Project.tic_tak_toe import TicTacToe


while True:
    print()
    print("ARE YOU READY TO PLAY?")
    print("We have a variety of games.")
    print("===========================")
    print("1) Guess The Word 🧐")
    print("2) Battle Game ⚔️")
    print("3) Rock, Scissors and Paper ✂️️")
    print("4) Tick Tack Toe ⭕")
    print("Type EXIT to quit")
    print()

    choose_game = input("Choose your number or type EXIT: ").upper()

    if choose_game == "EXIT".upper():
        print("Goodbye!")
        break

    if choose_game == "1":
            game1 = Guess_The_Word()
            game1.guess_game()
    elif choose_game == "2":
            game2 = Battle_Game()
            game2.start_game()
            game2.attack_action()
    elif choose_game== "3":
            game3 = RockPaperScissors()
            game3.play_game()
    elif choose_game == "4":
            game4 = TicTacToe()
            game4.start_game()


    print("\nReturning to main menu...\n")
