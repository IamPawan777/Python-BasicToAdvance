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






#....separator {sep="some_think"}   {end="same_think"}.....
# print("my name is \"PAWAN\"")
# print("my", "name", "is", sep="....")
# print("hey", "pawan", end="||")




#......change upper() or lower() case
# name = "Pawan Bisht"
# l = name.upper()
# u = name.lower()
# print(f"{l},,   {u}")





#.........count().........
# name = "Pawan Bisht"
# n = name.count("a")
# m = name.count("B")
# print(f"{n},, {m}")
# print("Pawan".count("a"))





#......to check how many function in perticular object.......
# print(dir(str))






#.........ramdom module and their function........
import random

random_int = random.randint(1,10)                   # generate random int number
random_f = random.random()                          # generate random floating num but (0 -- 1)
random_f2 = random.random() * 10                    # generate 0.0** -- 9.0**
print(random_int)
print(random_f)
print(random_f2)