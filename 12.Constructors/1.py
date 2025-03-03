class MyClass:
    def __init__(self, a=None, b=None):  
        if a is None and b is None:
            print("Default constructor called")
        elif b is None:
            print(f"One-argument constructor called with value: {a}")
        else:
            print(f"Two-argument constructor called with values: {a}, {b}")

obj1 = MyClass()        
obj2 = MyClass(10)     
obj3 = MyClass(10, 20) 
