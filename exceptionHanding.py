# a = int(input("Enter 1st value: "))
# b = int(input("Enter 2nd value: "))
# try:
#     c = a/b
#     print(c)
# except ZeroDivisionError as e:
#     print(e) 
# else:                               # if except block not print
#     print("else block")   
# finally:                            # compolsury print
#     print("end")
    



# user define exception

class MyExcep(Exception):
    pass
a = 12
if a>10:
    raise MyExcep("....#*#*# Wrong something here #*#*.....")