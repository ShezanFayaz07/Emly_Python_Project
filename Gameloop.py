from TestMain import *

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
    
    
    while checkLoseCondition(attempts_left) != True:
        User_Guess = getUserGuess(guessed_letters, Wrong_letters)
        
        guessed_letters, Wrong_letters, attempts_left = processGuess(User_Guess, selected_word, guessed_letters, Wrong_letters, attempts_left)
        print(guessed_letters, Wrong_letters, attempts_left)
        
        displayWordProgress(selected_word, guessed_letters, attempts_left)
            
            
    
    # Issue Program not stoping if word letters are guessed all correct it stops only when attempts reach to 0
    
    
    
gameLoop()
    
    

