a, b, c = map(int, input("Enter three numbers: ").split())
largest = a if a > b and a > c else (b if b > c else c)
print("Largest number:", largest)
