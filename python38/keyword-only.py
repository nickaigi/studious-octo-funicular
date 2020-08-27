"""
- Positional-only arguments complement 'keyword-only' arguments.
  In any version of python 3, you can specify keyword-only arguments by using
  the star '*'
- Any argument after '*' must be specified using a keyword
"""

def to_fahrenheit(*, celsius):
    return 32 + celsius * 9 / 5
