# .....string and Regular Expression......................

import re                           # regular expresion

str = "pawan bisht IS my Name is xusme"
str2 = "HAD"
# str2[0] = 'a'                       # not possible bcz string are imutable
# str3 = "had"
# print(str)
# print(str2==str3)                         # string equal or not
# print("\\")                                 # print " \ "

# print(str[:3])                              # 0 to 2 char. print
# print(str[3:])                                # 0 to last char. print
# print(str[:])                                 # 0 to last
# print(str[-3:-1])                              # -3 to -2 char. print
# print(str[-23:19])                              # -23(or)8 to 28 char. print

# print(str[6:12]+"single")                   # (6 to 11) update string
# print(str[::2])                             # every 2nd character print
# print(str[5:12:2])                          # 5 to 12 index, every 2nd character print    


# print("3"+str2)
# print(3*str2)                                  # 3 times print

# print(str.capitalize())                 # only 1st charater of string is Capitalized and other are small
# print(str.title())                      # every character starts with upper case

# print(str.swapcase())                   # lower to upper and upper to lower

# print(str.casefold())                   # string in lower case
# print(str.lower())
# print(str.islower())                    # TRUE or FALSE
# print(str.upper())                      # string in upper case
# print(str.isupper())                    # TRUE and FALSE


# print(str.count('is'))                  # number of times character is comming

# print(str.endswith('me.'))              # return TRUE & FALSE

# print(str.find("bish"))                # index of the 1st occurence otherwish -1
# print(re.findall("is", str))           # list of the all occurence otherwish []
# print(re.search("is", str))           # tuple range

# print(str.index('bish'))               # index of the 1st occurence otherwise error
# print(str.rfind('pawan'))              # index of the 1st form right side occurence
# print(str.rindex('is'))                # index of the 1st form right side occurence

# print(str.isalnum())                   # return true if all character are number and alphabates
# print(str.isalpha())                   # return true if only alphabates is present
# print(str.isascii())                   # return true if only ascii value
# print(str.isdecimal())                 # return true if only decimal
# print(str.isdigit())                   # return true if only digit are present
# print(str.isnumeric())                 # return true if all character are numeric
# print(str.isprintable())               # return true if only printable

# print(str.isspace())

# print(str.join(str2))                  

# print(str.replace('pawan', str2))        # replace with other string 
# print(str.replace('pawan', "Harry", 2))        # --here 2 represent starting 2 times occurences "pawan" replace "Harry" string form occurences 3rd occrence "pawan" not replace

# print(str.split(" "))                            # return the list....break into the List
# print(str.split("a"))
# print(re.split("i", str))                    # return the list....break into the List

# print(str.lstrip('p'))                   # left side p is trim
# print(str.strip())                       # left and right side spaces are removed

# print(str.startswith("pawan"))           # cheak by which character start the string or not








# regular Expression.........(import re)

# patt = r"abc"
# str = "abcde@ f%gh, hsacdessdsd ,dsde."

# anss = re.search(patt, str)             # search intire string
# ansss = re.match(patt, str)             # search from beginning
# print(anss,"\n",ansss)
# ans2 = re.search("\s",str)              # white space 1st occurences
# print(ans2.start())


# print(re.sub(r"DE", "XXXX", str, flags=re.IGNORECASE))                # replace sub String
# print(re.sub(r"[^a-z]", "7", str))







# # print all vowels
# senta = "pawan bisht IS my Name is xusme"
# for i in senta:
#     if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
#         print(i, end=', ')




# # check palimdrom
# word = input()
# if word == word[::-1]:
#     print("yes palimdrom")
# else:
#     print("No palimdrom")

 