# Definition and example of a dictionary in Python

# A dictionary is a built-in Python data structure that stores key-value pairs.
# Keys must be unique and immutable (e.g., strings, numbers, tuples).
# Values can be of any data type.

# Example:
# person = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }

# # Accessing values
# print(person["name"])  # Output: Alice

# # Adding a new key-value pair
# person["email"] = "alice@example.com"

# # Iterating over keys and values
# for key, value in person.items():
#     print(f"{key}: {value}")



# **************************create dictionary *************************

# students = {
#     "name": "Vijay",
#     "age": 20,
#     "Rollno": 12
# }

# # print(students) 
# print(students["age"])                // 20

# PRINTING ALL THE KEYS NAME ONE BY ONE
# for i in students:
#     print(i)


# PRINTING ALL THE VALUES NAME ONE BY ONE
# for i in students:
#     print(students[i])


# ITERATE DIRECTLY IN VALUES OF A DICTIONARY
# for i in students.values():
#     print(i)


# GET KEYS AND VALUE TOGATHER THROUGH ITERATION

# for x,y in students.items():
#     print(x,"-",y)



# ********************** Functions used in dictionary ****************************

# len() - Returns the number of key-value pairs in the dictionary
students = {"name": "Vijay", "age": 20, "Rollno": 12}
print(len(students))  # Output: 3

# dict.keys() - Returns a view object of all keys
print(students.keys())  # Output: dict_keys(['name', 'age', 'Rollno'])

# dict.values() - Returns a view object of all values
print(students.values())  # Output: dict_values(['Vijay', 20, 12])

# dict.items() - Returns a view object of key-value pairs (tuples)
print(students.items())  # Output: dict_items([('name', 'Vijay'), ('age', 20), ('Rollno', 12)])

# dict.get(key, default) - Returns the value for key if key is in the dictionary, else default
print(students.get("name"))  # Output: Vijay
print(students.get("email", "Not Found"))  # Output: Not Found

# dict.update(other_dict) - Updates the dictionary with elements from another dictionary
students.update({"email": "vijay@example.com"})
print(students)

# dict.pop(key) - Removes the specified key and returns the value
age = students.pop("age")
print(age)  # Output: 20
print(students)

# dict.popitem() - Removes and returns the last inserted key-value pair as a tuple
item = students.popitem()
print(item)
print(students)

# dict.clear() - Removes all items from the dictionary
students.clear()
print(students)  # Output: {}