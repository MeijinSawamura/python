#This program allows user 6 chances to guess a random number

import random

secretNo = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

#Ask player to guess 6 times.
for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNo:
        print('Your guess is too low.')
    elif guess > secretNo:
        print('Your guess is too high.')
    else:
        break
    
if guess == secretNo:
    print('Congrats, you guessed the number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Sorry, the number was ' + str(secretNo))
