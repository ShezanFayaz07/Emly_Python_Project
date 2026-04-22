from Main_Checked_Functions import *

selected_word = ''
attempts_left = 0
guessed_letters = set()

WordsList = {
    "fruits" : ["apple", "banana", "grapes", "orange", "mango"],
    "animals" : ["tiger", "elephant", "lion", "leapord", "cheetah"],
    "places" : ["london", "dubai", "kuwait", "karachi", "lahore"],
    "tech" : ["computer", "science", "internet", "server", "python"]
}

selected_word = ''
User_Guess = ''

Wrong_letters = set()

def gameLoop():     
    global selected_word, guessed_letters, attempts_left, User_Guess, Wrong_letters, WordsList
    hint_used = False
       
    choosen_WordsList = chooseCategory(WordsList)
    attempts_left = chooseDifficulty(attempts_left)

    selected_word, guessed_letters= initializeGameState(selected_word, guessed_letters, choosen_WordsList)
    displayWordProgress(selected_word, guessed_letters, attempts_left)
    
    
    while not checkLoseCondition(attempts_left) and not checkWinCondition(guessed_letters, selected_word):
        User_Guess = getUserGuess(guessed_letters, Wrong_letters)
        
        if User_Guess == "hint":
            if not hint_used:
                guessed_letters = giveHint(selected_word, guessed_letters)
                hint_used = True
            else:
                print(f"{Red}⚠️ Hint already used!{White}")

            displayWordProgress(selected_word, guessed_letters, attempts_left)
            continue

        guessed_letters, Wrong_letters, attempts_left = processGuess(User_Guess, selected_word, guessed_letters, Wrong_letters, attempts_left)
        displayWordProgress(selected_word, guessed_letters, attempts_left)
        
    showFinalResult(checkWinCondition(guessed_letters, selected_word), selected_word, attempts_left)
    print(f"\033[33mWrong Guess: {Wrong_letters}\n\033[37m")