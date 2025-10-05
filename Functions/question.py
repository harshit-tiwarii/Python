# 1. Write a python progrsm to find greatest of 3 numbers

# def numbers(val1,val2,val3):
#     if val1 > val2 and val1 > val3:
#         print(val1,"is the greatest number")

#     elif val2 > val1 and val2 > val3 :
#         print(val2,"is greatest number")
#     else :
#         print(val3,"is the greatest number")

# numbers(213,34,411)


# 2. Write a python funsction to create and print a list where the values are square of numbers between 1 to 30

# def create_list ():
#     list = []
#     for i in range (1,31):
#         list.append(i**2)
#     return list

# print(create_list())


# 3. Write a python function that takes number as a parameter and checks number is prime or not

# def check_prime(num):
#     if num < 2:
#         print("Not a prime number")
#         return
#     if num == 2:
#         print("Prime number")
#         return
#     for i in range(2,num):
#         if num % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("prime number")

# check_prime(55)


# 4. Write a python function that sum all the list in a python

# list = [2,3,6,3,4,1,8]
# def sumOfList(list):
#     sum = 0
#     for i in list:
#         sum += i
#     return sum

# print(sumOfList(list))


# 5. Write a python function that sum all the list in a python using recursion

# list = [2,3,6,3,4,1,8,9,8]
# def sumOfList(list):   
#     if(len(list) == 1):
#         return list[0]
#     else:
#         return ( list[0] + sumOfList(list[1:]) )

# print('The sum of list is',sumOfList(list))



# 6. Write a python function to solve fibonacci series using recursion

def finonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n + finonacci(n-1)