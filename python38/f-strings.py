"""
- f-strings have been around since python 3.6
- An f-string AKA "formatted string literal" Can be easily recognized by the
  leading 'f' and curly braces containig expressions that will be replaced
  with their values at runtime
"""

import math
from datetime import date

class Comedian(object):
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        """
        string returned by __str__() is the informal representation of an object
        and should be readable
        call str() to trigger a call to __str__()
        """
        return f'{self.first_name} {self.last_name} is {self.age}.'

    def __repr__(self):
        """
        string returned by __repr__() is the official representation and should be
        unambiguous
        call repr() to trigger a call to __repr__()
        """
        return f'{self.first_name} {self.last_name} is {self.age}. Suprise!'


def self_documenting_expressions():
    """
    f-strings have an '=' specifier such as f'{expr=}' which expands to the
    text of the expression, an equal sign, then representation of the evaluated
    expression
    """
    user = 'nickson'
    member_since = date(1975, 2, 28)
    print(f'{user=} {member_since=}')

    # f-string format specifiers allow more control over how the result of the
    # expression is displayed
    delta = date.today() - member_since
    print(f'{user=!s} {delta.days=:,d}')


def multiline_fstrings():
    name = 'Nickson'
    profession = 'Developer'
    country = 'Kenya'
    message = (
        f'Hi {name}. '
        f'You are a {profession}. '
        f'You are from {country}. '
    )
    print(message)


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

    # by default f-strings will use __str__()
    # f-strings can make use of __repr__() if you include the conversion flag
    # !r
    print(f'{new_comedian!r}')
    self_documenting_expressions()
    multiline_fstrings()


if __name__ == '__main__':
    main()
