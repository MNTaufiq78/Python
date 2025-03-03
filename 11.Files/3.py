file = open("file.txt", "r")

chunk_size = 10  
while True:
    data = file.read(chunk_size)
    if not data:
        break
    print(data, end="") 

file.close()
