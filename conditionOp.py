#1...if-else.....
# a = 10
# b = 5
# if b>a:
#     print("b is greater")
# else:
#     print("a is greater")




#......multiple if.......
# if condition:
#     if condition:
#     elif condition:
#     elif condition:
#     else:

#     if condition:
#     else: 

#     if condition:
#     elif condition:
#     else:

#     if
# else:




#2.......if-elif-else.......
# a = 10
# b = 10
# if b>a:
#     print("b is greater")
# elif(b<a):
#     print("a is greater")
# elif(a==b):
#     print("a and b equal")
# else:
#     print("nothing")






# # 3.......if-elif ladder.......
# num = 30
# a = 12
# b = 5
# if num>a:
#     print("num is greater then a")
#     if num<a:
#         print("a is greater then num")
#     elif num<b:
#         print("b is greater then num")
#     elif num==30:
#         print("num is 30")
#     else:
#         print("all condition false")
# else:
#     print("else condition")





# #........Even of Odd......
# num = int(input("Enter number: "))
# if num>0:
#     if num%2==0:
#         print("Number is Even")
#     else:
#         print("Number is Odd")
# else:
#     print("only positive no.")





# #...leap year or not..........
# year = int(input("Enter any year do we want to cheack: "))
# if(year%4 == 0):
#     if(year%100 == 0):
#         if(year%400 ==0):
#             print("leap year")
#         else:
#             print("not a leap year")
#     else:
#         print("leap year")
# else:
#     print("Not a leap year")




# # truely value: [2], (1,3), "ba", 7, -23
# # falsy value: [], (), '', 0
# if [2,3]:
#     print("truely value")
# else:
#     print("Wrong")
# if 0:
#     print("truely value")
# else:
#     print("Wrong")




# match and case (switch-case).......
day = 35
match day:
    case 1:
        print("Sunday..")
    case 2:
        print("Monday..")
    case 3:
        print("Tuesday..")
    case 4:
        print("Wednesday..")
    case 5:
        print("Thrusday..")
    case 6:
        print("Friday..")
    case 7:
        print("Saturday..")
    case _:
        print("no days..")