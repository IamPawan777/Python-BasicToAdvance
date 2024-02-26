# same as list but not changeble...can change into a LIST

# name = (33,11,77,44,99)
# print(name[1])
# # .... or .......
# # tuple constructor..........
# val = tuple((1,2,3,4,5))
# print(val)


# #........count()........
# name = (33,44,77,44,99)
# print(name.count(44))


# # .........index().....first occurence....if not fount exception...
# name = (33,44,77,44,99)
# print(name.index(44))


#  # .....list()......change into a list
# val = (1,2,3,4,45,5)
# print(val)
# val2 = list(val)
# print(val2)



#..iterate.....
# val = tuple((1,2,3,4,5))
# i = 0
# while i<len(val):
#     print(val[i])
#     i+=1
# else:
#     print('end loop')




# equals a tuple or not
a = (1,2,3)
b = (1,2,8)
ans = a==b
print(ans)