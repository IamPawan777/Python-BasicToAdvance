# #..........access.....override.....new element.......
# name = {1:"pawan", 2:"Apple", 3:"Kavi", 4:5}
# print(name)                     # access as map 

# print(name[2])                  # access values by key........
# print(name.get(2))              # OR...access values by key........

# name[1] = 11111                 # can change / update / override....
# name[5] = 11111                 # new key value created....
# name.update({2:"AAAAAA"})       # OR... update / overide
# print(name)






# #  dict() method to create dictionary............
# dic1 = {"pawan":"bisht", 32:23, True:False}
# print(dic1)

# dic2 = dict(name= "Pawan",  age= "Mohan", )         # '=' operator use key without ""... keyword, number can't use
# print(dic2)







# #...........items().....list-[] of tuples-().....
# name = {1:"pawan", 2:"Apple", 3:"Kavi", 4:5}
# x = name.items()
# print(x)



# #...........keys()........keys of list.
# name = {1:"pawan", 2:"Apple", 3:"Kavi", 4:5}
# x = name.keys()
# print(x)




# # ...........values().......values of list..
# name = {1:"pawan", 2:"Apple", 3:"Kavi", 4:5}
# x = name.values()
# print(x)





# #...........pop().....del.......
# name = {1:"pawan", 2:"Apple", 3:"Kavi", 4:5}
# del name[1]             # ..or..
# x = name.pop(2)         # delete by key
# print(x)            #..pop()  item
# print(name)



# #...........popitem()......last item will be deleted.....
# name = {1:"pawan", 2:"Apple", 3:"Kavi", 4:5}
# name.popitem()
# print(name)





# #...........clear()...........
# name = {1:"pawan", 2:"Apple", 3:"Kavi", 4:5}
# name.clear()
# print(name)




# #...........copy()..........
# name = {1:"pawan", 2:"Apple", 3:"Kavi", 4:5}
# newName = name.copy()
# print(newName)





# #...........get().....access value at perticular key.....
# name = {1:"pawan", 2:"Apple", 3:"Kavi", 4:5}
# x = name.get(3)
# print(x)




# #  ...........setdefault()...(,)is here*...if key value present don't do any thing otherwise new key-value..
# name = {1:"pawan", 2:"Apple", 3:"Kavi", 4:5}
# x = name.setdefault(2,"ON")             #new element created if key not present
# print(name)




# #..........update().....override and add new element...
name = {1:"pawan", 2:"Apple", 3:"Kavi", 4:5}
name.update({2:"ON", 5:99999})             #override or new element created
print(name)

city = {99:33, 44:22, 22:11}
name.update(city)                       
print(name)





# #...........fromkeys()....  create new key-value but value will be same.......
# x = {"k1", "k2", 3}             # keys
# y = "Hari"                      # value
# dictionary = dict.fromkeys(x,y)
# print(dictionary)






# # nested dictionary........
# student_scores = {"pawan": 77, "Harry": 12, "Radha": 98, "Bawana": 51,}

# student_grade = {}

# for i in student_scores:               # 'i' is str
#     score = student_scores[i]           # change to int 'score' is int
#     if score > 90:
#         student_grade[i] = "A+"
#     elif score > 70:
#         student_grade[i] = "A"
#     elif score > 60:
#         student_grade[i] = "B"
#     elif score > 50:
#         student_grade[i] = "C"
#     else:
#         student_grade[i] = "Fail"

# print(student_grade)





# #  nesting.........
# std = {
#     "ram": {"sub": ["hindi", "englisd", "maths",]},
#     "SLIET": {
#         "name": {
#             "Pawan": {"marks": [12,45,67], "age": 12},   
#             "Radha": {"marks": [33,11], "age": 12}  
#         } 
#     },
#     "MMMUT": {
#         "name": {
#             "Harry": {"Marks": [3,6,12,], "age": 23},
#             "Om": {"Marks": [4,1,45], "age": 22},
#         }
#     }
# }




# #......append dictionary from function...

# std_details = [
#     {
#         "name": "Ganesh",
#         "marks": [12,23,34,12],
#     },
#     {
#         "name": "Omprakash",
#         "marks": [33,11,77,99],
#     },
# ]

# def add_fun(name, marks):
#     new_std = {}                    # 1st
#     new_std["name"] = name           # 2nd
#     new_std["marks"] = marks
#     std_details.append(new_std)        # 3rd

# add_fun("payal", [22,545,999])          # from here
# print(std_details)













