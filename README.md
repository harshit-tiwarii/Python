 🐍 Python Notes — Basic to Advanced

Welcome to the **Complete Python Notes** repository!  
This document is for learning Python from **beginner to advanced**, focusing on **core programming concepts**.

---

## 📘 Table of Contents

1. [Introduction to Python](#introduction-to-python)
2. [Variables and Data Types](#variables-and-data-types)
3. [Operators](#operators)
4. [Conditional Statements](#conditional-statements)
5. [Loops](#loops)
6. [Lists](#lists)
7. [Tuples](#tuples)
8. [Sets](#sets)
9. [Dictionaries](#dictionaries)
10. [Functions](#functions)
11. [Recursion](#recursion)
12. [Modules and Packages](#modules-and-packages)
13. [File Handling](#file-handling)
14. [Common Python Built-in Functions](#common-python-built-in-functions)
15. [Bonus: Best Practices](#bonus-best-practices)

---

## 🧠 Introduction to Python

- **Python** is a high-level, interpreted, and object-oriented language.
- Known for its **simplicity, readability**, and **versatility**.
- Used in **data analysis, web development, AI, ML, and automation**.

```python
print("Hello, Python!")
📊 Variables and Data Types
➤ Variables
Variables are used to store data.


name = "Harshit"
age = 21
price = 99.99
is_active = True

➤ Data Types
Type	Example	Description
int	10	Integer
float	3.14	Decimal number
str	"hello"	String
bool	True / False	Boolean
list	[1,2,3]	Ordered, mutable
tuple	(1,2,3)	Ordered, immutable
set	{1,2,3}	Unordered, unique
dict	{"a":1,"b":2}	Key-value pairs

⚙️ Operators

➤ Arithmetic
x, y = 10, 3
print(x + y)  # 13
print(x - y)  # 7
print(x * y)  # 30
print(x / y)  # 3.333
print(x // y) # 3 (floor division)
print(x ** y) # 1000 (exponent)
print(x % y)  # 1 (modulus)

➤ Comparison

print(x > y)   # True
print(x == y)  # False
print(x != y)  # True

➤ Logical

a, b = True, False
print(a and b)  # False
print(a or b)   # True
print(not a)    # False

➤ Assignment

x = 5
x += 2   # x = x + 2
x *= 3   # x = x * 3

🔀 Conditional Statements

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

🔁 Loops

➤ For Loop

for i in range(5):
    print("Iteration:", i)

➤ While Loop

count = 0
while count < 5:
    print(count)
    count += 1

➤ Loop Control

for i in range(10):
    if i == 5:
        break  # exits loop
    if i == 2:
        continue  # skip iteration
    print(i)

📋 Lists
Ordered, mutable (can change values)
Allows duplicate elements

fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # apple
fruits.append("mango")     # to add element in last we use append
fruits.remove("banana")
fruits[1] = "grapes"
print(fruits)

➤ Useful List Methods

numbers = [1, 2, 3, 4, 5]
print(sum(numbers))
print(len(numbers))
print(max(numbers))
print(min(numbers))
numbers.reverse()
numbers.sort()

➤ List Comprehension

squares = [x**2 for x in range(5)]
print(squares)

🔸 Tuples
Ordered and immutable
Faster than lists

t = (1, 2, 3)
print(t[0])

# Cannot modify
# t[0] = 5  ❌ Error

# Tuple unpacking
a, b, c = t
print(a, b, c)

🔹 Sets
Unordered, unique elements only.

cities = {"Delhi", "Mumbai", "Delhi", "Pune"}
print(cities)  # {'Delhi', 'Mumbai', 'Pune'}

cities.add("Bangalore")
cities.remove("Pune")

➤ Set Operations

a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

🔸 Dictionaries
Key-Value pairs, mutable.

student = {
    "name": "Harshit",
    "age": 21,
    "city": "Delhi"
}

print(student["name"])
student["age"] = 22
student["gender"] = "Male"
print(student)

➤ Dictionary Methods

print(student.keys())
print(student.values())
print(student.items())

student.update({"city": "Mumbai"})

➤ Nested Dictionary

data = {
  1: {"name": "harshit", "city": {"delhi", "bangalore"}, "gender": "Male"},
  2: {"name": "rahul", "city": "mumbai", "gender": "Male"},
}
data[1]["city"].add("pune")
print(data)

🧩 Functions

➤ Basic Function

def greet(name):
    return f"Hello, {name}!"

print(greet("Harshit"))

➤ Default & Keyword Arguments

def intro(name, age=21):
    print(f"My name is {name}, age {age}")

intro("Harshit")
intro(age=22, name="Rahul")

➤ *args and **kwargs

def sum_all(*nums):
    return sum(nums)

def show_info(**details):
    for key, value in details.items():
        print(key, ":", value)

print(sum_all(1, 2, 3, 4))
show_info(name="Harshit", city="Delhi")

🔁 Recursion
A function calling itself.

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120

📦 Modules and Packages

➤ Creating and Importing
module1.py

def greet(name):
    print(f"Hello, {name}")
main.py

import module1
module1.greet("Harshit")

➤ Importing Specific Functions

from math import sqrt, pi
print(sqrt(25), pi)

➤ Installing External Modules
bash
Copy code
pip install requests

📁 File Handling
python
Copy code
# Write
with open("data.txt", "w") as file:
    file.write("Hello, world!")

# Read
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

🧮 Common Python Built-in Functions

Function	Description

len()	Length of iterable
type()	Returns data type
sum()	Sum of numbers
max() / min()	Largest / smallest value
sorted()	Sorts elements
range()	Generates a sequence
enumerate()	Returns index with value
zip()	Combines iterables
map()	Applies function to iterable
filter()	Filters based on condition
