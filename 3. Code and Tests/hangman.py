import random
import utility
game_screen = """
_______
|     |
|     O
|    /|\ 
|     |
|\   / \ 
|_\__

"""
rules = """
1. Select a difficulty from easy(4-5), medium(6-8) or hard(8+)
2. try to guess the word letter by letter
3. wrong guesses will add to the hangman, if completed, you lose
"""

print("Hangman")
print(rules)
difficulty = ""
while difficulty == "":
    difficulty = input("Select difficulty: ")
    with open("3. Code and Tests/"+difficulty.lower()+".txt", "r") as f:
        words = f.read().splitlines()
        numder = random.randrange(0,len(words)-1)
        word = words[numder]
    if difficulty.lower() == "easy":
        utility.clear_screen()
        for letters in list(word):
            print("_", end="")
        print(game_screen)
        letter = input('Pick a letter: ')
    elif difficulty.lower() == "medium":
        utility.clear_screen()
        for letters in list(word):
            print("_", end="")
        print(word)
        print(game_screen)
        letter = input('Pick a letter: ')
    elif difficulty.lower() == "hard":
        utility.clear_screen()
        for letters in list(word):
            print("_", end="")
        print(word)
        print(game_screen)
        letter = input('Pick a letter: ')
    else:
        difficulty = ""