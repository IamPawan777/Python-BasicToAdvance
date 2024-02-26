# print(dir(list))              # check function......... 


# # ......access.....slicing...
# name = ["pawan", "bisht", "Ravi", 45, 23.23]
# print(name[2])
# print(name[1:4])
# print(name[:20])        # upto last
# print(name[-1])


# # list constructor..........
# val = list((1,2,3,4,5))
# print(val)


# # .....replacing or update.........
# name = ["pawan", "bisht", "Ravi", 45, 23.23]
# name[0] = 22222
# print(name[0])
# name[1:3] = [99, 11]
# print(name)


# # #.......insert().......
# name = ["Pawan", "Harry", "Kavita", "fark"]
# name.insert(1, "RAVI")
# print(name)


# # ....append()......
# name = [12,34,45,67,89]
# name.append(9999)
# print(name)


# # .....clear().........
# name = [12,34,45,67,89]
# name.clear()
# print(name)


# #........copy()..........
# name = [12,34,45,67,89]
# x = name.copy()
# print(x)
# print(name)



# # .........count().........
# name = [12,34,45,89,12]
# x = name.count(12)
# print(x)


# #.........extend().....add list in the end of current list....
# name = ["Pawan", "Harry", "Kavita", "fark"]
# cast = ["Bisht", "Parihar", "Goshwami", "Duplysis"]
# name.extend(cast)
# print(name)



# #.......index().......
# name = ["Pawan", "Harry", "Kavita", "fark"]
# print(name.index("Harry"))



#............pop()... 3 way.. remove by index....
name = ["Pawan", "Harry", "Kavita", "fark", "cerry"]
name.pop()              # last value
print(name)
name.pop(2)             # second value
print(name)
del name[0]             # delete 0th value
print(name)


# #............remove()...  remove by value....
# name = ["Pawan", "Harry", "Kavita", "fark"]
# name.remove("Kavita")
# print(name)


# #............reverse().........
# name = ["Pawan", "Harry", "Kavita", "fark"]
# name.reverse()
# print(name)


# #............sort().........
# name = [45,67,12,454,2]
# name.sort()
# print(name)




# ###########################################################
# #....2-D list.........
# li1 = ["Hari", "Ram", "Krishna", "Bhrama"]
# li2 = ["Rukamani", "Sita", "Radha", "Saraswati", "person"]
# gene = [li1, li2]
# print(gene)
# print(gene[1][3])                           # access 2D list element