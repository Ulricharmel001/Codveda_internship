"""
Number Guessing Game
--------------------
Description:
This program generates a random number between 1 and 100.
The user must guess the number. The program provides feedback
("Too high" or "Too low") after each guess and allows up to
20 attempts per round.

It uses Object-Oriented Programming (OOP) to structure the logic
in a clean and reusable way. After each game, a new random number
is generated, allowing the user to play multiple rounds.
"""

import random


class NumberGuessingGame:
    MAX_ATTEMPTS = 20  

    def __init__(self):
        """Initialize the game with a random number and reset attempts."""
        self.reset_game()

    def reset_game(self):
        """Generate a new random number and reset attempts."""
        self.target_number = random.randint(1, 100)
        self.attempts = 0

    def play(self):
        """Main game loop."""
        print("Welcome to the Number Guessing Game")
        print("I have chosen a number between 1 and 100.")
        print(f"You have {self.MAX_ATTEMPTS} attempts to guess it.\n")

        while True:
            while self.attempts < self.MAX_ATTEMPTS:
                try:
                    guess = input("Enter your guess (or type 'exit' to quit): ")

                    if guess.lower() == 'exit':
                        print("Exiting the game. Goodbye.")
                        return 

                    guess = int(guess)
                    self.attempts += 1

                    if guess < self.target_number:
                        print("Too low.\n")
                    elif guess > self.target_number:
                        print("Too high.\n")
                    else:
                        print(f"Congratulations. You guessed the number {self.target_number} "
                              f"correctly in {self.attempts} attempts.\n")
                        break  

                    if self.attempts == self.MAX_ATTEMPTS:
                        print(f"Game over. The correct number was {self.target_number}.\n")

                except ValueError:
                    print("Invalid input. Please enter a number.\n")

            play_again = input("Would you like to play again? (yes/no): ").lower()
            if play_again == "yes":
                self.reset_game()
                print("\n--- New Game Started ---\n")
            else:
                print("Thank you for playing. Goodbye.")
                break


# --- Main program execution ---
if __name__ == "__main__":
    game = NumberGuessingGame()
    game.play()
