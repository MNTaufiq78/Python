#10. Write a program to generate ClassNotFoundException 
try:
    from non_existent_module import SomeClass
except ModuleNotFoundError:
    print("Error: Class not found.")
