from Main_Checked_Functions import *

selected_word = ''
attempts_left = 0
guessed_letters = set()

WordsList = ["apple", "banana", "grapes", "orange", "mango"]

selected_word = ''
User_Guess = ''

Wrong_letters = set()




def gameLoop():     
    global selected_word, guessed_letters, attempts_left, User_Guess, Wrong_letters, WordsList
       
       
    selected_word, guessed_letters, attempts_left = initializeGameState(selected_word, guessed_letters, attempts_left, WordsList)
    displayWordProgress(selected_word, guessed_letters, attempts_left)
    
    
    while not checkLoseCondition(attempts_left) and not checkWinCondition(guessed_letters, selected_word):
        User_Guess = getUserGuess(guessed_letters, Wrong_letters)
        
        guessed_letters, Wrong_letters, attempts_left = processGuess(User_Guess, selected_word, guessed_letters, Wrong_letters, attempts_left)
        displayWordProgress(selected_word, guessed_letters, attempts_left)
        
    showFinalResult(checkWinCondition(guessed_letters, selected_word), selected_word)
    print(f"\033[33mWrong Guess: {Wrong_letters}\n\033[37m")