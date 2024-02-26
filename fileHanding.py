# ...... file create by open()........
fil = open("demo.txt", "w")  


    
# # # .....write().....close().....

# str = "I am Wring on a file..OKK"
# fil = open("demo1.txt", "w")                # open(“file_name”, “permision”)
# fil.write(str)
# print("created file..")
# fil.close()



# # ........read()...........

# fil = open("demo1.txt", "r")
# filCon = fil.read()
# print(filCon)




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



#........ appeand the value..............
s = "Java Developer Download"
fil = open("demo1.txt", "a")
fil.write(s)
print("updated")
fil.close()