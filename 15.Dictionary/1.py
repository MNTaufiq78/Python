# 1.Create a Dictionary with at least 5 key value pairs of the Student ID and Name
students = {
    101: "Alice",
    102: "Bob",
    103: "Charlie",
    104: "David",
    105: "Emma"
}

# 1.1 Adding values to the dictionary
students[106] = "Frank"  # Adding a new student
print("After Adding:", students)

# 1.2 Updating a value in the dictionary
students[102] = "Bobby"  # Updating Bob to Bobby
print("After Updating:", students)

# 1.3 Accessing a value from the dictionary
student_id = 103
if student_id in students:  # Checking key manually
    print(f"Student with ID {student_id} is {students[student_id]}")
else:
    print(f"Student ID {student_id} not found")

# 1.4 Creating a nested dictionary
nested_students = {
    101: {"name": "Alice", "age": 20, "grade": "A"},
    102: {"name": "Bobby", "age": 21, "grade": "B"},
    103: {"name": "Charlie", "age": 22, "grade": "A"},
}

# 1.5 Accessing values of a nested dictionary
student_id = 101
if student_id in nested_students:
    print(f"Details of Student {student_id}:")
    for key in nested_students[student_id]:  # Manual loop to access keys
        print(f"{key.capitalize()}: {nested_students[student_id][key]}")
else:
    print(f"Student ID {student_id} not found in nested dictionary")

# 1.6 Printing all keys in the dictionary manually
print("Keys in dictionary:", [key for key in students])  # Extract keys manually

# 1.7 Deleting a value from the dictionary manually
delete_id = 104
if delete_id in students:
    del students[delete_id]
    print(f"Student ID {delete_id} deleted successfully!")
else:
    print(f"Student ID {delete_id} not found!")
print("Final Dictionary:", students)
