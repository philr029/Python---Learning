# guess.py
# Number Guessing Game - Python Learning

import random

def play():
    print("=" * 45)
    print("       NUMBER GUESSING GAME")
    print("=" * 45)
    print()
    print("I'm thinking of a number between 1 and 100.")
    print("Type 'q' to quit.\n")

    secret = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Your guess: ").strip()
        if guess.lower() in ("q", "quit", "exit"):
            print("\nMaybe next time!")
            return

        try:
            number = int(guess)
        except ValueError:
            print("Please enter a number.\n")
            continue

        attempts += 1

        if number < secret:
            print("Too low.\n")
        elif number > secret:
            print("Too high.\n")
        else:
            print(f"\nGot it in {attempts} tries!")
            return

def main():
    while True:
        play()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("\nGoodbye!")
            break
        print()

if __name__ == "__main__":
    main()
