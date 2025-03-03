#6. Write a program to create your own exception
class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message

raise MyCustomException("This is a custom exception")
