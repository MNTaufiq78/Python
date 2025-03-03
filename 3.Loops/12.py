gender = input("Enter M/F: ").upper()
match gender:
    case "M":
        print("Male")
    case "F":
        print("Female")
    case _:
        print("Invalid Input")
