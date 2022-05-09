# this is the guess the number game
import random

print('hello, what is your name')
name = input()

print('well, ' + name + ', I guess the number is between 1 and 20')
secretNumber = random.randint(1, 20)

try:
    for guessesTaken in range(1, 7):
        print('take a guess!')
        guess = int(input())

        if guess < secretNumber:
            print('your guess is too low')
        elif guess > secretNumber:
            print('your guess is too high')
        else:
            print('yes!')
            break  # this condition is for correct guess
except ValueError:
    print('you did not enter a number')

if guess == secretNumber:
    print('good job! ' + name + '! you guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('nope. the number i was thinking of was ' + str(secretNumber))
