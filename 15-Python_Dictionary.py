
# Creating a Dictionary & Accessing
student={
    "name":"Rohit",
    "age":21,
    "city":"pune"
}
# print(student["name"])
# print(student["age"])
# print(student["city"])

# Adding and updating
# student["marks"]=85
# student["city"]="mumbai"
# print(student)

# Removing
# student.pop("age")
# student.pop("city")
# print(student)

# Dictionary methods

# print(student.keys())
# print(student.values())
# print(student.items())
# print(student.get("name"))

# Looping

# for k in student:
#     print(k,student[k])

# Nested dictionary
# employees={
#     "E101": {"name": "Rohit", "city": "Pune"},
#     "E102": {"name": "Sneha", "city": "Delhi"}
# }
# print(employees["E101"]["name"])
# print(employees["E101"]["city"])
# print(employees["E102"]["name"])
# print(employees["E102"]["city"])

# Mapping wrong → correct
mapper = {
    "mombai": "Mumbai",
    "kolkatta": "Kolkata",
    "jalgoon": "jalgaon"
}
print(mapper["mombai"])
print(mapper["kolkatta"])
print(mapper["jalgoon"])
