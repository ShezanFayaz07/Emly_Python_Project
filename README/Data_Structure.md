# 📌 DSA used in Hangman (Project-E):


> ## 1️⃣ Array / List
>
> - Used as: words list

> ### Structure:
>  - Linear data structure
>  - Indexed
>  - Stores same-type elements

> ### Why used here:
>  - Store predefined words
>  - Easy random access

> ### How used:
> ```
> words = ["python", "school", "kashmir", "laptop", "logic"]
> ```

Operations

Access: O(1)

Traversal: O(n)

Purpose in project

Computer randomly selects one word

Base data source for the game

2️⃣ String

Used as: secret_word, user input

Structure

Immutable sequence of characters

Why used

Words are character sequences

Easy comparison and iteration

How used

secret_word = "banana"


Operations

Character traversal

Membership check (in)

Length calculation

Purpose

Compare guessed letters

Build display word

3️⃣ Set

Used as: guessed_letters, wrong_letters

Structure

Unordered

No duplicate elements

Hash-based

Why used (VERY IMPORTANT)

Automatically prevents repeated guesses

Fast lookup

How used

guessed_letters = set()
wrong_letters = set()


Operations

Insert: O(1)

Search: O(1)

Purpose

Track guessed letters

Detect repeated guesses instantly

4️⃣ Integer

Used as: attempts_left

Structure

Primitive data type

Why used

Count remaining chances

How used

attempts_left = 6


Operations

Decrement

Comparison

Purpose

Win/Loss decision control

5️⃣ Loop (While Loop)

Used as: Main game loop

Structure

Iterative control structure

Why used

Game continues until win or lose

How used

while attempts_left > 0:


Purpose

Repeated gameplay

Continuous user input handling

6️⃣ Conditional Statements (Decision Making)

Used as: if / elif / else

Why used

Check correct/wrong guesses

Validate input

Win/Lose detection

Purpose

Game logic flow control

7️⃣ Function (Modular Design)

Used as: pick_word(), get_display_word() etc.

Structure

Block of reusable code

Why used

Code reusability

Clean structure

Easy debugging

Purpose

Separate concerns

Improve readability

🧠 DSA Mapping Table (Exam Gold)
DSA Concept	Used For	Why
List	Word storage	Easy random selection
String	Word handling	Character operations
Set	Guess tracking	No duplicates + fast
Integer	Attempts	Count control
Loop	Gameplay	Continuous execution
Condition	Decisions	Logic handling
Function	Modularity	Clean code