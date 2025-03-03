class Example:
    def show(self, a, b=None): 
        if b is None:
            print(f"Method with one parameter: {a} (Type: {type(a).__name__})")
        else:
            print(f"Method with two parameters: {a} (Type: {type(a).__name__}), {b} (Type: {type(b).__name__})")

obj = Example()
obj.show(10)         
obj.show("Hello")    
obj.show(10, "Hi")  
