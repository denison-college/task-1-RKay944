import random
import utility
import game_screen 

rules = """
1. Select a difficulty from easy(4-5), medium(6-8) or hard(8+)
2. try to guess the word letter by letter
3. wrong guesses will add to the hangman, if completed, you lose
"""

def play_with_word(word):
    points = 6
    number = 0
    chosen = []
    while points != number:
        utility.clear_screen()
        underscore = []
        for unit in word:
            if unit in chosen:
                underscore.append(unit)
            else:
                underscore.append("_")
        print(underscore)
        print(word)
        print(game_screen.start_screen)
        letter = input('Pick a letter: ')
        if letter in word:
            chosen.append(letter)
        else:
            points = points-1
    else:
        utility.clear_screen
        print(game_screen.end_screen)

def game():
    print("Hangman")
    print(rules)
    difficulty = ""
    while difficulty == "":
        difficulty = input("Select difficulty: ")
        if difficulty.lower() in ["easy", "medium", "hard"]:
            with open("3. Code and Tests/"+difficulty.lower()+".txt", "r") as f:
                words = f.read().splitlines()
                numder = random.randrange(0,len(words)-1)
                word = words[numder]
                word = word.lower()
            play_with_word(word)
        else:
            difficulty = ""

if __name__ == "__main__":
    game()