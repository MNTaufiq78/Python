#9. Write a program to generate FileNotFoundException 
try:
    file = open("non_existent_file.txt", "r")  
except OSError as e:
    print("FileNotFoundException occured:",e)