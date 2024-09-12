from abc import ABC, abstractmethod 
import os
# import random
# class Nigeria:
#     population = "8000000000 people"
#     def __init__(self, state, capital):
#         self.state = state
#         self.capital = capital

#     def add_state(self):
#         r = [", Akwa-Ibom",", Adamawa",", Anambra"]
#         po = random.choice(r)
#         self.state += po

#     def change_capital(self):
#         new_capital = input("Enter your new capital: ")
#         self.capital = new_capital
#         print(f"You have now changed the capital of Nigeria to {self.capital} ")

# class Companies(Nigeria):
#     num_of_company = 0
#     num_of_company += 1
#     location = "Abuja"

# nig = Nigeria("Enugu", "Lagos")
# company1 = Companies("Abuja", "Lagos")
# company2 = Companies("Abuja", "Lagos")
# print(Companies.location)
# print(Companies.num_of_company)
# print(Nigeria.population)
# nig.add_state()
# print(nig.capital)
# print(nig.state)

# class Vehicle:
#     def __init__(self, color, name, year_of_manufacture):
#         self.color = color
#         self.name = name
#         self.year_of_manufacture = year_of_manufacture

#     @abstractmethod    
#     def check_grade_of_horsepower(self):
#         pass

# class Sports_car(Vehicle):
#     def __init__(self, color, name, year_of_manufacture, horsepower):
#         super().__init__(color, name, year_of_manufacture)
#         self.horsepower = horsepower
#     def check_grade_of_horsepower(self):
#         print(f"Your {self.color} {self.name}'s horsepower {"is of a Mini sport car. You pick the wrong category please swicth to the Mini_sport_car category" if self.horsepower < 120 else "is in the Sport car category"}")
        
# class Mini_sports_car(Vehicle):
#     def __init__(self, color, name, year_of_manufacture, horsepower):
#         super().__init__(color, name, year_of_manufacture)
#         self.horsepower = horsepower
#     def check_grade_of_horsepower(self):
#         print(f"Your {self.color} {self.name}'s horsepower {"is of a Sport_car. You pick the wrong category please swicth to Sport_car category" if self.horsepower > 120 else "is in the Mini_sport_car category"}")

# car1 = Sports_car("Red", "Benz", 1986, 14)
# car2 = Mini_sports_car("Gold", "Appolo", 1878, 189)
# car1.check_grade_of_horsepower()
# car2.check_grade_of_horsepower()

# class Garage:
#     def __init__(self, name, num_of_cars_in_the_garage):
#         self.name = name
#         self.num_of_cars_in_the_garage = num_of_cars_in_the_garage
#         self.car = []
#     def add_car(self, car):
#         self.car.append(car)
#     def list_of_cars(self):
#         for car in self.car:
#             self.num_of_cars_in_the_garage += 1
#         print(f"There {"are" if self.num_of_cars_in_the_garage > 1 else "is"} {self.num_of_cars_in_the_garage} {"cars" if self.num_of_cars_in_the_garage > 1 else "car"} in the garage")
#         for car in self.car:
#             print(f"The {car.color} {car.name}")  



# class Car:
#     def __init__ (self, color, name):
#         self.color = color
#         self.name = name
# garage = Garage("E.Z.E Garage", 0)
# mycar1 = Car("Matte", "Mustang")
# mycar2 = Car("Blue", "Nissan GTR")
# mycar3 = Car("Grey", "Wolkeswagaon")

# garage.add_car(mycar1)
# garage.add_car(mycar2)
# garage.add_car(mycar3)
 
# garage.list_of_cars()


u = "THe goat"
e = u.split(" ")
print(e)




