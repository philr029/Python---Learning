# password_generator.py
# Simple Password Generator - Python Learning

import random
import string

def generate_password(length=12, use_symbols=True):
    characters = string.ascii_letters + string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=" * 45)
    print("       SIMPLE PASSWORD GENERATOR")
    print("=" * 45)
    print()

    while True:
        try:
            length = input("Password length (default 12): ").strip()
            length = int(length) if length else 12

            if length < 4:
                print("Password should be at least 4 characters.\n")
                continue

            symbols = input("Include symbols? (y/n, default y): ").strip().lower()
            use_symbols = symbols != "n"

            password = generate_password(length, use_symbols)

            print("\n" + "-" * 45)
            print(f"Your password:  {password}")
            print("-" * 45)
            print()

            again = input("Generate another? (y/n): ").strip().lower()
            if again != "y":
                print("\nDone. Stay safe!")
                break

            print()

        except ValueError:
            print("Please enter a valid number.\n")

if __name__ == "__main__":
    main()
