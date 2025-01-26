secret_number = 7
guess = 0
tries = 0

while tries < 3 and guess!= secret_number:
    guess = int(input("Guess a number between 1 and 10:  "))
    tries = tries + 1

if guess == secret_number:
    print("You Won!")
else:
    print("You Lost!")
