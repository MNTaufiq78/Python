class Parent:
    def __init__(self):
        self.__private_var = "This is a private variable"
    def __private_method(self):
        print("This is a private method")
    def access_private(self):
        print(self.__private_var)  
        self.__private_method()   

def main():
    obj = Parent()
    obj.access_private()  
    print(obj._Parent__private_var)
    obj._Parent__private_method()

class Child(Parent):
    def try_access_private(self):
        print("Cannot access private members from subclass")
main()
