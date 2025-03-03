file = open("file.txt", "r")

file.seek(5)  
print(file.read(10))  

file.close()
