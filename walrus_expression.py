class Walrus(object):
    """
    Assingment Expressions aka Walrus expression :=
    - Assignment expressions allow you to assign and return a value in the same
      expression

    - most convenient when using 'while' loops where you need to initialize and
      update a variable
    """

    def old_example_one(self):
        """ without the assignment expresssion, we would normally do this """
        walrus = False
        print(walrus)

    def example_one(self):
        """ with assignment expression """
        print(walrus := True)

    def old_example_two_with_repetition(self):
        inputs = list()
        current = input("Write something: ")
        while current != "quit":
            inputs.append(current)
            current = input("Write something: ")

    def old_example_two_dry(self):
        """ DRY - Don't Repeat Yourself """
        inputs = list()
        while True:
            current = input("Write somethings: ")
            if current == "quit":
                break
            inputs.append(current)

    def example_two(self):
        """
        avoids repetition, is logical
        """
        inputs = list()
        while (current := input("Write something: ")) != "quit":
            inputs.append(current)
