import random

choice = ["stone", "paper", "scissors"]

while True:
    print("\n---- GAME START ----")
    print("1. Stone")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    user = input("Enter your choice: ").strip()

    if user == "4":
        print("Thank you for playing")
        break

    if user not in ["1", "2", "3"]:
        print("Invalid Choice")
        continue

    if user == "1":
        user = "stone"
    elif user == "2":
        user = "paper"
    else:
        user = "scissors"

    bot = random.choice(choice)

    print(f"You chose: {user}")
    print(f"Computer chose: {bot}")

    if user == bot:
        print("It's a Draw!")

    elif (user == "scissors" and bot == "paper") or (user == "paper" and bot == "stone") or (user == "stone" and bot == "scissors"):
        print("You win!")

    else:
        print("You lose!")