"""
- f-strings have been around since python 3.6
- An f-string AKA "formatted string literal" Can be easily recognized by the
  leading 'f' and curly braces containig expressions that will be replaced
  with their values at runtime
"""

import math

class Comedian(object):
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f'{self.first_name} {self.last_name} is {self.age}.'

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is {self.age}. Suprise!'


def main():
    name = 'Nickson'
    age = 32
    print(f'Hello, {name}. You are {age}.')

    # because f-strings are evaluated at runtime, you can put any and all
    # valid python expressions in them
    print(f'{2 * 16}')

    # you can call functions in an f-string
    print(f'{name.lower()} is funny.')
    # you could use objects created from classes with f-strings
    new_comedian = Comedian('Nick', 'Son', 32)
    print(f'{new_comedian}')


if __name__ == '__main__':
    main()
