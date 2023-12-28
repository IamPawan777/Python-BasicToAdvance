# 1.....sum of 2 digit no.....
# num = input("Enter 2 digit no only: ")
# first = int(num[0])
# second = int(num[1])
# sum = first + second
# print(sum)
# print("type of num: ",type(sum))                # now sum also is int





# 2.........squre of num........ **-(squre operator)......

# num = int(input("Enter any no: "))
# squre = int(num**2)
# print(squre)





# 3........... calculate life of lives..(fstring).......

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




 



# 5...........Treasure Hunt game..............
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




# # 7......... get random person (random and string)..........
# import random
# inpu = input("Enter person name (with comma and space): - ")
# name = inpu.split(', ')                    # return the list
# # index = random.randint(0, len(name)-1)          # return random index
# # ran_name = name[index]                     # get value from list
#     #..or...
# ran_name = random.choice(name)
# print(f"person is: {ran_name}")




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





# # 10..........sum of even number.........
# sum = 0
# # for x in range(0, 101):
#     # if x%2 == 0:
#   #......or.......
# for x in range(0, 101, 2):
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
import random
letter = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
          'O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbol = ['@','#','$','%','&']
number = ['0','1','2','3','4','5','6','7','8','9']
t_Letter = int(input("Total letter: "))
t_Symbol = int(input("Total symbol: "))
t_Number = int(input("Total number: "))

#......easy...........
# password = ""
# for x in range (0, t_Letter):
#     password += random.choice(letter)
# for x in range (0, t_Symbol):
#     password += random.choice(symbol)
# for x in range (0, t_Number):
#     password += random.choice(number)
# print(f'Password is: {password}')


#....hard........
password_list = []
for x in range (0, t_Letter):
    # password_list += random.choice(letter)
  #.....or.......
    password_list.append(random.choice(letter))
for x in range (0, t_Symbol):
    password_list += random.choice(symbol)
for x in range (0, t_Number):
    password_list += random.choice(number)
# print(f'Password is: {password_list}')

random.shuffle(password_list)

password = ""
for x in password_list:
    password += x
print(f'Password is: {password}')