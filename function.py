# # .............simple function............
# def my_fun():
#     print("Hello World")
# my_fun()



# def my_fun(x):
#     x*=2
#     return x
# a = 12
# print(my_fun(a))




# # .........With Argument...........
# def my_fun(name, marks):
#     print(f'name: {name}, marks: {marks}')
# my_fun("Pawan", 12)
# my_fun("Bisht", 32)
# my_fun("Radhe- radhe", 3434)




# # .........default argument value........
# def demo(name="Ravi"):
#     print("names are:",name)             
# demo("pawan")
# demo()


# def demo(name, msg = "Hello"):
#     print(name, msg)
# demo("Pawan")





# # ...... *parameter.....don't know how many argument ..........
# def my_fun(*cars):
#     print(f'car is: {cars[1]}')                # function receive a tuple of argument 
# my_fun("BMW", "audi", "Tyata")



# def fun(*args, a, b):
#     print(type(args))
#     print(args)
#     print(a)
#     print(b)
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)
# fun(1,3,4,5, a=1000, b=5555)




# # ............send arguement with key=value syntax.....order does't metter..........
# def my_fun(name1, name2, name3):
#     print("My favorite name is: ",name2)
# my_fun(name3="Radhe", name1=12, name2="Pawan")




# #..........**parament.......dont know how many key-value argument......also order not metter...
# def demo(**name):
#     print("names are:",name["n1"])              # function receive a dictionary of argument
# demo(n2="Pawan", n4=2332, n1=12.12, n3=True)


# def fun(**args):
#     for key in args:
#         print(key + " : " + args[key])

# fun(Country='Canada',Province='Ontario',City='Toronto')


# def fun(**args):
#     print(args)
#     for k,v in args.items():
#         print(k,"->",v, end=' | ')
# fun(a="Pawan", b="Bisht", c="Harry")





# # .....passing List as an argument...(list are mutable).....
# name = ["pawan", "Harry", "Ravi"]
# def demo(name):
#     for x in name:
#         print(x+" ")
# demo(name)


# def demo(na):
#     na.append("kakak")
# print(name)            # before appending..... 
# demo(name)
# print(name)            # after appending.....




# #.......return statemnt........
# def sum(a,b):
#     return a+b
# print("Sum is: ",sum(12,3))


# def fun(a:int, b:int) -> int:               # explicitly told return int value and values are also int
#     return a+b
# print(fun(11,4))




# #.......pass statemnt.....defination write in iater...
# def sum(a,b):
#     pass






# #  method overloading not suppoted....by default last one is consider
# class Poly:
#     def fun(self, a):
#         print("Poly1 class...",a)

#     def fun(self, a):
#         print("class...",a)

# p = Poly()
# p.fun(23)






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



# #lambda function:  a is argument
# fun = lambda a: a+10
# print(fun(5))

# func = lambda a,b,c: c*a*b
# print(func(2,3,4))

# def fun():                      
#     return lambda msg: print(msg)       # function nasting
# print(fun()("hello World"))





# # largest number.
# (lambda a,b: print(a) if a>b else print(b)) (2,3)







# # function can print and return togather at a time
# def fun(li):
#     print(li)               # 1 task- print
#     return li[0]+100        # 2 task- add in oth index

# li = [12,34,"pa",True]
# print(fun(li))





# print with index:.....................
# def fun(li):
#     for i,s in enumerate(li):
#         print(i,' ',s)

# li = [12,34,"pa",True]
# fun(li)





# # globle variable........
# a = 11                  # globle variable
# def fun(aaa):
#     global x            # globle variable
#     x = 99
#     print(aaa)

# fun(a)
# fun(x)




# # count the word comes...........
# st = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"
# def little(s, key):
#     li = []
#     dic = {}
#     li = s.split()
#     for i in li:
#         if i==key:
#             dic[i] = li.count(i)
#             print(dic)
# little(st, "little")




# # function nesting:
# def outer():
#     print("outer function")
#     def inner():
#         print("Inner function")
#     return inner

# outer()()




# # return multiple function: (but in the form of tuple)

# def fun(age, name, course):
#     return age, course, name

# ans = fun(12,"Harry", "JAVA")
# a,b,c= fun(12,"Harry", "JAVA")
# print(ans)
# print(b)

          

def f(a,b):
    print(a,b)
f(a=33,b=9)