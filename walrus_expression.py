class Walrus(object):
    """
    Assingment Expressions aka Walrus expression :=
    - Assignment expressions allow you to assign and return a value in the same
      expression
    """

    def old_example_one(self):
        """ without the assignment expresssion, we would normally do this """
        walrus = False
        print(walrus)

    def example_one(self):
        """ with assignment expression """
        print(walrus := True)
