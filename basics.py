#......print "Hello World"......
# print("Hello World")
# print("PAWAN \nBISHT")
# print(2323)



#.......concatinate string........
# print("\nHello"+" Wolrld ")



"""
    Take input form user.......input()
"""
# input("\nEnter no: ")
# print("Hollo "+input("My name: "))




"""
    length of string..........len()
"""
# print("\n")
# print(len("Hello"))
# print(len(input("Enter any thing to check length: ")))





#...type().....can check type of variable....
# num = 12
# print(type(num))
# num = float(12)
# print(type(num))
# num = 12.232
# print(type(num))





# #......fstring......different datatype to string.........
# num1 = 12
# num2 = 12.334
# num3 = True
# print(f"first: {num1}, second: {num2}, third: {num3}")          #...f write in front of "..."






# # ....separator {sep="some_thing"}   {end="same_thing"}.....
# print("my name is \"PAWAN\"")
# print("my", "name", "is", sep="....")
# print("hey", "pawan", end="||")




# #......change upper() or lower() case
# name = "Pawan Bisht"
# l = name.upper()
# u = name.lower()
# print(f"{l},,   {u}")





# .........count().........
# name = "Pawan Bisht"
# n = name.count("a")
# m = name.count("B")
# print(f"{n},, {m}")
# print("Pawana".count("a"))





# #......to check how many function in perticular object.......
# print(dir(str))






#.........ramdom module and their function........
# import random

# random_int = random.randint(1,10)                   # generate random int number
# random_f = random.random()                          # generate random floating num but (0 -- 1)
# random_f2 = random.random() * 10                    # generate 0.0** -- 9.0**
# print(random_int)
# print(random_f)
# print(random_f2)

# or.........
# from random import choice, randint
# li = [1,2,3,4,5]
# print(choice(li))
# print(randint(100,200))




# # access local varible out side by 'global' keyword ...or... change global variable
# # x= 2
# def fun():
#     global x
#     x = 300
#     print(x)
# fun()
# print(x)            # print local varible




# # date 
# from datetime import date

# x = date.today()
# print(x)
# print(x.month)
# print(x.day)



#.......Math module.........
import math
# from math import function

print(math.factorial(5))            # 120
print(math.sqrt(16))                # 4.0
print(math.ceil(3.2))               # 4
print(math.floor(3.2))              # 3
print(math.log(10))                 # 2.302..
print(math.pow(2,4))                # 16