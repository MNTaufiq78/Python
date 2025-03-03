#5. Write a program to throw exception with your own message 
def check_number(n):
    if n < 0:
        raise ValueError("Negative numbers are not allowed!")

check_number(-5)
