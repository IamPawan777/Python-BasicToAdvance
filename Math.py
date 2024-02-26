# # 1.....sum of 2 digit no.....
# num = input("Enter 2 digit no only: ")
# first = int(num[0])
# second = int(num[1])
# sum = first + second
# print(sum)
# print("type of num: ",type(sum))                # now sum also is int





# # 2.........squre of num........ **-(squre operator)......

# num = int(input("Enter any no: "))
# squre = int(num**2)
# print(squre)





# # 3.Game.......... calculate life of lives..(fstring).......

# age = input("Enter your age: ")
# age_as_int = int(age)
# year_remain = 80 - age_as_int
# months_remain = year_remain*12
# week_remain = year_remain*52
# days_remain = year_remain*365

# print(f"you have year remaining: {year_remain}, months remaining: {months_remain}, week remaining {week_remain} ,days remaining: {days_remain}")






# 4............calculate true love..........
# print(".....Welcome to the true love calculator......")
# boy_name = input("Enter boy name:  ")
# girl_name = input("Entre girl name: ")
# combine_name = boy_name + girl_name
# lower_case_str = combine_name.lower()

# t = lower_case_str.count("t")
# r = lower_case_str.count("r")
# u = lower_case_str.count("u")
# e = lower_case_str.count("e")
# true = t+r+u+e

# l = lower_case_str.count("l")
# o = lower_case_str.count("o")
# v = lower_case_str.count("v")
# e = lower_case_str.count("e")
# love= l+o+v+e

# love_percentage = str(true) + str(love)
# print("Love success rate:"+love_percentage)

# ...........or................

# import random
# love_percentage = random.randint(1, 100)
# print(f'love success rate is : {love_percentage}')




 



# # 5...........Treasure Hunt game..............
# print("Welcome to treasure hunt game, find island [....left->wait->red....(win game)]")
# choice1 = input('Which side you want to go "left" or "right" : ').upper()

# if choice1 == "LEFT":
#     choice2 = input('you come in right place...now you want to "swim" or "wait" : ').upper()
#     if choice2 == "WAIT":
#         choice3 = input('you were waited here....now you want choose door....."red" or "Yellow" or "blue" : ').upper()
#         if choice3 == "RED":
#             print(".......YOU WIN......")
#         elif choice3 == "YELLOW":
#             print('Choose wrong door "yellow".........GAME OVER.............')
#         elif choice3 == "BLUE":
#             print('Choose wrong door "Blue".........GAME OVER.............')
#         else:
#             print("Choose wrong door.........GAME OVER.............")
#     else:
#         print('If you had "wait" there you would have got the treasure.......GAME OVER!..........')
    
# else:
#     print('treasure present at "left" side........GAME OVER!.........')







# # 6.............HEAD and TAIL (random)........................
# import random
# random_int = random.randint(0,1)
# if random_int == 0:
#     print('HEADs')
# else:
#     print('TAILs')




# 7......... get random person (random and string)..........
import random
inpu = input("Enter person name (with comma and space): - ")
name = inpu.split(', ')                    # return the list
# index = random.randint(0, len(name)-1)          # return random index
# ran_name = name[index]                     # get value from list
    #..or...
ran_name = random.choice(name)
print(f"person is: {ran_name}")




# # 8.......Student average height..(list and loop).......
# std_height = input("Enter student height (space can be spilt): ").split()
# # print(std_height)                   # got string

# for n in range(0, len(std_height)):                 # now change into the integer
#     std_height[n] = int(std_height[n])
# print(std_height)

# # total_height = sum(std_height)
# # count = len(std_height)
#     #....or.........
# total_height = 0
# count = 0
# for x in std_height:
#     total_height += x
#     count += 1

# avg_height = round(total_height/count)
# print(avg_height)







# # 9.........highest number....(loop, string)....
# num = input("Enter number: ").split(" ")            # saparate num with single space
# for x in range(len(num)):
#     num[x] = int(num[x])
# # print(max(num))
#     #........or........
# highest = 0
# for x in num:
#     if x > highest:
#         highest = x
# print(f'Hightest no is {highest}')





# 10..........sum of even number.........
# sum = 0
# for x in range(0, 101):
#     if x%2 == 0:
#   #......or.......
# # for x in range(0, 101, 2):
#         sum += x
# print(sum)




# #.11........Fizz and Buzz.........
# num = int(input("Enter num: "))
# if num%3 == 0 and num%5 == 0:
#     print('FIZZ BUZZ')
# elif num%3 == 0:
#     print('FIZZ')
# elif num%5 == 0:
#     print('BUZZ')
# else:
#     print('Not divisible by 3 and 5')





# 12.....password generator........
# import random
# letter = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
#           'O','P','Q','R','S','T','U','V','W','X','Y','Z']
# symbol = ['@','#','$','%','&']
# number = ['0','1','2','3','4','5','6','7','8','9']
# t_Letter = int(input("Total letter: "))
# t_Symbol = int(input("Total symbol: "))
# t_Number = int(input("Total number: "))

# # ......easy...........
# password = ""
# for x in range (0, t_Letter):
#     password += random.choice(letter)
# for x in range (0, t_Symbol):
#     password += random.choice(symbol)
# for x in range (0, t_Number):
#     password += random.choice(number)
# print(f'Password is: {password}')

# # #....hard........
# password_list = []
# for x in range (0, t_Letter):
#     # password_list += random.choice(letter)
#   #.....or.......
#     password_list.append(random.choice(letter))
# for x in range (0, t_Symbol):
#     password_list += random.choice(symbol)
# for x in range (0, t_Number):
#     password_list += random.choice(number)
# # print(f'Password is: {password_list}')

# random.shuffle(password_list)

# password = ""
# for x in password_list:
#     password += x
# print(f'Password is: {password}')






# # ....check prime number......
# def check_Palim(n):
#     is_prime = True
#     for x in range(2, n):
#         if n%x == 0:
#             is_prime = False
#     if is_prime:                # is_prime == true
#         return is_prime
#     else:
#         return is_prime


# num = int(input("Enter any No: "))
# print(f'prime number : {check_Palim(num)}')






# # .......encryption aand decryption.......
# alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
#              'r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h',
#              'i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# encode_decode = input("Encode: e || decode: d ")
# text = input("Type text: ").lower()
# shift = int(input("How much shift: "))

# shift %= 26

# def encrypt(plain_text, shift_amt):
#     cipher_txt = ""
#     for letter in plain_text:
#         position = alphabets.index(letter)          # return index (particular letter)
#         new_position = position+ shift_amt          # new shifted position
#         cipher_txt += alphabets[new_position]       # new alphabetes
#     print(f'cyper texr is: {cipher_txt}')

# def decrypt(cyper_txt, shift_amt):
#     plain_text = ""
#     for letter in cyper_txt:
#         position = alphabets.index(letter)
#         new_position = position - shift_amt
#         plain_text += alphabets[new_position]
#     print(f"Plain text: {plain_text}")


# if encode_decode == "e":
#     encrypt(plain_text=text, shift_amt=shift)
# else:
#     decrypt(cyper_txt=text, shift_amt=shift)

#.........or...................

# def caeser(start_text, shift_amt, cipher_direction):
#     end_txt = ""
#     if(cipher_direction == 'd'):
#         shift_amt *= -1
#     for letter in start_text:
#         position = alphabets.index(letter)
#         new_position = position + shift_amt
#         end_txt += alphabets[new_position]
#     print(f'{cipher_direction}d msg is: {end_txt}')

# caeser(start_text=text, shift_amt=shift, cipher_direction=encode_decode)







# #  multiple return statement.........

# def is_leap(y):
#     if y%4==0:
#         if y%100==0:
#             if y%400==0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
    
# def total_days(y, m):
#     m_days = [31,28,31,30,31,30,31,31,30,31,30,31]
#     if(is_leap(y) and m == 2):          # true && 2 -> fabuarary only
#         return 29
#     return m_days[m-1]                  


# y = int(input("Enter year : "))
# m = int((input("Enter month: ")))
# d = total_days(y,m)
# print(d)







# # function and dictionary...........calculator........

# def add(a,b):
#     return a+b

# def subtract(a,b):
#     return a-b

# def multiply(a,b):
#     return a*b

# def divide(a,b):
#     return a/b

# opera = {"+":add, "-":subtract, "*":multiply, "/":divide}           #dictionary

# # func = opera["*"]
# # print(func(3,6))

# shou_conti = True

# while shou_conti:
#     val1 = int(input("Enter 1st no: "))
#     val2 = int(input("Enter 2nd no: "))

#     operation = input("choose operator: ")
#     calculat = opera[operation]
#     ans = calculat(val1, val2)                  # <-<-<- important line....

#     print(f"{val1} {operation} {val2} = {ans}")

#     if input(f"Type 'y' to continue or type 'n' to exit: ") == 'y':
#         shou_conti = True
#     else:
#         shou_conti = False




# # guess what is the random number..........

# from random import randint,random
# num = randint(1,100)
# chance = 5
# flag = True

# while flag:
#     guess = int(input(f"{chance} Guess the number.."))
#     if num < guess:
#         print("guess num is too high. guess again")
#         chance -= 1
#         if chance == 0:
#             print(f"Chance Over, You lose, number is: {num}")
#             flag = False
#     elif num > guess:
#         print("guess number is too low guess again")
#         chance -= 1
#         if(chance == 0):
#             print(f"Chance Over, You lose, number is: {num}")
#             flag = False
#     else:
#         print(f"You Won, number is: {num}")
#         flag = False



    