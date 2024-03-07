# # create class and object...........
# class Student:              # class create (Abstract)
#     pass

# s1 = Student()              # object create
# s1.name = "Pawan"           
# s1.id = 12
# print(s1.name)

# s2 = Student()
# s2.name = "Konal"
# s2.id = 55
# print(s2.name)




# # # Constructor...........
# class Student:
#     def __init__(self, name, id):              # constuctor......paramenter are here 2
#         self.name = name
#         self.id = id
#         self.date = "12.12.2000"               # default value
    
#     def disp(self):                            # method
#         print(f"Name is: {self.name}, Id: {self.id}")

# s1=Student("Harry", 232)
# s1.disp()                                       # call member of class by "."
# print(s1.date)                                  # default print

# s2=Student("lokesh", 66)
# s2.disp()
# print(s2.date)






# # Constructor.....defalut value attribute......
# class Student:
#     def __init__(self):                        # constuctor....
#         self.date = "12.12.2000"               # default value
    
# s1=Student()
# print(s1.date)                                 # default print





#....Inheritance.........

# class Stude:
#     def fun(self):
#         print("parant calss......")

# class Child(Stude):
#     def fun1(self):
#         print("Child class")

# x = Child()                   # creating obj of child class
# x.fun()






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





#  Polymorphism.....(overloading not suppoted)..(but Overriding supported)....

# class Poly:
#     def fun(self, a):
#         print("Poly1 class...",a)

# class PM(Poly):
#     def fun(self, a):
#         print("PM class...",a)
#         super().fun(10)                 # call to perent call by "super()"

# p = PM()
# p.fun(23)




# # Abstaction.................

# class RBI:                 # abstract class
#     def fun(self):          # abstract function
#         pass

# class SBI(RBI):                 # child class
#     def fun(self):
#         print("SBI bank")

# class HDFC(RBI):                # child class
#     def fun(self):
#         print("HDFC Bank")


# sbi = SBI()
# hdfc = HDFC()
# sbi.fun()
# hdfc.fun()




# # Encapculation.........("_ _" private, "_" protected).......

# class A:
#     __a = 10                      # private data
#     _b = 555                      # protected data
#     def __init__(self,b):
#         self._b = b
#     def fun(self):
#         print("A class: a value",self.__a, ",& b value",self._b)

# class B(A):
#     def __init__(self,x):
#         super().__init__(x)                      # call to parent class
#     def disp(self):
#         # print("B class",self.__a)              #can't access private data
#         print("B class:",self._b)                 #can access protected data


# rv = B(22)
# rv.fun()
# rv.disp()



help()