# same as list but not changeble...can change into a LIST

# name = (33,11,77,44,99)
# # name[1] = 2323              # error bcz of mutable
# print(name[1])
# print(name[1:3]) 
# # .... or .......
# # tuple constructor..........
# val = tuple((1,2,3,4,5))
# print(val)



# #.....nesting.......
# a = (1,(99,66),2,3,4,("Pawan",44,2.2))
# print(a[1])
# print(a[1][0])


# # extend tuple by "+" operator
# a = (1,2,3,4,("Pawan",44,2.2))
# b = a + ("Hello",3)
# print(b)





# # sort tuple..........
# tup = (1,7,0,3,23,30,45,11)
# tup_sort = sorted(tup)
# print(tup_sort)





# #........count()........
# name = (33,44,77,44,99)
# print(name.count(44))         # no of times 44


# # .........index().....first occurence....if not fount exception...
# name = (33,44,77,44,99)
# print(name.index(44))


#  # .....list()......change into a list
# val = (1,2,3,4,45,5)
# print(val)
# val2 = list(val)
# print(val2)



# # add more element......
# val = (1,2,3,4,45,5)
# val2 = val+("hi",2,3.3)
# print(val2)
           

#..iterate.....
# val = tuple((1,2,3,4,5))
# i = 0
# while i<len(val):
#     print(val[i])
#     i+=1
# else:
#     print('end loop')




# # equals a tuple or not
# a = (1,2,3)
# b = (1,2,86)
# ans = a==b
# print(ans)