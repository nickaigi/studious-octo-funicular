def incr(x, /):
    """
    - in python 3.8 you can use '/' to denote that all arguments before it
      must be specified by position.
    """
    return x + 1

def greet(name, /, greeting="Hello"):
    """
    the slash '/' is placed between 'name' and 'greeting' to signify that
    'name' is a positional-only argument while 'greeting' is a regular
    argument that can be passed either by position or keyword
    """
    return f"{greeting}, {name}"

def main():
    pass

if __name__ = '__main__':
    main()
