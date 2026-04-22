import random
from CL_Colors import *

#-----------------------------------------------------------------------------------------------------------------------
def getUserGuess(guessed_letters, Wrong_letters):
        
    while True:
        # guess = input(f"{Magenta}Enter your guess: {White}").strip().lower()
        guess = input(f"{Magenta}Enter your guess (or type 'hint'): {White}").strip().lower()

        if guess == "hint":
            return "hint"
    
        #⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
        #Dev use only:
        if guess == 'mm1':
            exit(0)
        #⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
    
        if validateGuess(guess):        
            if isRepeatedGuess(guess, guessed_letters, Wrong_letters):
                print(f"{Red}⚠️  User guess is repeated{White}")
                continue
            else:
                return guess
        else:
            print(f"{Red}user guess is invalid! Try again{White}")
            continue
#-----------------------------------------------------------------------------------------------------------------------
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#-----------------------------------------------------------------------------------------------------------------------        
def chooseCategory(Wordslist):
    print("Word Categories:\n")
    print("Fruits , Places , Animals , Tech \n")
    while True:
        choice = input("Enter the Category: ").strip().lower()
        if choice in Wordslist:
            return Wordslist[choice]
        else:
            print("Invalid Category , Please try again")

#-----------------------------------------------------------------------------------------------------------------------
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#-----------------------------------------------------------------------------------------------------------------------

def chooseDifficulty(attempts_left):
    print("Difficulty Level:\n")
    print("Easy -> 8 attempts \n")
    print("Medium -> 6 attempts \n")
    print("Hard -> 4 attempts \n")
    while True:
        choice = input("Enter Difficulty :").strip().lower()
        if choice == "easy":
            attempts_left = 8
            return attempts_left
        elif choice == "medium":
            attempts_left = 6
            return attempts_left
        elif choice == "hard":
            attempts_left = 4
            return attempts_left
        else:
            print("Invalid Diificulty Level , Please try again")

#-----------------------------------------------------------------------------------------------------------------------
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#-----------------------------------------------------------------------------------------------------------------------
def initializeGameState(selected_word, guessed_letters, WordsList):
    
    selected_word = getRandomWord(WordsList)
    guessed_letters = set()

    print(f"{Yellow}Game Initialization Done, Random Word Is Selected\n")

    return selected_word, guessed_letters
#-----------------------------------------------------------------------------------------------------------------------
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#-----------------------------------------------------------------------------------------------------------------------
def displayWordProgress(word, guessed_letters, attempts_left):
    drawHangman(attempts_left)
    progress = ""
    for letter in word:
        if letter in guessed_letters:
            progress += " " + letter + " "
        else:
            progress += " x "
    print(f"\033[1;30;47m{progress.strip()}  {Blue}|-=-=-> Attempts Left: {attempts_left}----\033[0m\n")
#-----------------------------------------------------------------------------------------------------------------------
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#-----------------------------------------------------------------------------------------------------------------------    
def processGuess(guess, secret_word, guessed_letters, wrong_letters, attempts_left):
    for letter in secret_word:
        if guess == letter:
            guessed_letters.add(guess)
            print(f"\n{Green}Correct Guess!{White}")
            return guessed_letters, wrong_letters, attempts_left
    wrong_letters.add(guess)
    print(f"\n{Red}⚠️  Wrong Guess!{White}")
    attempts_left -= 1
    return guessed_letters, wrong_letters, attempts_left
#-----------------------------------------------------------------------------------------------------------------------
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#-----------------------------------------------------------------------------------------------------------------------
def validateGuess(guess):
    if len(guess) != 1 or not guess.isalpha():
        return False
    return True
#-----------------------------------------------------------------------------------------------------------------------
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#-----------------------------------------------------------------------------------------------------------------------
def isRepeatedGuess(guess, guessed_letters, Wrong_letters):
    for letter in guessed_letters.union(Wrong_letters):
        if guess == letter:
            return True
    return False
#-----------------------------------------------------------------------------------------------------------------------
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#-----------------------------------------------------------------------------------------------------------------------
def getRandomWord(Words_List):
    word = random.choice(Words_List)
    # print("Random Word Done", word);
    return word
#-----------------------------------------------------------------------------------------------------------------------
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#-----------------------------------------------------------------------------------------------------------------------
def checkLoseCondition(attempts_left):
    if attempts_left == 0:
        return True
    return False
#-----------------------------------------------------------------------------------------------------------------------
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#-----------------------------------------------------------------------------------------------------------------------

def giveHint(secret_word, guessed_letters):
    remaining_letters = []

    for letter in secret_word:
        if letter not in guessed_letters:
            remaining_letters.append(letter)

    if remaining_letters:
        hint_letter = random.choice(remaining_letters)
        guessed_letters.add(hint_letter)

        print(f"{Cyan}💡 Hint used! Revealed letter: {hint_letter}{White}")

    return guessed_letters
#-----------------------------------------------------------------------------------------------------------------------
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#-----------------------------------------------------------------------------------------------------------------------
def drawHangman(attempts_left):

    stages = [
"""
   ------
   |    |
   |    O
   |   /|\\
   |   / \\
   |
=========
""",
"""
   ------
   |    |
   |    O
   |   /|\\
   |   /
   |
=========
""",
"""
   ------
   |    |
   |    O
   |   /|\\
   |
   |
=========
""",
"""
   ------
   |    |
   |    O
   |   /|
   |
   |
=========
""",
"""
   ------
   |    |
   |    O
   |    |
   |
   |
=========
""",
"""
   ------
   |    |
   |    O
   |
   |
   |
=========
""",
"""
   ------
   |    |
   |
   |
   |
   |
=========
"""
]

    index = min(attempts_left, len(stages)-1)
    print(stages[index])

#-----------------------------------------------------------------------------------------------------------------------
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#-----------------------------------------------------------------------------------------------------------------------
def checkWinCondition(guessed_letters, selected_word):
    for letter in selected_word:
        if letter not in guessed_letters:
            return False
    return True
#-----------------------------------------------------------------------------------------------------------------------
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#-----------------------------------------------------------------------------------------------------------------------
def showFinalResult(is_win, word , attempts_left):
    if is_win:
        word_length = len(word)
        score = attempts_left * word_length
        print(f"{Green}🎉 Congratulations! You guessed the word: {word}{White}")
        print(f"{Cyan}Your Score: {score}{White}")
    else:
        print(f"{Red}❌ Game Over! The word was: {word}{White}")

#--------------------------------------------------------------
#--------------------------------------------------------------
#----------ABOVE FUNCTIONS IS CHECKED AND WORKING--------------
#--------------------------------------------------------------
#--------------------------------------------------------------