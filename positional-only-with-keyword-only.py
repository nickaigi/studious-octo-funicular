"""
You can comibne position-only, regular, and keyword-only arguments by
specifying them in this order separated by / and *
"""

def headline(text, /, border="♦", *, width=50):
    """
    - 'text' is a positional-only argument
    - 'border' is a regular argument with a default value
    - 'width' is a keyword-only argument with a default value
    """
    return f" {text} ".center(width, border)


def main():
    # 'text' is a positional-only arg, you can't use the keyword 'text'
    print('in main')
    print(headline("Positional-only Arguments"))

    # 'border' can be specified both with and without the keyword
    print(headline("Python 3.8", "="))
    print(headline("Real Python", border=":"))

    # 'width' must be specified using the keyword
    print(headline("Python", "🐍", width=38))

if __name__ == '__main__':
    main()
