import random
# world = "Hello World"
# hello = "Hello"
# print(hello)
# print(world)
#
# a = int(input("Type in a number"))
# if (a % 2) == 0:
#         print(a,"Is even.")
# else:
#         print(a, "is odd")
#
# name = "Kevin Munar"
# age = "29"
#
# print(name)
# print(age)
# nameAge = name +" is "+age

# print(nameAge)
# number = random.randint(1,20)
# guess = None
#
# while guess != number:
#         guess = input("Guess a number from 1 - 20\n")
#         guess = int(guess)
#         if guess == number:
#                 print("congrats you found the numbers!")
#                 break
#         else:
#                 print("Try again")
########################################################
# 5.Declare a list
# [1, 4, 9, 16, 25]
#  or tuple
# (1, 4, 9, 16, 25)
# , and using the for-loop print out all values that are even.
# list = [1, 4, 9, 16, 25]
# for i in list:
#         if i % 2 == 0:
#                 print(i)
# else:
#         print("Not even", i)
years = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
sum = 0
i = 0;
while i < len(years):
    sum+=i

    i+=1

print(sum)