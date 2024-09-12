

#     def bought(self):
#         print(f"You bought your {self.colour} {self.model} in {self.year}")

    
# car1 = Car("Mustang", 1987, "Red", False)
# car1.bought()# class Car:
#     def __init__ (self, model, year, colour, for_sale):
#         self.model = model
#         self.year = year
#         self.colour = colour
#         self.for_sale = for_sale
    
#     def drive(self):
#         print(f"You drive the {self.colour} {self.model}")


# class Student:
#     class_year = 2024
#     num_students = 0

#     def __init__ (self, name, age):
#         self.name = name
#         self.age = age
#         Student.num_students += 1
    

# stud1 = Student(age=20, name="Andrew")
# stud2 = Student(age=20, name="Lucky")
# stud3 = Student(age=20, name="Victor")
# stud4 = Student(age=20, name="Anna")
# stud5 = Student(age=20, name="Jon")
# stud6 = Student(age=20, name="John")
# stud7 = Student(age=20, name="Dave")
# print(stud1.name)
# print(stud6.class_year)
# print(Student.num_students)

# class Mammal:
#     def __init__ (self, name, type_of_animal):
#         self.name = name
#         self.type_of_animal = type_of_animal
# class Dog(Mammal):
#     def eat(self):
#         print(f"{self.name} is eating")
# class Cat(Mammal):
#     def be_annoying(self):
#         print(f"The {self.type_of_animal} is playing")

# dog1 = Dog("Gunter", "dog")
# cat1 = Cat("Sam", "cat")
# dog1.eat()

# Multilevel inheritance
# class Animal:
#     def __init__ (self, name):
#         self.name = name
#     def eat(self):
#         print(f"{self.name} is eating")
#     def sleep(self):
#         print(f"{self.name} is sleeping")
# class Prey(Animal):
#     def flee(self):
#         print(f"{self.name} is fleeing")
# class Predator(Animal):
#     def hunt(self):
#         print(f"{self.name} is hunting")
# class Rabbit(Prey):
#     pass
# class Hawk(Predator):
#     pass
# class Fish(Prey, Predator):
#     pass

# rabbit = Rabbit("him")
# hawk = Hawk("pamko")
# fish = Fish("pamk")

# rabbit.eat()
# hawk.hunt()
# fish.flee()
# fish.hunt()
# print(rabbit.name)

# Abstract class
# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def drive(self):
#         pass
    
#     @abstractmethod
#     def park(self):
#         pass

# #vehicle = Vehicle()
# class Car(Vehicle):
#     def drive(self):
#         print("Your are driving your car")
        
    
#     def park(self):
#         print("Your have parked your car")
        
# car = Car()
# car.drive()


    
# class Car:
#     def __init__ (self, name_of_car, color_of_car):
#         self.name_of_car  = name_of_car
#         self.color_of_car = color_of_car    
#     def drive(self):
#         print(f"You have started driven your {self.color_of_car} {self.name_of_car}")
#     def park(self):
#         print(f"You parked your {self.color_of_car} {self.name_of_car}")

# class Convertible(Car):
#     def con(self):
#         print(f"You have converted your {self.color_of_car} {self.name_of_car} to a boat")

# # class Bulletproof(Car, Convertible):
# #     def bp(self):
# #         print(f"Your {self.color_of_car} {self.name_of_car} car is now bulletproof")
          

# mustang = Convertible("Mustang", "Red")
# print(mustang.drive())
# mustang.con()

#Super function

# class Shape:
#     def __init__(self, color, is_filled):
#         self.color = color
#         self.is_filled = is_filled
#     def describe(self):
#         print(f"it is {self.color} and {"filled" if self.is_filled else "not filled"}")

# class Circle(Shape):
#     def __init__(self, color, is_filled, radius):
#         super().__init__(color, is_filled)
#         self.radius = radius
#     def describe(self):
#         super().describe()
#         print(f"it is a circle with an area of {3.14 * self.radius * self.radius}cm^2")

# class Square(Shape):
#     def __init__(self,color, is_filled, width):
#         super().__init__(color, is_filled)
#         self.width = width
#     def describe(self):
#         super().describe()
#         print(f"it is a Square with an area of {self.width * self.width}cm^2")
        

# class Triangle(Shape):
#     def __init__(self,color, is_filled, width, height):
#         super().__init__(color, is_filled)
#         self.width = width
#         self.height = height
#     def describe(self):
#         super().describe()
#         print(f"it is a Triangle with an area of {self.width * self.width / 2}cm^2")

# circle = Circle("Red", False, 8)
# square = Square("Blue", False, 6)
# triangle = Triangle("Yellow", True, 8, 26)

# circle.describe()
# print(square.width)
# print(triangle.height)
# triangle.describe()
        
#AGGREGATION

# class Library:
#     def __init__(self, name):
#         self.name = name
#         self.books = []
#     def add_books(self, book):
#         self.books.append(book)

#     def list_books(self):
#         return[f"{book.title} by {book.author} " for book in self.books]

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author


# library = Library("Dave's library")

# book1 = Book("Rich Dad Poor Dad", "Rober Kiyosaki")
# book2 = Book("Influence", "Peter Mike")
# book3 = Book("Take Risk", "John Ken")

# library.add_books(book1)
# library.add_books(book2)
# library.add_books(book3)
# print(library.name)
# for boo in library.list_books():
#     print(boo)



# Composition

# class Salary:
#     def __init__(self, pay, bonus):
#         self.pay = pay
#         self.bonus = bonus

#     def annual_salary(self):
#         return (self.pay * 12) + self.bonus

# class Employee:
#     def __init__(self, name, age,  pay, bonus):
#         self.name = name
#         self.age = age
#         self.obj_salary = Salary(pay, bonus)
#     def  total_salary(self):
#         return self.obj_salary.annual_salary()
    
# emp = Employee("Dave", 23, 150008, 10000)

# print(emp.total_salary())

# Nested class

# class Company:
#     class Employee:
#         def __init__(self, name, position):
#             self.name = name
#             self.position = position
#         def get_details(self):
#             return f"{self.name} {self.position}"

#     def __init__(self , company_name):
#         self.company_name = company_name
#         self.employees = [] 
#     def add_employee (self, name, position):
#         self.name = name
#         self.position = position
#         new_employee = self.Employee(name, position)
#         self.employees.append(new_employee)
#     def list_employees(self):
#         return [employee.get_details() for employee in self.employees]

# company = Company("Rewod Tech")
# print(company.company_name)

# company.add_employee("dave", "engineer")
# company.add_employee("luke", "cleaner")
# company.add_employee("evad", "marketer")

# for employee in company.list_employees():
#     print(employee)         

# Static method
# class Employee:
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#     def get_info(self):
#         return f"{self.name}, {self.position}"
    
#     @staticmethod
#     def is_valid_position(position):
#         valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
#         return position in valid_positions
    
# print(Employee.is_valid_position("Cooks"))

# employee1 = Employee("Eugene", "Manager")
# employee2 = Employee("Peter", "Cleaner")
# employee2 = Employee("Dave", "Cashier")

# print(employee1.get_info())


# class Student:
#     count = 0
#     total_gpa = 0
#     def __init__(self, name, gpa: int):
#         self.name = name
#         self.gpa = gpa
#         Student.count += 1
#         Student.total_gpa += gpa

#     def get_info(self):
#         return f"{self.name} {self.gpa}"
    
#     @classmethod
#     def get_count(cls):
#         return f"Total No. of students: {cls.count}"
    
#     @classmethod
#     def get_average_gpa(cls):
#         if cls.count == 0:
#             return 0
#         else:
#             return f"{cls.total_gpa / cls.count:.2f}"

# student1 = Student("Dave", 4.66)
# student2 = Student("David", 4.60)
# student3 = Student("Lucky", 4.69)

        
# print(Student.get_count())
# print(Student.get_average_gpa())

# Magic method
# class Book:
#     def __init__(self, title, author, num_pages):
#         self.title = title
#         self.author = author
#         self.num_pages = num_pages
    
    # def __str__(self):
    #    return f"{self.title} by {self.author}"
    
    # def __eq__(self, other):
    #     return self.titles == other.title and self.author == other.author

    
    # def __lt__(self, other):
    #     return self.num_pages < other.num_pages
    
    # def __gt__(self, other):
    #     return self.num_pages > other.num_pages
    
    # def __add__(self, other):
    #     return f"{self.num_pages + other.num_pages} pages"
    
    # def __contains__(self, keyword):
    #     return keyword in self.title or keyword in self.author
    
    # def __getitem__(self, key):
    #     if key == "title":
    #         return self.title
    #     elif key == "author":
    #         return self.author
    #     elif key == "num_pages":
    #         return self.num_pages
    #     else:
    #         return f"Key '{key}' was not found"
        
# book1 = Book("The Habbit", "K.K Peter", 345)
# book2 = Book("The Mummy", "K.K Dave", 467)
# book3 =  Book("The Kill", "Collins", 876)

# print(book1)
# print("Peter" in book1)
# print(book3['audio'])
# print(book1 + book3)

# Property decorator

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    @property
    def width(self):
        return f"{self._width:.2f}cm"
    
    @property
    def height(self):
        return f"{self._height:.2f}cm" 
    
    # @width.setter
    # def width(self, new_width):
    #     if new_width > 0:
    #         self._width = new_width
    #     else:
    #         print("Width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")

    # @width.deleter
    # def width(self):
    #     del self._width
    #     print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")


rectangle = Rectangle(4, 5)
# rectangle.width = 0
rectangle.height = 1

print(rectangle.height)
del rectangle.height
    
        