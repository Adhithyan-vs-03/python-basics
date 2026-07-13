# file_reader.py

try:
    with open("sample.txt", "r") as file:
        content = file.read()
        print("File Content:")
        print(content)

except FileNotFoundError:
    print("File not found!")

except Exception as e:
    print("Error:", e)