# For loop 

# syntax:
# for variable_name in range(start,end):
#     print()

# for i in range(1,11):
#     print(i*2)

# Table of any number

# n = int(input("Enter your number "))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)


# While loop

# num = 4

# while num <= 20 :
#     print(f"number is {num}")
#     num += 1


# True while loop

# while True:
#     num1 = int(input("Enter 1st number "))
#     num2 = int(input("Enter 2nd number "))
#     print(num1 + num2)

#     res = input("Do you want to continue ")
#     if res == 'yes':
#         break


# Nested loops

# for i in range(1,6) :
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
    




# //******* Question on Loops *******\\

# 1.  Write a program to find sum of all even numbers up to 50

# sum = 0
# for i in range(2,51):
#     if(i % 2 == 0):
#         sum += i
   
# print("total sum is", sum)


# 2. write a program to write first 20 numbers and their squared number

# for i in range(1,21):
#     print(f"The square of {i} is ", i**2)


# 3. Write a program to find sum of first 10 odd numbers using while loop

# count = 0
# i = 1
# sum = 0
# while count<10:
#     if i % 2 != 0:
#         sum += i
#         count+=1
#     i+=1
# print("The sum of first 10 odd numbers is",sum)


# 4. write a program to check if a number is divisible by 8 and 12 up to 100 numbers 

# for i in range(1,101):
#     if i % 8 == 0 and i % 12 == 0:
#         print(i)


# 5. Write a program to print fibonacci series upto n numbers

# n = int(input("Enter your number: "))
# a = 0
# b = 1

# if n == 1:
#     print(1)
# else:
#     print(a,end=" ")
#     print(b,end=" ")
#     for i in range(2,n):
#      c = a+b
#      a = b
#      b = c
#      print(c,end=" ")



# 6. Check number is prime or not

# n = int(input('Enter your number to check : '))

# if n <= 1:
#     print(n,"is not a prime number")
# else:
#     for i in range (2,n):
#         if n % i == 0:
#             print(n,"is not a prime number")
#             break
#     else:
#         print(n,"is a prime number")



# 7. Check number is palindrome number or not

n = int(input("Enter number : "))
temp = n
rev = 0
while(n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10

if temp == rev :
    print(temp,"is palindrome number")
else: print(temp,"is not palindrome number")
