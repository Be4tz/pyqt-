
# class Learners:
#     num_of_learners = 0
#     def __init__ (self, name, age, bc):
#         self.name = name
#         self.age = age
#         self.bc = bc
#         num_of_learners += 1
#     def sitdown(self):
#         if sitdown1 == True:
#             u = print(f"{self.name} is has satdown !")

#         else:
#             u = print(f"{self.name} will sitdown")
#         return u
#     def stand_up(self):
#         if  sitdown1 == False:
#            r = print(f"{self.name} is already standing !")
#         else:
#             r = print(f"{self.name} has stoodup!")
#         return r
           
           

# class Smart(Learners):
#     reading = True
#     def read(self):
#         print(f"{self.name} is already reading")
# sitdown1 = False
# stud1 = Smart("Dave", 14, 149)
# stud2 =Smart("ave", 14, 14)
# print(Learners.num_of_learners)
# import random
# from abc import ABC, abstractmethod
# class Shape:
#     def __init__(self, color):
#         self.color = color

#     @abstractmethod
#     def calc_area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, color, radius):
#         super().__init__(color)
#         self.radius = radius
#     def calc_area(self):
#         r = 22 / 7
#         print(f"The area of the circle is {self.radius * 2 * r }")

# class Rectangle(Shape):
#     def __init__(self, color, width, height):
#         super().__init__(color)
#         self.width = width
#         self.height = height
#     def calc_area(self):
#         print(f"The area of the rectangle is { self.width * self.height}")

# rec = Rectangle("Red", 4, 79)
# cir = Circle("Blue", 33.3)
# cir.calc_area() 
# rec.calc_area()


# def add(x, y):
#     return x + y

# def sub(d, i):
#     return d - i


# def div(r, t):
#     return r / t


# def mul (g, h):
#     return g * h

# while True:
#     num1 = float(input("Enter your first number: "))
#     symbol = input(">")
#     num2 = float(input("Enter your second number: "))
#     if symbol == "+":
#        print(f"{num1} + {num2} = {add(x=num1, y=num2):.2f}")
#        continue

#     elif symbol == "-":
#        print(f"{num1} - {num2} = {sub(d=num1, i=num2):.2f}")
#        continue

#     if symbol == "/":
#        if num1 and num2  > 0:
#            print(f"{num1} / {num2} = {div(r=num1, t=num2):.2f}")
#            continue
#        else: 
#             print("You cannot divide a number by zero")
#             continue
       
#     if symbol == "*" or "x":
#         print(f"{num1} * {num2} = {mul(g=num1, h=num2):.2f}")
#         continue


#     if symbol == "done":
#         break

         
            

