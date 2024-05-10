
# def safe_divide(n, d):  
#     try:  
#         ans = n/d               
#         return ans
#     except:
#         print("0 se nhi kar sakte")
#         return None
# n = int(input("Enter numerator: "))
# d = int(input("Enter denominator: "))     
# print(safe_divide(n, d))




# 0-> try-else-finally || not 0-> except-finally

a = int(input("Enter 1st value: "))
b = int(input("Enter 2nd value: "))
try:
    c = a/b
    print(c)
except ZeroDivisionError as e:
    print(e) 
else:                               # if except block not print
    print("else block")   
finally:                            # compolsury print
    print("end")
    



# # user define exception

# class MyExcep(Exception):
#     pass
# a = 12
# if a>10:
#     raise MyExcep("....#*#*# Wrong something here #*#*.....")