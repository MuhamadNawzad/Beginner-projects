import random

command = "Y"
start = 0
end = 100
counter = 1
print("Guess a number between 1 and 100")
while command == "Y":
    number = random.randint(start, end)
    print(number)
    answer = input("is it, too large (L), too small (S), correct (C)?").upper()
    if answer == "L":
        end = number
    elif answer == "S":
        start = number
    else:
        print("You won in " + str(counter) + " times")
        command = input("Continue (Y/N)?").upper()
        start = 0
        end = 100
        counter = 1
    counter += 1

