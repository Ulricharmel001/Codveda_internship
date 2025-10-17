# Number Guessing Game

## Description
This is a simple **Number Guessing Game** built using **Object-Oriented Programming (OOP)** in Python.

The program randomly generates a number between 1 and 100, and the user has to guess it.  
After each guess, the program provides feedback:
- "Too high" if the guess is greater than the target number.
- "Too low" if the guess is less than the target number.

Each game allows a maximum of 20 attempts.  
If the user guesses correctly or runs out of attempts, they can choose to play again or exit.

---

## Features
- Built using OOP principles for clean and modular code.
- Automatically regenerates a new random number after each game.
- Provides feedback after every guess.
- Handles invalid input gracefully.
- Allows the user to exit anytime by typing `exit`.

---

## How to Run

1. Ensure you have Python 3 installed on your computer.
2. Save the project files in a folder named `number_guessing_game/`.
3. Open your terminal or command prompt in that folder.
4. Run the program using the command:

   ```bash
   python number_guessing_game.py





Welcome to the Number Guessing Game
I have chosen a number between 1 and 100.
You have 20 attempts to guess it.

Enter your guess (or type 'exit' to quit): 50
Too low.

Enter your guess (or type 'exit' to quit): 75
Too high.

Enter your guess (or type 'exit' to quit): 63
Congratulations. You guessed the number 63 correctly in 3 attempts.

Would you like to play again? (yes/no): yes

--- New Game Started ---

Enter your guess (or type 'exit' to quit): 45
Too high.
