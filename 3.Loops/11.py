def check_even_odd(n):
    match n % 2:
        case 0:
            print("Even")
        case 1:
            print("Odd")

num = int(input("Enter a number: "))
check_even_odd(num)
