🎮 Hangman Game – Display & Game Loop Module (Person 3)

📌 Overview

This module is my contribution to the team-based Python Hangman game project.
My responsibility (as Person 3) was to implement the game loop, word display logic, and final result handling, while integrating with shared core functions written by teammates.

This file handles:

● Displaying the word progress (_ _ a _ _)

● Tracking remaining attempts

● Running the main game loop

● Showing win/lose results

● Coordinating user guesses with the core game logic

The core logic functions are imported from Main_Checked_Functions.py, which is maintained by the team.

🧠 Features Implemented

✅ 1. Word Progress Display

Shows guessed letters and hides unknown ones using _.

Example output:

_ _ a _ _ | ===> Attempts Left: 5

Implemented in:

displayWordProgress(word, guessed_letters, attempts_left)

✅ 2. Game Loop Controller

Controls the flow of the game:

● Initializes the game state

● Repeatedly asks the user for input

● Processes guesses

● Updates attempts and progress

● Stops when the user wins or loses

Implemented in:

gameLoop()

✅ 3. Win / Lose Condition Check

Checks if:

● The user has guessed all letters (Win)

● The user has no attempts left (Lose)

Implemented in:

checkWinCondition(guessed_letters, selected_word)
checkLoseCondition(attempts_left)

✅ 4. Final Result Display

Displays colored win/lose messages using ANSI color codes:

● 🎉 Win → Green

● ❌ Lose → Red

Implemented in:

showFinalResult(is_win, word)

📁 File Structure

Emly_Python_Project/
│
├── Main_Checked_Functions.py      # Core logic (teammates)
│
├── Contributors/
│   └── Hamaad/
│       ├── Hamaad_Code.py         # My implementation (this file)
│       └── Hamaad.md              # This README

🔗 Dependencies (Team Integration)

This file depends on functions defined in:

from Main_Checked_Functions import *

Which provides:

● initializeGameState()

● getUserGuess()

● processGuess()

● Color constants like Green, Red, White

This design keeps:

● Core logic → centralized

● UI & game flow → modular and maintainable

▶️ How to Run

From the project root directory:

python Contributors/Hamaad/Hamaad_Code.py

Make sure:

● Main_Checked_Functions.py exists in the project root

● Python is installed

● You are running the command from the root folder of the repo

🧪 Sample Game Flow

_ _ _ _ _ | ===> Attempts Left: 5
Enter your guess: a
{'a'} set() 5
_ a _ _ _ | ===> Attempts Left: 5
Enter your guess: z
{'a'} {'z'} 4
_ a _ _ _ | ===> Attempts Left: 4
...

🛠 Tech Stack

● Language: Python 3

● Concepts Used:

○ Functions

○ Loops

○ Sets

○ Modular programming

○ Team-based code integration

● Tools: Git, GitHub, VS Code

🤝 Contribution

Contributor: Hamaad (Person 3)
Responsibility:

● Game loop

● Display logic

● Win/Lose conditions

● Output formatting

● Integration with core logic module

📈 Future Improvements

● Add difficulty levels (easy/medium/hard)

● Add hint system

● Improve UI with ASCII art

● Add multiplayer mode

● Add replay option

⭐ Resume Note

This module demonstrates:

● Collaborative development

● Clean separation of concerns

● Ability to integrate code written by teammates

● Handling merge conflicts and Git workflows

● Writing modular and testable Python code
