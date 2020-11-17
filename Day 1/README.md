# Python Review 1

## About 40-50 mins

Create a Python file to implement the following game: 
Ask the user to guess a random number by entering a positive integer from 0-100 (or -1 to quit)
Create a random number between 0 and 100 (e.g. use the following code)
from random import randint
r = randint(0,100)

When the user types in a number tell them if it's too high or too low (e.g. use a while loop)
When they guess correctly, tell them and stop the program

In the game, if the user enters -2, give them a clue:

- Is the number even/odd, a square and/or a prime number
- Use code structures to determine the clues
For example you might:
- Generate a collection of the even numbers from 0-100
- Generate a collection of squares of 0-10
- Copy this code to create a collection of the prime numbers under 100:
primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
- If they type -2, give clues such as 'it is even' etc.

### Optional Ideas

Store each guess by appending it to a list. At the end show the numbers they guessed
Allow the user to choose the number range (and therefore the difficulty)
Give feedback like 'much too small' 'a bit higher', 'close' etc. based on their guess
Suggest a number which would be sensible to guess next, based on their last guess
