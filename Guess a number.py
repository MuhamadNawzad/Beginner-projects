import random
command = "Y"
secret_number = random.randint(1, 100)
counter = 1
while command == "Y":
    guess = int(input("Guess:"))
    if guess == secret_number:
        print(f"You won in {counter} times.")
        command = input("Continue? (Y/N)").upper()
        secret_number = random.randint(1, 100)
        counter = 1
    elif guess > secret_number:
        print("Your number is too large")
    elif guess < secret_number:
        print("Your number is too small")
    counter += 1