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

# print("1st: {}, 2nd: {}, 3rd: {}".format(num1,num2,num3))




# # ....separator {sep="some_thing"} ........
# print("my name is \"PAWAN\"")
# print("my", "name", "is", sep="....")




# #  {end="same_thing"}.....
# print(1,2,3,4, end=" ")
# print(5,6,7,8, end=" ")
# print("\n")
# print("hey", "pawan", end="||")





# # multiply operator (*)
# print(5 * 5)
# print(5 * " Hello")
# print("5" * " Hello")               # error (string multiplication not posible)





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





# ## Slicing..............
# li = ['a','b','c','d','e','f','g','h','i']
# print(li[1:5])              
# print(li[:-1])                  # apart form last  [a to h]
# print(li[:])                   # complete list
# print(li[0:-1])                 # apart from last value [a to h]
# print(li[-4:-1])                # [f,g,h]
# print(li[0:8:2])                # [a,ce,g]
# print(li[8:0:-2])               # **2 step reverse order [i,g,e,c]
# print(li[::-1])                 # **reverse     [i,h,g,f,e,d,c,b,a]






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



# #.......Math module.........
# import math
# # from math import function

# print(math.factorial(5))            # 120
# print(math.sqrt(16))                # 4.0
# print(math.ceil(3.2))               # 4
# print(math.floor(3.2))              # 3
# print(math.log(10))                 # 2.302..
# print(math.pow(2,4))                # 16




# # +ve and -ve infinite number
# a = float("inf")            # +ve infinite
# b = float("-inf")           # -ve infinite
# print(a, b)




# private attribute and function.......

# class Demo:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age            # private attribute
#     def dispName(self):
#         return self.name
#     def dispAge(self):
#         self.__fun()                # ...*  this way access private function
#         return self.__age           # access private attribute
    
#     def __fun(self):
#         print("Hiii")

# obj = Demo("Kamal", 12)
# print(obj.dispName())
# print(obj.dispAge())
# print()

# print(obj.name)
# # print(obj.__age)                # not accessible private attribute
# print(obj._Demo__age)             # but access private attribute
# print()

# # obj.__fun()                     # not accessible method
# print(obj._Demo__fun())           # but access private method




# # in operator.........
# name = "Coding the python programming"
# print("the" in name)        # True
# print("The" in name)        # Flase





# # in operator.........
# name1 = "Coding the python programming"
# name2 = "Coding the python programming"
# print(name1 is name2)        # True





# print(0 or 1)





# # monkey patching..........change the behaviour of funtion at run time 
# class Demo:
#     def __init__(self, name):
#         self.name = name
#     def fun(self):
#         print("My name is: ",self.name)
#     def f1(self):
#         self.fun()
#     def f2(self):
#         self.fun()

# obj = Demo("Harry")
# obj.f1()
# obj.f2()

# def new_fun():
#     print("Update")
# obj.fun = new_fun           # change the proterties of funtion
# obj.f1()
# obj.f1()



# # get code of emoji character and words
# print(ord('😀'))
# print(ord('🐕'))
# print(ord('a'))
# print(ord('स'))

# print(chr(2360))
# print(chr(65))
# print(chr(128512))





# # but sort element...
# k = [(22,4),(3,77),(45,1)]
# k.sort()                    # sort by 1th element                             
# print(k)

# # def fun(x):                 # sort by 2nd element
# #     return x[1]
# # k.sort(key=fun)
# # print(k)
# # ..or..........
# k.sort(key = lambda x: x[1])
# print(k)




no = [2,4,5,2,6,4]
def fun(no):
    no2 = []
    for i in no:
        if i not in no2:
            no2.append(i)
    return no2
print(fun(no))
