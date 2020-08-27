"""
- f-strings have been around since python 3.6
- An f-string AKA "formatted string literal" Can be easily recognized by the
  leading 'f' and curly braces containig expressions that will be replaced
  with their values at runtime
"""

def to_lower(text):
    return text.lower()


def main():
    name = 'Nickson'
    age = 32
    print(f'Hello, {name}. You are {age}.')

    # because f-strings are evaluated at runtime, you can put any and all
    # valid python expressions in them
    print(f'{2 * 16}')

    # you can call functions in an f-string


if __name__ == '__main__':
    main()
