## 🎮 Number Guessing Game


import random

while True:
    secret_number = random.randint(1, 20)
    chances = 5
    attempts = 0

    while attempts < chances:
        guess = int(input("Enter your guess (1 to 20): "))
        attempts += 1

        if guess == secret_number:
            print(f"🎉 Correct! You guessed it in {attempts} tries.")
            break
        elif guess < secret_number:
            print("Too Low!")
        else:
            print("Too High!")

        print("Tries left:", chances - attempts)

    if guess != secret_number:
        print("❌ Sorry! The number was:", secret_number)

    again = input("Play again? (yes/no): ")
    if again.lower() != "yes":
        print("👋 Goodbye!")
        break
