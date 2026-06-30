import random

class GameManager():

    def __init__(self):
        # Number guessing game state
        self.secret_number = None
        self.guess_count = 0

    # -----------------------
    # Coin Flip
    # -----------------------
    def flip_coin(self):

        coin = random.choice(["Heads", "Tails"])

        return f"The coin landed on {coin}."

    # -----------------------
    # Dice Roll
    # -----------------------
    def roll_dice(self):

        number = random.randint(1, 6)

        return f"You rolled a {number}."

    # -----------------------
    # Start Guessing Game
    # -----------------------
    def start_guess_game(self):

        self.secret_number = random.randint(1, 100)
        self.guess_count = 0

        return "I have selected a number between 1 and 100. Start guessing!"

    # -----------------------
    # Guess Number
    # -----------------------
    def guess_number(self, guess):

        if self.secret_number is None:

            return "No game is running. Type 'start game' first."

        self.guess_count += 1

        if guess < self.secret_number:

            return "Too low!"

        elif guess > self.secret_number:

            return "Too high!"

        else:

            attempts = self.guess_count

            # reset game
            self.secret_number = None
            self.guess_count = 0

            return f"Congratulations! You guessed correctly in {attempts} attempts."

    # -----------------------
    # End Game
    # -----------------------
    def stop_guess_game(self):

        if self.secret_number is None:

            return "No game is currently running."

        self.secret_number = None
        self.guess_count = 0

        return "Guessing game stopped."