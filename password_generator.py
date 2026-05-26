import random
import string

print("=== Password Generator ===")
length = int(input("Enter password length: "))

characters = ""

# User choices
if input("Include letters? (y/n): ").lower() == "y":
    characters += string.ascii_letters
if input("Include numbers? (y/n): ").lower() == "y":
    characters += string.digits
if input("Include symbols? (y/n): ").lower() == "y":
    characters += string.punctuation

# Check if no character type selected
if characters == "":
    print("Error: You must select at least one character type.")
else:
    password = ""
    for i in range(length):
        password += random.choice(characters)
    print("\nGenerated Password:")
    print(password)
