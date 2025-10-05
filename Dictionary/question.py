# 1. write a program that multiply items of all list

# dict = {"a":1,"b":2,"c":3,"d":4,"e":5}
# product = 1
# for i in dict:
#     product *= dict[i]

# print(product)

# 2. write a python script to print a dictionary where the keys are numbers between 1 to 15 and vakues are squqare of keys

# numbers = {}

# for i in range(1,16):
#     numbers[i] = i * i

# print(numbers)


# write a program that sort the values of a dictionary
# dict = {"a":1,"b":2,"c":3,"d":4,"e":5}

# print(dict)
# dict = sorted(dict.values())

# print(dict)

dict = {
         1: {"name": "harshit","city":{"delhi","banglore"},"gender":"Male"},
         2: {"name": "rahul", "city": "mumbai","gender":"Male"},
         3: {"name": "sapna", "city": "pune","gender": "female"}
        }
# print(dict[3])
# print(dict[1]["city"])
# print(dict[2]["name"])

# dict.update({4:{"name":"aman"}})
# print(dict)

print(dict[1]["city"])