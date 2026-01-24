🔍 Dry Run (Example):

Initial State:

Secret word: banana
Attempts left: 6
Guessed letters: { }
Display: _ _ _ _ _ _
----------------------------------------------------------------
Turn 1:

Input: a

Valid input? Yes
Already guessed? No
a is in word → Correct

Display: _ a _ a _ a
Attempts left: 6

Guessed letters: {a}
----------------------------------------------------------------
Turn 2:

Input: z

Valid input? Yes
Already guessed? No
z not in word → Wrong

Display: _ a _ a _ a
Attempts left: 5

Guessed letters: {a, z}
----------------------------------------------------------------
Turn 3:

Input: a

Already guessed? Yes
Message shown: “Already guessed that letter”
Attempts left: 5 (unchanged)
----------------------------------------------------------------
Turn 4:

Input: 1

Valid input? No
Message shown: “Invalid input”
Attempts left: 5 (unchanged)
----------------------------------------------------------------
Turn 5:

Input: b

Correct guess

Display: b a _ a _ a
Attempts left: 5
----------------------------------------------------------------
Turn 6:

Input: n

Correct guess

Display: b a n a n a
----------------------------------------------------------------


Win Check:
All letters revealed? Yes

Output:
“You won! The word was: banana”

🏁 Final Result:

Game ends with win
Attempts remaining: 5