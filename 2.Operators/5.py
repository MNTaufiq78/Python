def small_large(a,b):
    if a<b:
        print(a," is small number")
        print(b," is large number")
    elif a>b:
        print(a," is large number")
        print(b," is small number")
    else:
        print("Both are equal")

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))        
small_large(a,b)