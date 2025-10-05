"""
A tuple is an immutable, ordered collection of elements in Python. 
Tuples can contain elements of different data types and are defined by enclosing the elements in parentheses, separated by commas. 
They are commonly used to group related data and can be accessed via indexing.
"""

# # How to create a tuple ?
# create_tuple = ("maruti","Bmw","thar","Bolero")
# create_tuples = "hii","hello","is",

# print(type(create_tuple))
# print(type(create_tuples))
# print(create_tuple)
# print(len(create_tuple))

# ***************Slicing in tuple ***********************

# print(create_tuple[1])
# print(create_tuple[:2])
# print(create_tuples[1:])
# print(create_tuple[-2::-1])

# **************** Loop in tuple *************************

create_tuple = ("maruti","Bmw","thar","Bolero")
create_tuples = "hii","hello","is",

# for i in create_tuples:                           for in loop
#     print(i)

# for i in range(len(create_tuple)):                for in loop in range
#     print(create_tuple[i],end=" ")

# i = 0                                             while loop
# while i< len(create_tuple):
#     print(create_tuple[i])
#     i+=1


""" if we want to add or modify tuple then first we convert the tuple
to list and then we can use all features of list in tuple"""

# create_tuple = list(create_tuple)         #this convert the tuple to list
# print(type(create_tuple))

# create_tuple.append("Ola")
# print(create_tuple)

# create_tuple = tuple(create_tuple)
# print(type(create_tuple))
