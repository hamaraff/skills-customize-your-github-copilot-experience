
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a command-line Hangman game in Python that reinforces string manipulation, control flow, and user input handling.

## 📝 Tasks

### 🛠️ Implement the Game

#### Description
Create a Hangman game where the program selects a secret word and the player guesses letters until they either reveal the word or run out of attempts.

#### Requirements
Completed program should:

- Randomly select a secret word from a predefined list (see `starter-code.py`).
- Accept single-letter guesses and display the current word progress in a spaced format (e.g. `_ a _ _ m a n`).
- Track and display incorrect guesses and remaining attempts.
- Ignore repeated guesses (do not double-penalize the player).
- End the game with a clear win or lose message and reveal the secret word when the game ends.
- Include clear function decomposition and docstrings for main functions (e.g., `choose_word()`, `display_progress()`, `process_guess()`).

## 🚀 How to run

Run the assignment from the assignment folder using the system Python interpreter:

```bash
python starter-code.py
```

If your system uses `python3` as the command, use:

```bash
python3 starter-code.py
```

## 📂 Files

- `starter-code.py` — starter code and word list to get you started.

## ✅ Submission

- Submit the completed `starter-code.py` (or a new `hangman.py`) with your implementation.
- Ensure your code is well-formatted, includes comments, and passes basic manual tests (plays correctly for several words).

## ✨ Extensions (optional)

- Add difficulty levels that adjust allowed attempts.
- Load words from an external file (e.g., `words.txt`).
- Add a hint system or scoring.

## 🎓 Learning Outcomes

- Practice working with strings, lists, and control flow.
- Design simple interactive applications and decompose logic into functions.
- Improve debugging and user input validation skills.
