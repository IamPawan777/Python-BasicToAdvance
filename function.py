#.............simple function............
# def my_fun():
#     print("Hello World")
# my_fun()




# # .........With Argument...........
# def my_fun(name, marks):
#     print(f'name: {name}, marks: {marks}')
# my_fun("Pawan", 12)
# my_fun("Bisht", 32)
# my_fun("Radhe- radhe", 3434)





# # ...... *parameter.....don't know how many argument ..........
# def my_fun(*cars):
#     print(f'car is: {cars[1]}')                # function receive a tuple of argument 
# my_fun("BMW", "audi", "Tyata")



# # ............send arguement with key=value syntax.....order does't metter..........
# def my_fun(name1, name2, name3):
#     print("My favorite name is: ",name2)
# my_fun(name3="Radhe", name1=12, name2="Pawan")




# #..........**parament.......dont know how many key-value argument......also order not metter...
# def demo(**name):
#     print("names are:",name["n1"])              # function receive a dictionary of argument
# demo(n2="Pawan", n4=2332, n1=12.12, n3=True)




# # .........default parameter value........
# def demo(name="Ravi"):
#     print("names are:",name)             
# demo("pawan")
# demo()
# demo("Harry")





# # .....passing List as an argument........
# name = ["pawan", "Harry", "Ravi"]
# def demo(name):
#     for x in name:
#         print(x+" ")
# demo(name)




# #.......return statemnt........
# def sum(a,b):
#     return a+b
# print("Sum is: ",sum(12,3))



# #.......pass statemnt.....defination write in iater...
# def sum(a,b):
#     pass




# #......... Program.........
# import math
# def fun_disp(height, width, val):
#     ans = height + width / val
#     round_off = math.floor(ans)
#     print("Ans is: ",round_off)
      
# a_value = int(input("Enter first no: "))
# b_value = int(input("Enter second no: "))
# inte = 7
# fun_disp(a_value, b_value, inte)




# # recursion......
# def fibonacci(n):
#     if(n<=1):
#         return n
#     else:
#         return (fibonacci(n-1)+fibonacci(n-2))

# n = int(input("Enter a number: "))
# for c in range(n):
#     print(fibonacci(c))



# # program.............
# fruits = ["apple", "Banana", "Orange", "Lichi"]

# if len(fruits[0]) > len(fruits):
#     pri = fruits[0]
# else:
#     pri = fruits[len(fruits)-1]
    
# print(pri)



# lambda function:  a is argument
# fun = lambda a: a+10
# print(fun(5))
#....or.....
func = lambda a,b,c: c*a*b
print(func(2,3,4))