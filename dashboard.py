# dashboard.py
# Simple Terminal Dashboard - Python Learning

import os
import time
from datetime import datetime

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_dashboard():
    clear()
    now = datetime.now().strftime("%A, %d %B %Y  |  %H:%M:%S")
    
    print("=" * 50)
    print("          PYTHON LEARNING DASHBOARD")
    print("=" * 50)
    print(f"  {now}")
    print("-" * 50)
    print()
    print("  1. Calculator")
    print("  2. View Progress")
    print("  3. Daily Goal")
    print("  4. Quit")
    print()
    print("-" * 50)

def main():
    while True:
        show_dashboard()
        choice = input("  Select an option (1-4): ").strip()

        if choice == "1":
            print("\n  → Opening calculator...")
            time.sleep(1)
            os.system("python3 calculator.py")   # runs your existing calculator
        elif choice == "2":
            print("\n  Progress so far:")
            print("  • Calculator .............. Done")
            print("  • Dashboard ............... In progress")
            print("  • Next project ............ Coming soon")
            input("\n  Press Enter to go back...")
        elif choice == "3":
            print("\n  Today's goal: Practice Python for 30 minutes")
            input("\n  Press Enter to go back...")
        elif choice == "4" or choice.lower() == "q":
            print("\n  Goodbye! Keep learning.")
            break
        else:
            print("\n  Invalid option. Try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()
