#.1.....variable  (python is loosly type language).........
# name = input("\nEnter any name: ")                  #..store string type..
# length = len(name)
# print("name is: ",name)
# print("length is: ",length)

# name = 12121                                     #..store int type as a string...
# print("int value store in same variable: ",name)

# name = 12.2323                                    #..store float type as a string...
# print("float value store in same variable: ",name)





#.2....add two number.....but cancatinate...
# a_Value = int(input("Enter first value: "))
# b_Value = int(input("Enter Second value: "))
# sum = a_Value + b_Value             #.......concatinate values........
# print("Sum is: ",sum)               #....can't write '+' bcz int can"t cancatenate




#.....print character of string...
# print("Welcome"[2])
# print("Welcome"[-2])                #...from last 2nd digit



# 4....large number......
# num = 123_4567_789
# print(num)




# 5.....change int to string...str()..
# num = len(input("Enter string:  "))             # num is int
# num = str(num)                                  # now num is string
# print("String are "+num)                        # now cancatenate

# print(100+300)                                     #..add
# print(str(100)+str(300))                        #..cancatinate




# 6.......operator..........
# num1 = int(input("Enter first no: "))
# num2 = int(input("Enter seconf no: "))

# add = num1+num2
# sub = num1-num2

# mul = num1*num2
# pow = num1**num2                        # return power

# div1 = num1/num2                        # return float value
# div2 = num1//num2                       # return int value
# div3 = round(num1/num2)                 # 8/3 = 2.666666665 so return O/P: 3
# div4 = round(num1/num2, 3)              # return UPTO 3 decimal place  

# print("Addtion",add)
# print("Subtraction",sub)
# print("Multiplecation (*): ",mul)
# print("power: (**) ",pow)
# print("divide (/) float ", div1)
# print("divide2 (//) int", div2)
# print("divide3 round(/) ", div3)
# print("divide3 round(/) ", div4)







# logical op...........
a = 12
b = 12
c = a==12 and b==12
d = not(a>2)                # a 2 se bada nhi h (false)
print(c)
print(d)