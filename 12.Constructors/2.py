class Parent:
    def __init__(self, a=None):
        if a is None:
            print("Parent default constructor")
        else:
            print(f"Parent constructor with argument: {a}")

class Child(Parent):
    def __init__(self, a=None, b=None):
        if a is None and b is None:
            super().__init__()  
            print("Child default constructor")
        elif b is None:
            super().__init__(a) 
            print(f"Child constructor with one argument: {a}")
        else:
            super().__init__(a)  
            print(f"Child constructor with two arguments: {a}, {b}")

child1 = Child()          
child2 = Child(10)       
child3 = Child(10, 20)    
