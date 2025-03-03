import os

file_path = "file.txt"

if os.path.exists(file_path):
    can_read = os.access(file_path, os.R_OK)
    can_write = os.access(file_path, os.W_OK)
    print(f"Read Access: {'Yes' if can_read else 'No'}")
    print(f"Write Access: {'Yes' if can_write else 'No'}")
else:
    print("File does not exist.")
