class Example:
    def show(self, a, b=None):  
        if b is None:
            print(f"Method with one parameter: {a}")
        else:
            print(f"Method with two parameters: {a}, {b}")

obj = Example()
obj.show(10)        
obj.show(10, 20)   
