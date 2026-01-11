
students = {
"student1": {
    "name": "Amit",
    "age": 20,
    "grade": "A"
    },
"student2": {
    "name": "Neha",
    "age": 22,
    "grade": "B"
    }
}

# print(students)

# print(students["student1"])

for key, value in students.items():
    print(key)
    for sub_key, sub_value in value.items():
        print(sub_key, ":", sub_value)