import random

num = random.randint(1, 100)
guesses = 0

while guesses < 7:
    input_num = int(input("Guess a number between 1 and 100: "))

    if input_num < num:
        print("Too low! Try again.")
    elif input_num > num:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number.")
        break

    guesses += 1

if guesses == 7 and input_num != num:
    print("Sorry, you've used all your guesses.")
    print("The number was:", num)