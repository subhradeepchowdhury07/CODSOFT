import random

# Initialize scores
user_score = 0
computer_score = 0

print("===================================")
print("   ROCK PAPER SCISSORS GAME")
print("===================================")

# Game loop
while True:
    print("\nChoose one:")
    print("  rock")
    print("  paper")
    print("  scissors")

    user_choice = input("Enter your choice: ").lower().strip()

    # Check valid input
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please try again.")
        continue

    # Computer choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    print(f"\nYou chose:      {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Game logic
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock"     and computer_choice == "scissors") or
        (user_choice == "paper"    and computer_choice == "rock")     or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    # Display scores
    print("\n--- Score Board ---")
    print(f"You:      {user_score}")
    print(f"Computer: {computer_score}")

    # Play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()
    if play_again != "yes":
        print("\nThanks for playing!")
        print("Final Score:")
        print(f"  You:      {user_score}")
        print(f"  Computer: {computer_score}")
        break
