# # create class and object...........
# class Student:              # class create (Abstract)
#     pass

# s1 = Student()              # object create
# s1.name = "Pawan"           # external attribute (for object specific)
# s1.id = 12                 
# print(s1.name)

# s2 = Student()
# s2.name = "Konal"
# s2.id = 55
# print(s2.name)





# # call method 2 ways............
# class Circle(object):
#     a = 20                        # class level attributes for all object
#     def fun(self,b):
#         print(self.a + b)

# obj = Circle()          # object/instance create 
# # obj.a = 100          # modify attribute...now change a value 12 -> 99

# b = 10
# # 1st..........
# obj.fun(b)

# # 2nd................. 
# call = obj.fun(b)
# call







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
# print(s1.name)
# s1.id = 99999                                   #  change for only s1 object
# print(s1.date)                                  # default 
# print(s1.id)


# s2=Student("lokesh", 66)
# s2.disp()
# print(s2.date)
# print(s2.id)







# # Constructor.....defalut value attribute......
# class Student:
#     def __init__(self):                        # constuctor....
#         self.date = "12.12.2000"               # default value
    
# s1=Student()
# print(s1.date)                                 # default print






# # Coustructor default value........
# class Student:
#     def __init__(self, name, id, address="Delhi"):
#         self.name = name
#         self.id = id
#         self.address = address
#     def dis(self):
#         print(f"name: {self.name},id: {self.id},address: {self.address}")
#     def findName(self):
#         return self.name
    
# obj = Student("Kamal",23)
# obj.dis()
# obj2 = Student("mal",23,"Utt")
# obj2.dis()
# print(obj2.findName())





# # class method.......should access by class name and can't object properties..
# class Demo:
#     conta = "India"
#     @classmethod
#     def contary(cls):
#         print("Contry name is:",cls.conta)
# obj = Demo()
# obj.contary()
# Demo.contary()




# # static method........should access by class name and object properties.
# class Demo:
#     @staticmethod
#     def contary():
#         print("Contry India")
# obj = Demo()
# obj.contary()
# Demo.contary()





# # class variable
# class Demo:
#     data = []                   # comman for all object(change not for single object)
#     def __init__(self, name):
#         self.name = name
#         Demo.data.append(self.name)
#     def fun(self):
#         return self.name
    
# obj = Demo(11)
# print(obj.fun())
# print(obj.data)

# obj2 = Demo(99)
# print(obj2.fun())
# print(obj.data)






# # ....Inheritance.........

# class Stude:
#     def fun(self):
#         print("parant calss......")

# class Child(Stude):
#     def fun1111(self):
#         print("Child class")

# x = Child()                   # creating obj of child class
# x.fun()
# x.fun1111()






# .......inheritance........super class call......

class Person:
    def __init__(self, name, id=11):
        self.name = name
        self.id = id                    # initial id value is 1
    def dis_parent(self):
        print(f"Parent class. {self.id}")

class Man(Person):
    def __init__(self, na,id,age):
        # Person.__init__(self, nam)                    # or super() (no need to use self) || here call to parant class
        super().__init__(na)
        # self.na = na
        self.id = id
        self.age = age

    def dis_child(self):
        print(f"Child class: {self.id}, {self.name}, {self.age}")          # access perent data

emp = Man("Harry", 101, 34)
emp.dis_parent()        # can access parent function
emp.dis_child()







# #  Polymorphism.....(overloading not suppoted)..(but Overriding supported)....
# # 1...using inheritance
# class Poly:
#     def fun(self, a):
#         print("Poly1 class...",a)

# class PM(Poly):
#     def fun(self, a):               # overriding....
#         print("PM class...",a)
#         super().fun(10)                 # call to perent call by "super()"

# p = PM()
# p.fun(23)


# # # 2....using Duck typing concept
# class Poly:
#     def fun(self, a):
#         a.fun2()                # call method
# class Poly2:
#     def fun2(self):
#         print("Hii")
# class Poly3:
#     def fun2(self):
#         print("Hello")

# p = Poly2()
# q = Poly3()

# obj = Poly()
# obj.fun(p)
# obj.fun(q)










# # Abstaction...........child class should implemented......
# from abc import ABC,abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def eat(self):
#         pass

# class Dog(Animal):
#     def eat(self):
#         print("Dog clss..")

# # a = Animal()           # abstract class can't instantiate
# a = Dog()  
# a.eat()   







# class RBI:                 # abstract class
#     def fun(self):          # abstract function
#         pass
#     def fun2(self):
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






# composition............

# class Engin:
#     def enginDetails(self):
#         print("Print engin details..")
# class Tyre:
#     def tyreDetails(self):
#         print("Print tyre details..")

# class Car:
#     def __init__(self):
#         self.en = Engin()               # create object
#         self.ty = Tyre()
#     def detailes(self):
#         self.en.enginDetails()                  # imp
#         self.ty.tyreDetails()
# obj = Car()
# obj.detailes()






# class A:
#     def __init__(self,b):
#         self.__b = b
    
#     def getName(self):
#         return self.__b
#     def setName(self,b):
#         self.__b = b

# rv = A(22)
# rv.setName(999)
# print(rv.getName())





# help()




# n = int(input("enter: "))

# for i in range(n):
#     for j in range(n):
#         # if i==0 or j==0 or i+j<=n-1 :
#         # if( i+j>=(n-1)/2 and j-i<=(n-1)/2 and i<=(n-1)/2):
#         if i+j>=(n-1) and i>=j:
#             print("#", end="")
#         else:
#             print(" ", end="")
#     print()

# for i in range(n):
#     spaces = n - i - 1
#     print(" " * spaces + "#" * (2 * i + 1))


# def fun(n):
#     for i in range(2, n):
#         if n%i == 0:
#             return False
#     return True
    
# n = int(input("ere: "))
# print(fun(n))
# # print(c)