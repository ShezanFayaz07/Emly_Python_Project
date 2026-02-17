import random

def getUserGuess(guessed_letters, Wrong_letters):
    guess = input("Enter your guess: ").strip().lower()
    
    if validateGuess(guess):
        print("user guess is valid")
        
        if isRepeatedGuess(guess, guessed_letters, Wrong_letters):
            print("user guess is repeated")
            return guess
        else:
            print("user guess is not repeated")
            return guess
    else:
        print("user guess is invalid! Try again")
        return guess
    

        
def initializeGameState(selected_word, attempts_left, guessed_letters, WordsList):
    
    selected_word = getRandomWord(WordsList)
    attempts_left = 5
    guessed_letters = set()

    print(f"Game Initialization Done:\nselected_word = ✅\nattempts_left = {attempts_left}\nguessed_letters = ✅")

    return selected_word, guessed_letters, attempts_left
    

def displayWordProgress(word, guessed_letters, attempts_left):
    progress = ""
    for letter in word:
        if letter in guessed_letters:
            progress += letter + " "
        else:
            progress += "_ "
    print(f"{progress.strip()}  |-=-=-> Attempts Left: {attempts_left}")
    
    
def processGuess(guess, secret_word, guessed_letters, wrong_letters, attempts_left):
    for letter in secret_word:
        if guess == letter:
            guessed_letters.add(guess)
            print("Correct guess!")
            return guessed_letters, wrong_letters, attempts_left
    wrong_letters.add(guess)
    attempts_left -= 1
    # print("Wrong guess!")
    return guessed_letters, wrong_letters, attempts_left



def validateGuess(guess):
    if len(guess) != 1 or not guess.isalpha():
        return False
    return True

def isRepeatedGuess(guess, guessed_letters, Wrong_letters):
    for letter in guessed_letters.union(Wrong_letters):
        if guess == letter:
            return True
    return False

def getRandomWord(Words_List):
    word = random.choice(Words_List)
    # print("Random Word Done", word);
    return word

#--------------------------------------------------------------
#--------------------------------------------------------------
#----------ABOVE IS CHECKED AND WORKING------------------------
#--------------------------------------------------------------
#--------------------------------------------------------------












def checkWinCondition(guessed_letters, selected_word):
    for letter in selected_word:
        if letter not in guessed_letters:
            return False
    return True


def checkLoseCondition(attempts_left):
    if attempts_left == 0:
        return True
    return False


def showFinalResult(is_win, word):
    """
    Displays final game result.
    """
    if is_win:
        print(f"🎉 Congratulations! You guessed the word: {word}")
    else:
        print(f"❌ Game Over! The word was: {word}")


    
    


    
    
    
    
       
    
    
    
        
    
    
    
    
