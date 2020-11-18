# Python Review 2

Write a new module called 'review2.py' which asks the user for a 'category' and an 'id'
(remember to use input() for this)

We also need a module that contains a function to ensure these two parameters are in the required form:

- The category may be any one of 'users', 'posts, 'albums' or 'photos'
- The id must be a positive integer in the range 1-8

Write this module and call it 'validation.py'
(You could put this module in the same package as your other utilities)
Inside the module write a function called 'cleanup'
Your cleanup function could receive positional and/or keyword arguments as you see fit
However you choose to pass the arguments, the cleanup function should ensure:

- there is a value for the 'category' as a non-empty string containing one of the permitted categories
- there is a value for the 'id' as an integer in the range 1-8 inclusive
- If category or id is missing, you should provide sensible defaults
- If category or id is not quite right, decide how you could fix it
So for example, if id is a floating point number or a string, try to cast it as an int()

Back in your top-level module (review2.py) import your validation module
Ask the user for category and id values and use the cleanup function to validate the

user-provided data
Print the cleaned-up data members as (for example) a list or a dictionary

## Optional

Force the 'category' text to lower-case text using category.lower()
Write try-except blocks around some of your code

- For example, you could catch exceptions when trying to cast a string to an int
Write other modules to contain functions which will:
- return the mean of a list of numbers
- return how many prime numbers exist in a list of numbers (0-100)
Write docstrings for your functions and decorate them with your 'document_it' function
Consider implementing the sanitize funtionality via decorators
Use if __name__ == '__main__': to write immediate code within each of your modules
(i.e. exercise the modules to check they work as expected)
Make use of the category and id values to atually return data from

<https://jsonplaceholder.com/typicode/>cat/id
