class Parent:
    def __init__(self):
        self._protected_var = "This is a protected variable"
    def _protected_method(self):
        print("This is a protected method")

class Child(Parent):
    def access_protected(self):
        print(self._protected_var)  
        self._protected_method()   

class AnotherClass:
    def access_protected(self):
        obj = Parent()
        print(obj._protected_var)  
        obj._protected_method()   

def main():
    print("\nAccessing from Child class:")
    child_obj = Child()
    child_obj.access_protected()
    print("\nAccessing from AnotherClass:")
    another_obj = AnotherClass()
    another_obj.access_protected()
    
main()
