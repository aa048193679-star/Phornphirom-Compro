student = {"name": "Alice", "age": 25, "grade": "A", "major": "Computer Science"}

print("----------Example1----------")
for key in student:
    print(f"{key}: {student[key]}")

print("----------Example2----------")
for value in student.values():
    print(value)

print("----------Example3----------")
for key, value in student.items():
    print(f"{key}: {value}")