class Gargage:
    def __init__(self, owners_name):
        self.owners_name = owners_name
        self.cars = []
    def park_car(self):
        color = input("Enter the color of the car you want to park: ").capitalize()
        name_of_car = input("Enter the name of the car you want to park: ").capitalize()
        car = Car(color=color, type_name=name_of_car)
        self.cars.append(car)
        print("You have parked your car in the garage")
    def remove_car(self):
        name_ocr = input("Enter the name of the car you want to remove: ").capitalize()
        for car in self.cars:
            if name_ocr == car.type_name:
                self.cars.remove(car)
        print(f"You can drive your {name_ocr}")
    def list_of_cars(self):
        pj = 0
        for index, car in enumerate(self.cars, start=1):
            print(f"{index}. {car.color} {car.type_name}")
            pj += 1
        if len(self.cars) < 1:
            print("Your broke man try buying a car")
        else:
            print(f"{"These are" if pj > 1 else "This is" } the {"cars" if pj > 1 else 'car'} in {self.owners_name}'s garage")

    def play_out(self):
        print("""
Park : to park car
View cars : to view cars in the garage
Drive : as the name implies""")
    def __getitem__(self, key):
        if key == "Park":
            return self.park_car()
        if key == "View cars":
            return self.list_of_cars()
        if key == "Drive":
            return self.remove_car()
        else: 
            print(f'{key} not found')
        
class Car:
    def __init__(self, color, type_name):
        self.color = color
        self.type_name = type_name





while True:
    choice = input("Do you want to play the garage game?: ").capitalize()
    if choice == "Yes":
            break
    elif choice  == "No":
        print("Ok")
        continue
    else:
        print("invalid response try again")
own = input("Please input the owner's name: ").capitalize()
gar = Gargage(owners_name=own)
gar.play_out()
while True:
    key = input("> ").capitalize()
    if key == "Done":
        break
    else:
        print(gar[key])




