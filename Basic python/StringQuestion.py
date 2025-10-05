# 1.  Write a program to take a string input and print its length.

# str = input("Enter your string : ")
# length = len(str)
# print(length)


# 2.  Take a string and print it in uppercase and lowercase.
# str = "Harshit"
# print(str.upper())
# print(str.lower())


# 3.  Check whether a given string is a palindrome

# str = "bob"
# reverseStr = str[::-1]
# if str == reverseStr:
#     print("palindrome")
# else:
#     print("not palindrome")


# 4.  Count the number of vowels in a string.

# str = "harshit"
# count = 0
# for i in str:
#     if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
#         count += 1

# print(count)


# 5.  Replace all spaces " " in a string with "-".

# str = "harshit tiwari BCA"
# for char in  str:
#       result =  str.replace(' ','-')

# print(result)

# name = 'ajay'
# age = 12
# b= "My name is {} and age is {}"
# print(b.format(name,age))

# print(name.center(20,"*").upper())


# *************************************String pre built functions************************************

# a = "Harshit"
# b = "Harshit123"
# c = "Harshit.12"
# d = "Harshit Tiwari"
# e = "123456"
# f = "123Hello"

# print("a is alphanumeric ?",a.isalnum())
# print("b is alphanumeric ?",b.isalnum())
# print("c is alphanumeric ?",c.isdecimal())
# print("d is alphanumeric ?",d.isalnum())
# print("e is", e.isdecimal())
# print("f is alphanumeric ?",f.isalnum())


# a = "adcbfehg"

# print(sorted(a))


# 6  write a program to remove given character in a string

# str = "H.E.L.L.O"
# newStr = str.replace(".","")
# print(newStr)

# 7.  reverse a string

str = input("enter string : ")
reverseStr = str[::-1]
print(reverseStr)

print(str[2::-1])