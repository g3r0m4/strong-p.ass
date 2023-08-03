import random
import string

# Function to generate random password
def generate_random_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = random.sample(characters, length)
    return "".join(password)

if __name__ == "__main__":
    print("  _______   _______     _______.")
    print(" /  _____| /  _____|   /       |")
    print("|  |  __  |  |  __    |   (----`")
    print("|  | |_ | |  | |_ |    \   \    ")
    print("|  |__| | |  |__| | .----)   |   ")
    print(" \______|  \______| |_______/    ")
    print()

    print("--created by jerome")

    try:
        num_passwords = int(input("How many passwords do you want to generate? "))
        password_length = int(input("Enter the length of each password: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        exit()

    print("\nGenerated passwords:")
    for _ in range(num_passwords):
        password = generate_random_password(password_length)
        print(password)