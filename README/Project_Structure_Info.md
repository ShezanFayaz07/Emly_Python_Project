> [!NOTE]
> 📌 Important Project Note:
>        -   Every step must be implemented as its own function. No spaghetti logic. No giant main() doing everything.
>            This is a pure function-based project.
<br>

> [!IMPORTANT]
> ### 👤👤👤 Contributors:
>    ## 1) Hamaad ---- ![Type 1](https://img.shields.io/static/v1?label=|&message=GITHUB&color=ff&style=plastic&logo=github&logo-color=white)
>    ## 2) Shezan ---- ![Type 1](https://img.shields.io/static/v1?label=|&message=GITHUB&color=ff&style=plastic&logo=github&logo-color=white)
>    ## 3) Mubashir -- ![Type 1](https://img.shields.io/static/v1?label=|&message=GITHUB&color=ff&style=plastic&logo=github&logo-color=white)

<hr><hr><br>

# 🎮 Main Game Flow (Function-Based):

<hr>

#### 🟢 gameLoop() → Person 3 starts
#### 👉 getRandomWord() → Person 1
#### 👉 initializeGameState() → Person 1
#### 🔁 while game is not over → Person 3 controls loop
#### 🙂 displayWordProgress(word, guessedLetters) → Person 3
#### 🙂 displayGameStatus(attempts) → Person 3
#### ⌨️ getUserGuess() → Person 2
#### 🔎 validateGuess(guess) → Person 2
#### 🔁 if invalid → ask again (Person 2)
#### ♻️ isRepeatedGuess(guess, guessedLetters) → Person 2
#### 🔁 if repeated → ask again (Person 2)
#### ⚙️ processGuess(guess, word, guessedLetters, attempts) → Person 2
        - → updates guessedLetters and attempts
#### 🏆 checkWinCondition(word, guessedLetters) → Person 1
        - → if true → showFinalResult(true) → Person 3 → stop
#### 💀 checkLoseCondition(attempts) → Person 1
        - → if true → showFinalResult(false) → Person 3 → stop
#### 🔁 loop continues
#### 🛑 gameLoop() → Person 3 ends

<hr><hr>









# 📌 Project Work Assignment & Development Plan:

<hr><hr>

### 🧠 Step 1: Understand the Assigned Responsibility:
        - •	Carefully understand only the functions assigned to you
        - •	Clearly document:
            - o	What your functions do
            - o	What they accept (inputs)
            - o	What they return (outputs)
        - •	Write this understanding in a text file / Word document
<br>

### 🔄 Step 2: Function Flowcharts:
        - •	Draw a separate flowchart for each assigned function
        - •	Each flowchart must:
            - o	Show start → logic → return/end
            - o	Be independent (no dependency on other functions)
<br>

### 🧾 Step 3: Pseudocode:
        - •	Write pseudocode for each function
        - •	One function = one pseudocode block
        - •	Keep it readable and language-independent
<br>

### 🧩 Step 4: General Game Flowchart:
        - •	After understanding all functions:
            - o	Draw one general flowchart
            - o	Show how all functions interact inside gameLoop()
<br>

### 💻 Step 5: Coding (Individual Files):
        - •	Implement only your assigned functions
        - •	Create your own file:
        - •	AssignedWork_<your_name>.py
        - •	Follow function names exactly as defined
        - •	No extra logic, no unrelated code
<br>

### 🧪 Step 6: Self-Testing:
        - •	Manually test each of your functions
        - •	Use dummy values (hardcoded data)
        - •	Verify logic using print statements
        - •	Fix issues before integration
<br>

### 🔗 Step 7: Integration:
        - •	Combine all individual files into:
        - •	main.py
        - •	Align function calls inside gameLoop()
        - •	Resolve conflicts (variables, returns, flow)
<br>

### ✅ Step 8: Test Cases:
        - •	Run main.py with multiple test cases:
            - o	Correct guesses
            - o	Wrong guesses
            - o	Repeated input
            - o	Win scenario
            - o	Lose scenario
        - •	Record test cases and outcomes clearly
<br>

### 📘 Step 9: Documentation:
        - •	Update README.md with:
            - o	Project overview
            - o	Function list
            - o	File structure
            - o	How to run the project
            - o	Test cases summary
            - o	Team member responsibilities

<hr><hr><hr>

# 👤 Person 1 (Mubashir) – Game Data & Core Logic:
<br><br>

### Scope: Things that decide what the game is.
        - •	Random words array (predefined list)
        - •	Random word selection logic
        - •	Store selected word
        - •	Track attempts left
        - •	Win / lose condition check (all letters revealed OR attempts = 0)

    - 🧠 Owns the brain. Breaks it if careless.
<br>

### Responsibilities:
        - •	getRandomWord()
        - •	initializeGameState()
        - •	checkWinCondition()
        - •	checkLoseCondition()
<br>

### Handles:
        - •	Predefined words array
        - •	Random word selection
        - •	Attempts count
        - •	Win / lose evaluation
<br>

### How to test alone:
        - •	Hardcode a word: "apple"
        - •	Hardcode attempts: 5
<br>

### Manual checks:
        - •	Call getRandomWord() → prints a valid word
        - •	Call checkWinCondition(['a','p','l','e'], "apple") → should return true
        - •	Call checkLoseCondition(0) → should return true

    - 📌 Use print() to verify outputs.

<hr><hr><hr>

# 👤 Person 2 (Shezan) – Input & Guess Handling:
<br><br>

### Scope: Dealing with messy humans typing stuff.
        - •	Accept one letter input
        - •	Convert input to lowercase
        - •	Validate input (single letter, a–z)
        - •	Check repeated guesses
        - •	Update guessed letters list
        - •	Reduce attempts on wrong guess
    - 🧹 Owns cleanup duty. Humans are chaotic.
<br>

### Responsibilities:
        - •	getUserGuess()
        - •	validateGuess()
        - •	isRepeatedGuess()
        - •	processGuess()
<br>

### Handles:
        - •	Single-letter input
        - •	Lowercase conversion
        - •	Validation
        - •	Repeated guess check
        - •	Attempt deduction
<br>

### How to test alone:
        - •	Hardcode guessed letters array: ['a','b']
        - •	Hardcode input guess: 'A'
<br>

### Manual checks:
        - •	validateGuess('A') → valid
        - •	validateGuess('1') → invalid
        - •	isRepeatedGuess('a', ['a','b']) → true
        - •	processGuess('c', "apple", ['a']) → wrong guess, attempts –1
    - 📌 No real input. Pass values directly.

<hr><hr><hr>

# 👤 Person 3 (Hamaad) – Display & Game Loop
<br><br>

### Scope: What the user sees + flow.
        - •	Display _ _ a _ _ style output
        - •	Reveal correct letters in position
        - •	Show attempts left
        - •	Main game loop
        - •	Trigger win/lose messages
        - •	Final result display
    - 🎭 Owns presentation and control flow.
<br>

### Responsibilities:
        - •	displayWordProgress()
        - •	displayGameStatus()
        - •	gameLoop()
        - •	showFinalResult()
<br>

### Handles:
        - •	_ _ a _ _ word build
        - •	Revealing correct letters
        - •	Game loop execution
        - •	Win / lose output
<br>

### How to test alone:
        - •	Hardcode word: "apple"
        - •	Hardcode guessed letters: ['a','e']
        - •	Hardcode attempts: 3
<br>

### Manual checks:
        - •	displayWordProgress("apple", ['a','e']) → a _ _ _ e
        - •	displayGameStatus(3) → shows attempts left
        - •	showFinalResult(true) → win message
    - 📌 Just verify printed output visually.