class MyClass:
    static_var = 10  

MyClass.static_var = 30  

print(MyClass.static_var)  

obj1 = MyClass()
print(obj1.static_var) 

obj2 = MyClass()
print(obj2.static_var)  
