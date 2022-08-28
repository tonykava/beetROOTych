import random
a = random.randint(1, 10)
your_guess = input('Guess the number from 1 to 10: ')
if a == int(your_guess):
    print('The answer is: ' + str(a))
    print('You guessed right')
else:
    print('The answer is: ' + str(a))
    print('You guessed wrong')




