class MyClass:
    static_var = 10  

obj1 = MyClass()
obj1.static_var = 20  

print(obj1.static_var)   
print(MyClass.static_var)  

obj2 = MyClass()
print(obj2.static_var)   
