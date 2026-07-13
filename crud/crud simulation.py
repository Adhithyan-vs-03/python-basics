students = []

# Create
students.append("Rahul")
students.append("Arun")
students.append("Anu")

print("After Create:")
print(students)

# Read
print("\nRead Data:")
for student in students:
    print(student)

# Update
students[1] = "Akhil"

print("\nAfter Update:")
print(students)

# Delete
students.remove("Anu")

print("\nAfter Delete:")
print(students)