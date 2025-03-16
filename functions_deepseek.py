import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy, try again'
    else:
        return 'Ask again later'

# Allow user to input a number
user_input = input('Enter a number between 1 and 5: ')
try:
    answerNumber = int(user_input)
    if 1 <= answerNumber <= 5:
        print(getAnswer(answerNumber))
    else:
        print('Please enter a number between 1 and 5.')
except ValueError:
    print('Invalid input. Please enter a valid number.')