# name = {22,55,11,99,55}
# print(name)


# list to set..........
# nameList = [2,4,5,6]
# nameSet = set(nameList)             # change into the set
# print(nameList)
# print(nameSet)              




# # unique word........
# nu = "be the change you widh to see in the world"
# nu1 = nu.split()
# s = set(nu1)

# print(s,", ")


set1 = {3,4,5}
set1 += {1,2,3}
print(set1)





# # #........add()....if already value present then not add....otherwise random position
# name = {22,55,11,99,55}
# name.add(99)
# # name[1] = 88          # error index addition not posible
# print(name)




# #........clear()....
# name = {22,55,11,99,55}
# name.clear()
# print(name)





# #........copy()....
# name = {22,55,11,99,55}
# x = name.copy()
# print(name)
# print(x)





#........difference()....different value print which is on 1st set only......
# name1 = {22,66,11,99,55}
# name2 = {22,11,99,2}
# x = name1.difference(name2)
# print(x)




# # .......difference_update().....remove items that exist in both sets.......
# x = {22,66,11,99,55}
# y = {22,11,99,2}
# x.difference_update(y)
# print(x)




# #..discard().. remove()....delete that value...
# x = {22,66,11,99,55}
# x.discard(11)           # element not present no error
# print(x)

# x.remove(22)            # but element not present error comes
# print(x)



# #.......intersection()........common value print..........
# x = {22,66,11,99,55}
# y = {22,11,99,2}
# z = x.intersection(y)
# print(z)




# #......intersection_update()........that are not present in 2nd set removes in 1st set (update 1st list).......
# x = {22,66,11,99,55}
# y = {22,11,99,2}
# x.intersection_update(y)
# print(x)



# # ...isdijoint()........TRUE if both set values are different...
# x = {22,66,11,99,55}
# y = {2,4,6}
# z = x.isdisjoint(y)
# print(z)



# #......issubset()...issuperset().......
# x = {22,11}
# y = {22,66,11,99,55}
# z = x.issubset(y)
# e = x.issuperset(y)
# print(f'{z} \n {e}')



# #.......pop() .........delete random element......
# y = {22,66,11,99,55}
# y.pop()
# print(y)



# #.......remove() .........delete specify element......
# y = {22,66,11,99,55}
# y.remove(22)
# print(y)



# #.......union()......new large set will be created.....
# x = {22,11,3333}
# y = {22,66,11,99,55}
# z = x.union(y)
# print(z)



# # #....update()......updated all element insert at 1st set...get large set.....
# x = {22,66,11,99,55}
# y = {22,666}
# x.update(y)
# print(x)



# # in, &(intersection), union(), issubset(), issuperset()
# x = {2,4,6,7,6}
# y = {22,4,623,723,6}
# z = {2,4}

# print(9 in x)           # boolean check present or not
# print(x & y)            # intersection
# print(x.union(y))       # union of both 
# print(z.issubset(x))    # is z sub-set of x
# print(x.issuperset(z))    # is z super-set of x
