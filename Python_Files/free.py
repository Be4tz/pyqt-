import json
# # # # # class Company:
# # # # #     class Employee:
# # # # #         def __init__(self, name, position):
# # # # #             self.name = name
# # # # #             self.position = position
# # # # #         def get_details(self):
# # # # #             return f"{self.name} {self.position}"

# # # # #     def __init__(self , company_name):
# # # # #         self.company_name = company_name
# # # # #         self.employees = [] 
# # # # #     def add_employee (self, name, position):
# # # # #         self.name = name
# # # # #         self.position = position
# # # # #         new_employee = self.Employee(name, position)
# # # # #         self.employees.append(new_employee)
# # # # #     def list_employees(self):
# # # # #         return [employee.get_details() for employee in self.employees]
# # # # #     @staticmethod
# # # # #     def is_valid_position(position):
# # # # #         valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
# # # # #         return position in valid_positions
# # # # # p = 0
# # # # # while p<=2:
# # # # #     choice = input("Do you want to enter my company (yes or no): ")
# # # # #     if choice.lower() == "yes":
# # # # #         break
# # # # #     elif choice.lower() == "no":
# # # # #         continue
# # # # #     else:
# # # # #         print("Invalid response, Please enter Yes o")

# # # # class Class:
# # # #     student_count = 0
# # # #     total_avg_gpa_os = 0
# # # #     @classmethod
# # # #     def get_num_of_student(cls):
# # # #         return cls.student_count
# # # # class Students(Class):
# # # #     def __init__(self, name, gpa: float):
# # # #         self.name = name
# # # #         self.gpa = gpa
# # # #     def get_gpa(self):
# # # #         return f"The gpa of {self.name} is {self.gpa} "
# # # # student_name = input("What is your name: ") 
# # # # student_gpa = input("What is your gpa: ")
# # # # student1 = Students(student_name, student_gpa)
# # # # print(student1.get_gpa())
# # # #AGGREGATION
# # # # class Garage:
# # # #     def __init__(self, name):
# # # #         self.name = name
# # # #         self.cars = []
# # # #     def add_cars(self, car):
# # # #         self.cars.append(car)
# # # #         u = print(f"The {car.color} {car.name} has been added to the garage")
# # # #         return u
# # # #     def drive_car(self , other):
# # # #         if other in self.cars:
# # # #              self.car.remove(other)
# # # #         if other not in self.cars:
# # # #             print(f"The {other.color} {other.name} is not in {self.name}")
# # # #     def list_cars(self):
# # # #         print(f"The cars in {garage.name} are:")
# # # #         for car in self.cars:
# # # #             print(f"     The {car.color} {car.name}")
# # # #         u = print("That's all")
# # # #         return u
# # # # class Car:
# # # #     def  __init__(self, name, color):
# # # #         self.name = name
# # # #         self.color = color

# # # # garage = Garage("Dave's Garage")
# # # # car1 = Car("Mustang", "Matte")
# # # # car2 = Car("Nissan GTR", "Red")
# # # # car3 = Car("Nissan GTR", "Red")
# # # # garage.add_cars(car1)
# # # # garage.add_cars(car2)
# # # # garage.drive_car(car3)
# # # # garage.list_cars()


# # # # class Student:
# # # #     nost = 0
# # # #     def __init__(self, name, age):
# # # #         self.name = name
# # # #         self.age = age
# # # #         nost += 1 

# # # # class Teacher:
# # # #     def __init__(self, teacher_name):
# # # #         self.teacher_name = teacher_name

# # # # class Class:
# # # #     def __init__(self, name, nott):
# # # #         self.name_of_school = name
# # # #         self.name_of_teach = Teacher(nott)

# # # #     def details_of_class(self):
# # # #         u = print(f"""The name of the class is {self.name_of_school}
# # # #                 The of the teacher is {self.name_of_teach}
# # # # The number of students are {Student.nost}""")
# # # #         return u
# # # # stud1 = Student("dave", 13)
# # # # stud2 = Student("dave", 13)
# # # # class9 = Class("jss3", "Grudowenski")
# # # # class9.details_of_class()

# # # # dic = {
# # # #     "a" : 1,
# # # #     "b" : 2,
# # # #     "c" : 3
# # # # }
# # # # for key in dic:
# # # #     print(f"{dic[key]}", end=",")

# # # # set = [1, 2, 3, 4]
# # # # print(set[0])
# # # # for items in set:
# # # #     print(items, end=" ")
# # # import threading
# # # import time


# # # # while True:
# # # #     choice = input("Do you want to play the game Yes/no: ").lower()
# # # #     if choice == "yes":
# # # #         break
# # # #     elif choice == "no":
# # # #         print("ok")
# # # #     else:
# # # #         print("Invalid response please enter Yes or No")
            

# # # # set = [".....", "....", "...", "..", "."]
# # # # for dot in reversed(set):
# # # #     print(f"loading{dot}")
# # # #     time.sleep(2)

# # # class Company:
# # #     class Employee:
# # #         def __init__(self, name, position):
# # #             self.name = name
# # #             self.position = position
# # #         def get_details(self):
# # #             return f"{self.name} {self.position}"

# # #     def __init__(self , company_name):
# # #         self.company_name = company_name
# # #         self.employees = [] 
# # #     def add_employee (self, name, position):
# # #         self.name = name
# # #         self.position = position
# # #         new_employee = self.Employee(name, position)
# # #         self.employees.append(new_employee)
# # #         d = print(f"you have been added as an employee at {self.company_name}")
# # #         return d
# # #     def list_employees(self):
# # #         return [employee.get_details() for employee in self.employees]
   
        
    

# # #     def __getitem__(self, key):
# # #         if key.lower() == "add":
# # #             name = input("Enter your name: ")
# # #             while True:
# # #                 a_p = ["manager", "cook", "cleaner"]
# # #                 position = input("Which position are you looking for: ").lower()
# # #                 if position in a_p:
# # #                     company.add_employee(name, position)
                    
# # #                     break
# # #                 else:
# # #                     print("The position available are Manager, Cook, Cleaner. Choose wisely")
# # #                     continue
                
# # #         else:
# # #             print("You have entered the wrong key")
# # #         u = print("Ok")
# # #         return u


            

# # # company = Company("Rewod Tech")
# # # print(company.company_name)
# # # key1 = input("Enter your key: ")
# # # print(company[key1])
# # # class School:
# # #     count = 0
# # #     totalgpa = 0

# # #     def __init__(self, name_of_school):
# # #         self.name_of_school = name_of_school
# # #         self.students = []
# # #     def enroll_student(self, name, surname, gpa):
# # #         new_student = self.Student(name, surname, gpa)
# # #         self.students.append(new_student)
# # #         u = print(f"You have succesfully Enrolled {self.name} in {self.name_of_school}")
# # #         return u
# # #     def list_students(self):
# # #         for stud in self.students:
# # #             print(f"Name: {self.name}, Surname: {self.surname}, GPA: {self.gpa}")

# # # class Student:
# # #     def __init__(self, name, surname, gpa):
# # #         self.name = name
# # #         self.gpa = gpa
# # #         self.surname = surname
   
# # # school = School("Dave Comprehensive School")
# # # school.enroll_student("d", "s", 4.66)
# # # school.list_students()
    
# # # def evaluate(question):
# # #     try:
# # #         result = eval(question)
# # #         return result
# # #     except Exception as e :
# # #         print(f"Error: {e}")
# # # print("This is a calculator")
# # # while True:
# # #     user = input("> ").strip()
# # #     print(f"{user} = {evaluate(user)}")

# # # text = "   Hello, World!   "
# # # print(text.strip())  # "Hello, World!"
# # # print(text.strip(" H!"))  # "ello, World"
# # # while True:
# # #     password = input("> ")
# # #     if password.isdigit():
# # #         print("Your password must be alpha numeric ")
# # #     elif password.isalpha():
# # #         print("Your password must be alpha numeric ")
# # #     else:
# # #         print("Great! Password")
# # #         break

# # # 



# class Mainwindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         # self.setWindowTitle("Py game")
#         # self.setGeometry(500, 250, 1000, 1000)
#         # self.setWindowIcon(QIcon(r"C:\Users\USER\Documents\python_class\Python_Files\porsche-911-carrera-rsr-1973-4k-8l.jpg"))
#         # label = QLabel("Welcome", self)
#         # label.setFont(QFont("Arial", 30))
#         # label.setGeometry(0, 4, self.width(), self.height())
#         # label.setStyleSheet("color : blue;"
#         #                     "background-color : white;"
#         #                     "font-weight : bold;"
#         #                     "text-decoration : underline")
#         # # label.setAlignment(Qt.AlignmentFlag())
#         # label.setAlignment(Qt.AlignmentFlag.AlignTop)
        
#         # central_widget = QWidget()
#         # self.setCentralWidget(central_widget)
#         # label2 = QLabel("1")   
#         # label2.setFont(QFont("30"))     
#         # label3 = QLabel("3") 
#         # label4 = QLabel("13")
#         # label2.setGeometry(0, 0, 20, 56)  
#         # label3.setGeometry(0, 0, 20, 56) 
#         # label4.setGeometry(0, 0, 20, 56) 
#         # label2.setStyleSheet("background-color: yellow;") 
#         # label3.setStyleSheet("background-color: green;") 
#         # label4.setStyleSheet("background-color: blue;") 
#         # vbox = QVBoxLayout()
#         # vbox.addWidget(label2)
#         # vbox.addWidget(label3)
#         # vbox.addWidget(label4)
#         # central_widget.setLayout(vbox)
#         self.setWindowTitle("My first GUI")
#         self.setWindowIcon(QIcon(r"C:\Users\USER\Documents\python_class\Python_Files\porsche-911-carrera-rsr-1973-4k-8l.jpg"))
#         self.setGeometry(500, 60, 1000, 800)   
#         self.label = QLabel("Welcome", self)
#         self.ui()
#         timer = QTimer()
#         timer.singleShot(5000, self.label_hide)
#     def ui(self):
#         window = QWidget()
#         self.setCentralWidget(window)
#         self.label.setStyleSheet("font-size : 25px;"
#                                  "font-family: calibre;")
#         hbox = QHBoxLayout()
#         hbox.addWidget(self.label)
#         hbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         window.setLayout(hbox)
#     def initUI(self):
#         window2 = QWidget()
#         self.setCentralWidget(window2)
#         self.label2 = QLabel("How are you?", self)
#         self.label2.setStyleSheet("font-size : 25px;")
#         self.but1 = QPushButton("Fine", self)
#         self.but2 = QPushButton("Not Fine", self)
#         self.but1.setObjectName("b1")
#         self.but2.setObjectName("b2")
#         self.setStyleSheet("""
# QPushButton{
                           
#                            border : 3px solid black;
#                            font-size : 17px;
#                            margin : 14px;
#                            padding : 15px 30px
#                            }
# QPushButton:hover{
#                            border-radius : 10px;
#                            background-color : green}
# """)
#         vbox = QVBoxLayout()
#         hbox = QHBoxLayout()
#         hbox2 = QHBoxLayout()
#         hbox.addWidget(self.label2)
#         hbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         vbox.addLayout(hbox)
#         hbox2.addWidget(self.but1)
#         hbox2.addWidget(self.but2)
#         vbox.addLayout(hbox2)
#         window2.setLayout(vbox)
#     def label_hide(self):
#         self.label.hide()
#         self.initUI()

# def main():
#     app = QApplication(sys.argv)
#     window = Mainwindow()
#     window.show()
#     sys.exit(app.exec())

# if __name__ == '__main__':
#     main()




# Activity: "Simple Text Input App"
# Goal: Create a window with a text input field, a button, and a label. When the user types something in the text box and clicks the button, the label will update to display the input.


# class STIA(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.label = QLabel("")
#         self.text_input = QLineEdit()
#         self.text_input.setPlaceholderText("Type name here...")
#         self.text_input.setMaxLength(10)
#         self.b1 = QPushButton("Done")
#         layout = QVBoxLayout()
#         layout.addWidget(self.text_input)
#         layout.addWidget(self.label)
#         layout.addWidget(self.b1)
#         layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         self.setLayout(layout)
#         self.b1.clicked.connect(self.buttun)
#     def buttun(self):
#         ui = self.text_input.text()
#         self.label.setText(f"Hello {ui}")
        
# def main():
#     app = QApplication(sys.argv)
#     window = STIA()
#     window.show()
#     sys.exit(app.exec())

# if __name__ == '__main__':
#     main()





# Goal: Create a window with a label that shows a counter value and two buttons—"Increase" and "Decrease". When the buttons are clicked, the counter value will update accordingly.
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, 
                             QWidget, QVBoxLayout, QHBoxLayout, QGraphicsGridLayout, QPushButton, QLineEdit, QColorDialog, QGridLayout)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QIcon, QFont, QPixmap, QColor


class Counter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic Counter app")
        self.counter = 0
        self.label = QLabel(f"{self.counter}")
        self.b1 = QPushButton("Increase")
        self.b2 = QPushButton("Decrease")
        self.b3 = QPushButton("Reset")
        self.b1.clicked.connect(self.increase)
        self.b2.clicked.connect(self.decrease)
        self.b3.clicked.connect(self.reset_counter)
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        hbox.addWidget(self.b1)
        hbox.addWidget(self.b3)
        hbox.addWidget(self.b2)
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)
        vbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(vbox)
    def increase(self):
        self.counter += 1
        self.label.setText(f"{self.counter}")
    def decrease(self):
        self.counter -= 1
        self.label.setText(f"{self.counter}")
    def reset_counter(self):
        self.counter = 0
        self.label.setText(f"{self.counter}")

def main():
    app = QApplication(sys.argv)
    window = Counter()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()



# Basic Calculator GUI
# Goal: Create a simple calculator with a GUI that has buttons for digits (0-9), basic operations (+, -, *, /), and a display area for the result.


# class Calc(QWidget):
#     def __init__(self):
#         super().__init__() 
#         self.display = QLineEdit()
#         self.display.setReadOnly(True)
#         self.display.setFixedHeight(50)
#         self.vbox = QVBoxLayout()
#         self.gridlayout = QGridLayout()
#         self.buttons = [
#     ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
#     ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
#     ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
#     ('0', 3, 0), ('.', 3, 1), ('+', 3, 2), ('=', 3, 3)
# ]
#         for text, row, column in self.buttons:
#             self.button = QPushButton(text, self)
#             self.gridlayout.addWidget(self.button, row, column)

#         self.vbox.addWidget(self.display)
#         self.vbox.addLayout(self.gridlayout)
#         self.setLayout(self.vbox)

#         self.current_expression = ""
#         for text, row, coloumn in self.buttons:
#             self.button = self.gridlayout.itemAtPosition(row, coloumn).widget()
#             self.button.clicked.connect(self.add_expressiom)
#     def add_expressiom(self):
#         button = self.sender()
#         text = button.text()

#         if text == "=":
#             try:
#                 # Evaluate the expression and display the result
#                 result = str(eval(self.current_expression))
#                 self.display.setText(result)
#                 self.current_expression = result
#             except Exception:
#                 self.display.setText("Syntax Error")
#                 self.current_expression = ""
#         else:
#             self.current_expression += text
#             self.display.setText(self.current_expression)


# def main():
#     app = QApplication(sys.argv)
#     window = Calc()
#     window.show()
#     sys.exit(app.exec())

# if __name__ == '__main__':
#     main()

        
# from importation import subfile
# class Finances:
#     file_path = "finances.json"
#     expenses = []
#     income = []

#     def add_expenses(self):
#         expense = input("Enter your expense: ")
#         try:
#             with open(self.file_path, 'r') as file:
#                 data = json.load(file)
#         except Exception:
#             data = {}
#         if 'expenses' in data and isinstance(data['expenses'], list):
#             self.expenses.append(expense)
#             data['expenses'] = self.expenses
#         else:
#             # If 'expenses' key does not exist or is not a list, initialize it
#             data['expenses'] = self.expenses

#         # Write updated data back to the file
#         with open(self.file_path, 'w') as file:
#             json.dump(data, file, indent=4)

#     def add_income(self):
#         income = 
#         try:
#             # Load existing JSON data
#             with open(self.file_path, 'r') as file:
#                 data = json.load(file)
#         except json.JSONDecodeError:
#             # Handle invalid JSON data or empty file
#             print("Error: JSON data is invalid or file is empty.")
#             data = {}
#         except FileNotFoundError:
#             # Handle case where the file does not exist
#             print("Error: The file does not exist.")
#             data = {}

#         # Check if 'income' key exists and is a list
#         if 'income' in data and isinstance(data['income'], list):
#             data['income'].extend(new_income)
#         else:
#             # If 'income' key does not exist or is not a list, initialize it
#             data['income'] = new_income

#         # Write updated data back to the file
#         with open(self.file_path, 'w') as file:
#             json.dump(data, file, indent=4)

        
        


#     def __getitem__(self, key):
#         if key.lower() == "net profit":
#             self.add_expenses() 
#         else: 
#             print("Invalid key")

# finance = Finances()
# while True:
#     key =  input("> ")
#     if key.lower() == "done":
#         break
#     print(finance[key])

    
