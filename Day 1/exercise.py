import random

random_number = random.randint(0,100)

is_even = random_number % 2 == 0

primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
is_prime = primes.count(random_number) == 1

squares = tuple(number * number for number in range(1,11))
#for r in range(1,11):
#    squares.append(r * r)

is_square = squares.count(random_number) == 1

guesses = 0

print(random_number)

user_input = int(input('Guess a number between 0-100 '))

while user_input != random_number:
    if user_input == - 2:
        print(f'Clues --> Even: {is_even}, Prime: {is_square}, Square: {is_square}')
        user_input = int(input('Guess again '))
    elif user_input == -1:
        print(f'The number was {random_number}')
        break
    elif user_input > random_number:
        user_input = int(input('Guess lower '))
        guesses += 1
    elif user_input < random_number:
        user_input = int(input('Guess higher '))
        guesses += 1
 
if (user_input == random_number):
        print(f'Well done! You guessed the number! It took {guesses} attempt(s).')
