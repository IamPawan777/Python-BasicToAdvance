# #..........access.....override.....new element.......
# name = {1:"pawan", 2:"Apple", 3:"Kavi", 4:5}
# print(name)                     # access as map 
# print(name[2])                  # access by key........
# name[1] = 11111                 # can change/override....
# name[5] = 11111                 # new key value created....
# print(name)



# #...........items().....list-[] of tuples-().....
# name = {1:"pawan", 2:"Apple", 3:"Kavi", 4:5}
# x = name.items()
# print(x)



# #...........keys().........
# name = {1:"pawan", 2:"Apple", 3:"Kavi", 4:5}
# x = name.keys()
# print(x)




# # ...........values().........
# name = {1:"pawan", 2:"Apple", 3:"Kavi", 4:5}
# x = name.values()
# print(x)





# #...........pop().........
# name = {1:"pawan", 2:"Apple", 3:"Kavi", 4:5}
# x = name.pop(2)
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





# #...........get()......value at perticular key.....
# name = {1:"pawan", 2:"Apple", 3:"Kavi", 4:5}
# x = name.get(3)
# print(x)




# #  ...........setdefault()...(,)is here*...if key value present don't do any thing otherwise new key-value..
# name = {1:"pawan", 2:"Apple", 3:"Kavi", 4:5}
# x = name.setdefault(2,"ON")             #new element created if key not present
# print(name)




# # #..........update().....override...
# name = {1:"pawan", 2:"Apple", 3:"Kavi", 4:5}
# name.update({2:"ON"})             #new element created
# print(name)





# #...........fromkeys()....  create new key-value but value will be same.......
x = {"k1", "k2", 3}             # keys
y = "Hari"                      # value
dictionary = dict.fromkeys(x,y)
print(dictionary)
















