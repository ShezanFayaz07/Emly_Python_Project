# Emly_Python_Project

## Algorithm: Hangman (Single-Player CLI Game)

#### 1)  Start the program.
#### 2)  Create a list of words
            - Example: python, school, laptop, logic.
#### 3)  Select one word randomly from the list and store it as secret_word.
#### 4)  Set total allowed attempts to a fixed number (example: 6).
#### 5)  Create an empty set/list called guessed_letters to store all guessed letters.
#### 6)  Repeat the following steps while attempts > 0:
            - 6.1 Display the current word status
                 For each letter in secret_word:
                 If the letter is in guessed_letters, display the letter.
                 Otherwise, display _ (underscore).

            - 6.2 Display remaining attempts.

            - 6.3 Display letters already guessed.

            - 6.4 Ask the user to enter one letter.

            - 6.5 Convert the input to lowercase.

            - 6.6 Validate the input:
                = If input length is not exactly 1 → show error and go to step 6.
                - If input is not an alphabet (a–z) → show error and go to step 6.
                - If the letter is already in guessed_letters → show warning and go to step 6.

            - 6.7 Add the letter to guessed_letters.

            - 6.8 Check the guess:
                - If the letter exists in secret_word:
                - Display message “Correct guess”.
                - Else:
                    - Reduce attempts by 1.
                    - Display message “Wrong guess”.

            - 6.9 Check win condition:
                - If all letters of secret_word are present in guessed_letters:
                - Display “You won”.
                - Display the secret word.
                - End the loop.
#### 7)  After loop ends:
#### 8)  If attempts become 0:
#### 9)  Display “You lost”.
#### 10)  Display the secret word.
#### 11)  Stop the program.


## ✅ Code (Main Program)

### Inside code, clearly show:

- a) Random Words Array
    - Predefined list of words
    - Random selection logic
- b) Guess Handling
    - Accept one letter
    - Convert to lowercase
    - Validate input
    - Check repeated guesses
- c) Display Function
    - Build _ _ a _ _ output
    - Reveal letters correctly
- d) Game Loop
    - Runs until win or attempts = 0
- e) Win / Lose Logic
    - All letters revealed → win
    - Attempts finished → lose