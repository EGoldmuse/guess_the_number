import random

guesses_taken = 0

print("Hello, what is your name?")
myName = input()

number = random.randint(1, 50)
print("Well, " + myName + " I'm thinking of a number between 1 and 50.")

for guesses_taken in range(6):
    if guesses_taken == 0:
        print("Take a guess.")
    else:
        print("Your remaining guesses are at", (6 - guesses_taken))
    guess = input()
    guess = int(guess)

    if guess > number:
        print(f'{guess} is too high')
    elif guess < number:
        print(f'{guess} is too low')
    else:
        break
if guess == number:
    guesses_taken = str(guesses_taken + 1)
    print("Congratulations, you guessed the number was " + str(number) + " in " + str(guesses_taken) + " tries!")
else:
    print('Nope. The number I was thinking of was ' + str(number) + '.')