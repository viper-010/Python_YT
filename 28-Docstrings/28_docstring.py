'''This is a module for demonstrating docstrings.'''

def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)

square(5)
print(square.__doc__)

#A module docstring must be a string literal placed as the very first statement in the file, before any imports or code.
print(__doc__)

