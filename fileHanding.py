# # ...... file create by open()........
# fil = open("demo.txt", "w")  


    
# # # .....write().....close().....
# str = "I am Wring on a file..OKK"
# fil = open("demo1.txt", "w")                # open(“file_name”, “permision”)
# fil.write(str)
# print("created file..")
# fil.close()


# # write "with".... and close automatically........
# str = "ababababababab \npopopo p op "
# with open("demo.txt", "w") as f:
#     f.write(str)
#     f.write("Pawan pawan \n bisht")
# print("written")






# # ........read()...........
# fil = open("demo1.txt", "r")
# filCon = fil.read()
# print(filCon)
# print(".......file readed...........")
# fil.close()



# # ...about read method..and automatically close..."with" statement........
# with open("demo1.txt", "r") as file1:
#     # fil = file1.read()                # read all data
#     # print(fil)
    
#     fil = file1.read(4)                # read 4 character from all data
#     print(fil)
#     print(file1.tell())                 # now 4th position...position of file handle pointer
#     fill = file1.read(2)                #  next 2 character after reading 4 character
#     print(fill)

#     print(file1.seek(2))                # 2nd position...re-position file handle pointer

#     # fil = file1.readline()            # read 1st line
#     # print(fil)
#     # fil = file1.readlines()           # read line by line... as a list
#     # print(fil)
#     # fil = file1.readline(20)            # read 20 character from one line
#     # print(fil)
# # print(file1.close)
# # print(fil)




# with open("demo1.txt", "r") as fil:
#     for line in fil:
#         print(line)



# # ....write a list into file.....writelines()..
# li = ["python", "java" "PHP", "C"]               
# fil = open("demo2.txt", "w")
# fil.writelines(li)                             # store as a string
# print("file created")
# fil.close()


# #..... read a list from file......readlines()......
# fil = open("demo2.txt", "r")
# filLi = fil.readlines()
# print(filLi)





# #........ appeand or write the new data/value..............
# s = "Java Developer Download"
# fil = open("demo1.txt", "a")
# fil.write(s)
# print("updated")
# fil.close()




# ........write new data with 'a'......
s =  "java \n Developer"
with open("demo.txt", 'a') as fi:           # automatically.....
    fi.write(s)
print("Write")




# # **********read one line file and write another file..... "with" stmt resposible for automatically close file
# with open("demo1.txt", "r") as readFile:
#     with open("demo.txt", "w") as writeFile:           # create new write
#         for li in readFile:
#             writeFile.write(li)
# print("close file")