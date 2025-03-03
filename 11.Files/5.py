file = open("file.txt", "r")

file.seek(15)  
data = file.read(10)  
print("Data from index 15:", data)

file.close()
