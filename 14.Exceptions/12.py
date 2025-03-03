#12. Write a program to generate NoSuchFieldException
try:
    class MyClass:
        def __init__(self):
            self.name = "Python"
    obj = MyClass()
    print(obj.age)
except AttributeError as e:
    print("NoSuchFieldException occured:", e)
 
