#11. Write a program to generate IOException
try:
    with open("non_existing_directory/test.txt", "w") as f:
        f.write("This will fail!")
except OSError as e:
    print("IOException occurred:", e)

