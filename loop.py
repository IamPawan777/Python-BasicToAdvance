#.............traverse in list.....................
# li = [23, 56, 12, 78, 123, 56]
# for x in li:
#     print(x)




# #.....traverse in string........
# li = "Naveen"
# for x in li:
#     print(x)






# #.............break.................
# li = [11,22,33,44,55,66,77,88,99]
# for x in li:
#     print(x)
#     if x==55:
#         break





# #.............continue.................
# li = [11,22,33,44,55,66,77,88,99]
# for x in li:
#     if x==55:
#         continue
#     print(x)




#..........range..........
# for x in range(5):             # 0 to 4
    # ...or.....
# for x in range(5, 10):            # 5 to 9 
    #...or.....
# for x in range(3, 30, 2):           # 3 to 30 but 2-step
    # print(x)
# for x in range(10, 0, -1):
#     print(x, end=" ")




# enumerate function..........
# li = ['d','f','e','q','k','j']
# for i,val in enumerate(li):
#     print(i, val)



# #......else in for loop....at the end else block executed then loop is finised but break stmt is there else not executed.....
# for x in range(2, 10, 3):
#     print(x)
# else:
#     print("end loop")




# #.......nested for loop.........
# li = [1, 2, 3]
# li2 = ["pawan", 'bisht']
# for x in li:
#     for y in li2:
#         print(x,y)



#.........pass........"for" loop can't be empty but have "for" loop but no content
#.....................to avoid getting error put "pass" in the loop
# li = [3,4]
# for x in li:
#     pass





# # ........while loop........
# i=1
# while i<=10:
#     print(i)
#     if i == 6:
#         break
#     i = i+2



# #........while with else.....after executing the else, the while loop will be terminated........
# i=1
# while i<=10:
#     print(i)
#     i = i+1
# else:
#     print(f'Now i value is {i}')
#     print("now i value is",i)


i = 1
while i<=10:
    print(i, sep=" ")
    i+=1