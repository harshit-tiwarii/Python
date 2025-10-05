# basiclist.py


# Definition:
# A list in Python is an ordered, mutable collection of items, which can be of mixed data types.

# Points to remember:
# - Lists are defined using square brackets: []
# - Lists can contain elements of different types (int, float, str, etc.)
# - Lists are mutable: you can change, add, or remove elements after creation
# - Lists support indexing and slicing
# - Common methods: append(), remove(), insert(), pop(), sort(), reverse()


# Basic examples of using lists in Python

# Creating a list
# fruits = ["apple", "banana", "cherry"]

# Accessing elements
# print(fruits[0])  # Output: apple

# Modifying elements
# fruits[1] = "blueberry"
# print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

# # Adding elements
# fruits.append("orange")
# print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']

# # Removing elements
# fruits.remove("cherry")
# print(fruits)  # Output: ['apple', 'blueberry', 'orange']

# # Iterating through a list
# for fruit in fruits:
#     print(fruit)

# # List length
# print(len(fruits))  # Output: 3

# ************************* PRACTICE LISTS ******************************

students = ["siddhu","Abhishek","Aadi","Raj",1,1.5]
# print(students)

# print(students[2::-1])

# for i in range (len(students)):
#     print(students[i])

# students.append(9)
# students.append("Hii")
# print(students)


# shorthand loop
# [ print(i,end=" ") for i in students ]




# ************************ Some commonly used built-in list functions and methods:*******************************************



# 1. len() - Returns the number of items in the list
# print("Length:", len(students))

# # 2. min() and max() - Return the smallest/largest item (works if all elements are comparable)
# # For demonstration, let's use a numeric list:
# numbers = [5, 2, 9, 1, 7]
# print("Min:", min(numbers))
# print("Max:", max(numbers))

# # 3. sum() - Returns the sum of all elements (works with numeric lists)
# print("Sum:", sum(numbers))

# # 4. list() - Converts other iterables to a list
# tuple_example = (1, 2, 3)
# print("List from tuple:", list(tuple_example))

# # 5. sorted() - Returns a new sorted list
# print("Sorted numbers:", sorted(numbers))

# # 6. students.index(value) - Returns the index of the first occurrence of value
# print("Index of 'Raj':", students.index("Raj"))

# # 7. students.count(value) - Returns the count of value in the list
# print("Count of 1:", students.count(1))


numbers = [1,2,5,0,65,4,7,3,2]

# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
# print(numbers.count(2))
# print(sum(numbers))

# numbers.pop(2)
# print(numbers)

# numbers.sort()
# print(numbers)

# print( numbers.index(2))

# num = [99,98,96]
# print(num)
# num.extend(numbers)
# print(num)