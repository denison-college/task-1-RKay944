easy = ['flow', 'jazz']
medium = ['flight, altitude']
hard = ['canibalism', 'psychidelic']
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
    if difficulty.lower() == "easy":
        print(game_screen)
        letter = input('Pick a letter: ')
    elif difficulty.lower() == "medium":
        print(game_screen)
        letter = input('Pick a letter: ')
    elif difficulty.lower() == "hard":
        print(game_screen)
        letter = input('Pick a letter: ')
    else:
        difficulty = ""