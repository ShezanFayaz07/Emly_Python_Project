import random

words = ["apple", "banana", "grapes", "orange", "mango"]


def getRandomWord():
    word = random.choice(words)
    # print("Random Word Selected:", word)   
    return word


def initializeGameState():
    selected_word = getRandomWord()
    attempts_left = 5
    guessed_letters = []

    # print("\nGame Initialized")
    # print("Word:", selected_word)
    # print("Attempts Left:", attempts_left)

    return selected_word, attempts_left, guessed_letters


def checkWinCondition(guessed_letters, selected_word):
    for letter in selected_word:
        if letter not in guessed_letters:
            return False
    return True


def checkLoseCondition(attempts_left):
    if attempts_left == 0:
        return True
    return False



if __name__ == "__main__":

    # Initialize
    selected_word, attempts_left, guessed_letters = initializeGameState()

    # Win Test
    win_test = checkWinCondition(['a','p','l','e'], "apple")
    print("Win Condition Test:", win_test)   # Expected → True

    # Lose Test
    lose_test = checkLoseCondition(0)
    print("Lose Condition Test:", lose_test) # Expected → True
