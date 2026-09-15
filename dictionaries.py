''' A Dictionary stores data in key-value pairs.
    dictionary_name = {
    "key": "value"
}
Dictionary keys cannot have duplicates.values can be duplicate
Dictionary is Mutable,We can change dictionary values.
Ordered,Modern Python dictionaries preserve insertion order.
Different Data Types Are Allowed.
Accessing Dictionary Values,We access values using their keys.
Adding a New Key-Value Pair.


'''

#Important Dictionary Methods keys(),values(),items(),get(),update(),pop(),popitem(),clear()

students={
         "name":"Aswini",
         "age":23,
         "course":"B.Tech",
         "Branch":"ECE",
         "Department":"ECE"
         }
students["age"]=22
students["city"]="Hyderabad"
students.pop("Branch") # Removing the data
#del students["city"] deletes the data
print(students)
print(students.keys())
print(students.values())
print(students.items())
print(students.get("name"))
print(students["course"])
for key,value in students.items():
    print(key," : " ,value)

#User Inputs
students = {
    "name": input("Enter your name: "),
    "age": input("Enter your age: "),
    "course": input("Enter your course: "),
    "Branch": input("Enter your branch: "),
    "Department": input("Enter your department: ")
}

print(students)

#Nested Dictionaries,A dictionary can contain another dictionary.
students = {
    "student1": {
        "name": "Aswini",
        "age": 23
    },
    "student2": {
        "name": "Ravi",
        "age": 24
    }
}
print(students["student1"]["name"])