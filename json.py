import json

# Python dictionary
student = {
    "name": "Adhithyan",
    "course": "BCA",
    "age": 21
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("Data written to student.json")


with open("student.json", "r") as file:
    data = json.load(file)

print("\nData read from JSON file:")
print(data)
print("Name:", data["name"])
print("Course:", data["course"])