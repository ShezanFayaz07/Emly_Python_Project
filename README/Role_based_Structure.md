## 🧠 Data Structures Usage (Person-wise Breakdown)

### 👤 Person 1 (Mubashir) – Game Data & Core Logic

| Data Structure | Used In | Used For | How It Is Used |
|---------------|--------|----------|----------------|
| List | getRandomWord() | Store predefined words | Randomly selects one word from list |
| String | secret_word | Store selected word | Used for comparisons and win checking |
| Integer | attempts_left | Track remaining attempts | Decremented on wrong guesses |
| Set / List | guessed_letters | Track guessed characters | Checked to verify win condition |
| Boolean | checkWinCondition() | Win status | Returns True if all letters revealed |
| Boolean | checkLoseCondition() | Lose status | Returns True if attempts = 0 |

---

### 👤 Person 2 (Shezan) – Input & Guess Handling

| Data Structure | Used In | Used For | How It Is Used |
|---------------|--------|----------|----------------|
| String | getUserGuess() | Store user input | Converted to lowercase |
| Set | guessed_letters | Prevent repeated guesses | Fast membership check |
| Set | wrong_letters | Track incorrect guesses | Helps manage attempts |
| Integer | attempts_left | Reduce attempts | Decremented on wrong input |
| Boolean | validateGuess() | Input validation | Ensures single alphabet input |
| Boolean | isRepeatedGuess() | Duplicate detection | Prevents attempt reduction |

---

### 👤 Person 3 (Hamaad) – Display & Game Loop

| Data Structure | Used In | Used For | How It Is Used |
|---------------|--------|----------|----------------|
| String | displayWordProgress() | Word display | Reveals guessed letters, hides others |
| List | display build | Character-wise display | Builds `_ _ a _ _` format |
| Integer | attempts_left | Status display | Shows remaining attempts |
| While Loop | gameLoop() | Game control | Runs until win or lose |
| Boolean | game state | Loop control | Stops loop on win/lose |
| String | showFinalResult() | Final output | Displays win or lose message |

---

## 📌 Summary

- **Lists** → word storage & display building  
- **Sets** → fast lookup, no duplicate guesses  
- **Strings** → word handling & input  
- **Integers** → attempts & scoring logic  
- **Booleans** → win/lose control  
- **Loops & Conditions** → game flow
