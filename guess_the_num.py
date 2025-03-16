#This is Guess the number game
import random

Secret_Number=random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

for Guess_Taken in range (1,6):
    print('Take a guess!')
    guess=int(input())

    if guess>Secret_Number:
        print('The number is too high')
    elif guess<Secret_Number:
        print('Too low')
    else:
        break

if guess==Secret_Number:
    print('You guessed the number in '+str(Guess_Taken)+' guesses.')
else:
    print('Nope, the number I was thinking of is '+str(Secret_Number))


