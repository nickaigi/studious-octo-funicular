"""
New features to Python's typing system:
- Literal types
- Typed dictionaries
- Final objects
- Protocols

"""


# Python supports optional type hints: typically as annotations on your code
def double(number: float) -> float:
    """
    Here, we say that 'number' should be a float and the double() function
    should return a float.
    Python treats these annotations as hints, they are not enforced at runtime
    """
    return 2 * number


def main():
    print(double(3.14))
    # double() will also accept a string parameter
    print(double("I'm not a float"))


if __name__ == '__main__':
    main()
