#7. Write a program with finally block 
try:
    print("Inside try block")
    result = 10 / 0
except ZeroDivisionError:
    print("Exception caught: Division by zero")
finally:
    print("Finally block executed")
