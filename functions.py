def hello():
    print('hello!')
    print('howdy!!')
    print('hello, there!')

hello()

def hello(name):
    print('welcome '+name)

hello('Sobur')
hello('Ibrahim')

import random

def getAnswer(answerNumber):
    

    if answerNumber == 1:
        return 'It is certain'

    elif answerNumber ==2:
        return 'It is decidedly so'

    elif answerNumber == 3:
        return 'Yes'

    elif answerNumber == 4:
        return 'Reply hazy, try again'

    else:
        return 'Ask again later'

r=random.randint(1,5)

print(getAnswer(r))
    

    