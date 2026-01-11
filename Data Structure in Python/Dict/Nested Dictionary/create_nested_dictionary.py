
students = {
    "name" : "Rahul",
    "age" : 29,
    "marks" : {
        "math" : 85,
        "Science" : 70,
        "English" : 68
    }
}

# print(students)

# print(students["name"])

# print(students["marks"]["math"])

students["marks"]["math"] = 95

print(students["marks"]["math"])

students["marks"]["Computer"] = 50

print(students)