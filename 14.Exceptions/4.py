#4. Write a program with multiple catch blocks
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numbers only.")
except Exception as e:
    print("Unknown Error:", e)
