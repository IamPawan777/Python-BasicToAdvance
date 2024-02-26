# # create class and object...........
# class Student:              # class create
#     pass

# s1 = Student()              # object create
# s1.name = "Pawan"           
# s1.id = 12
# print(s1.name)

# s2 = Student()
# s2.name = "Konal"
# s2.id = 55
# print(s2.name)




# # Constructor...........
class Student:
    def __init__(self, name, id):              # constuctor......paramenter are here 2
        self.name = name
        self.id = id
        self.date = "12.12.2000"               # default value
    
    def disp(self):                            # method
        print(f"Name is: {self.name}, Id: {self.id}")

s1=Student("Harry", 232)
s1.disp()
print(s1.date)                                  # default print

s2=Student("lokesh", 66)
s2.disp()
print(s2.date)






# # Constructor.....defalut value attribute......
# class Student:
#     def __init__(self):                        # constuctor....
#         self.date = "12.12.2000"               # default value
    
# s1=Student()
# print(s1.date)                                 # default print





# # .......inheritance........super class call......
# class Person:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#     def dis_parent(self):
#         print(f"Parent class. {self.name}")

# class Man(Person):
#     def __init__(self, nam):
#         self.name = nam
#         Person.__init__(self, nam, id)                    # or super()  || here call to parant class

#     def dis_child(self):
#         print(f"Child class: {self.name}")

# emp = Man("Harry")
# emp.dis_parent()
# emp.dis_child()




# class Stude:
#     x = 5

# print(Stude.x)