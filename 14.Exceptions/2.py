#2. Handle the Arithmetic exception using try-catch block 
try:
    a = 10
    b = 0
    result = a / b
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
