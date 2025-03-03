class Example:
    def show(self, a, b):  
        print(f"First method: {a}, {b}")

    def show(self, x, y):
        print(f"Second method: {x}, {y}")

obj = Example()
obj.show(10, 20)  
