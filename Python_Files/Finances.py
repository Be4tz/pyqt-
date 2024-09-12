
import json
import os
file_name = "Finances.json"
# Create a class of name finaces that accepts expenses and income then you store them in a json file then you can view them and you can calculate the net profit

class Finances:
    def __init__(self, filename= file_name):
        self.filename = filename
        self.data = {'expenses' : [], 'incomes' : []}
        self._done = False
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                file.write("")
        else:
            try:
                with open(self.filename, 'r') as firt:
                    r = json.load(firt)
                self.data = r  
            except Exception:
                self.data = {'expenses' : [], 'incomes' : []}
                
    def _save(self):
        with open(self.filename, "w") as f:
            json.dump(self.data, f, indent=4)
    def add_expenses(self):
        while True:
            amount = input("Enter the expense amount: ").strip()
            if not amount.isdigit():
                print("Expenses amount must be all digit")
            else:
                break
        description_of_amount = input("Enter the description: ").strip().capitalize()
        entry = {'amount' : amount, 'description' : description_of_amount}
        self.data['expenses'].append(entry)
        self._save()
    def add_income(self):
        while True:
            amount = input("Enter the income amount: ").strip()
            if not amount.isdigit():
                print("Income amount must be all digit")
            else:
                break
        description_of_amount = input("Enter the description: ").strip().capitalize()
        entry = {'amount' : amount, 'description' : description_of_amount}
        self.data['incomes'].append(entry)
        self._save()
    def clear_record(self):
        if  self.data['expenses'] or self.data['incomes']:
            question = input("Are you sure you want to clear records (Yes/No): ").lower()
            if question == "yes":
                self.data['expenses'].clear()
                self.data['incomes'].clear()
                self._save()
            if question == "no":
                return
        else:
            print("There is nothing to be cleared")
    def view_record(self):
        for key, list in self.data.items():
            print(key.capitalize() + " :")
            if list:
                for entry in list:
                    for keys in entry:
                            print(f"        {keys.capitalize()}: {entry[keys]}")
            else:
                print("     None found")
    def search_and_delete(self):
        lirt = ["expenses", "income"]
        choice = input("Where do you want to delete from (Expenses/Income): ").strip().lower()
        if choice == "expenses":
            search = input("Enter the description of what you want to delete: ").capitalize().strip()
            for dic in self.data['expenses']:
                for key in dic.values():
                    if search == key:
                        self.data['expenses'].remove(dic)
                        self._done = True
                        self._save()
                        print(f"{search} has been deleted")
                        break    
            if self._done == False:
                print("Description not found in Expenses")
        if choice == "income":
            search = input("Enter the description of what you want to delete: ").capitalize().strip()
            for dic in self.data['incomes']:
                for key in dic.values():

                    if search == key:
                        self.data['incomes'].remove(dic)
                        self._save()
                        print(f"{search} has been deleted")
                        break
            if self._done == False:
                print("Description not found in Income")
        if choice not in lirt:
            print("Invalid response")
        

    def calc_net_profit(self):
        if self.data['expenses'] and self.data['incomes']:
            total_expenses = sum(int(item['amount']) for item in self.data['expenses'])
            total_income = sum(int(item['amount']) for item in self.data['incomes'])
            net_profit_or_loss = total_income - total_expenses
            print(f"Your Net{"Profit" if net_profit_or_loss > 0 else "Loss"} is {net_profit_or_loss}")
        else:
            print("You have not added your expenses and income")
    @staticmethod
    def begining():
        print("""
Add expenses : to add expenses
Add income : to add income
SAD : to search and delete something specifically
Clear record : to clear record
View record : to view the record
Calculate : to calculate netprofit or loss""")
    def __getitem__(self, key):
        if key == "add expenses":
            return self.add_expenses()
        if key == "add income":
            return self.add_income()
        if key == "sad":
            return self.search_and_delete()
        if key == "clear record":
            return self.clear_record()
        if key == "view record":
            return self.view_record()
        if key == "calculate":
            return self.calc_net_profit()
        else:
            print("Invalid key")



                
                   
                
                    
    

finan = Finances()
finan.begining()
while True:
    key = input(">> ").lower()
    if key == "done":
        break
    else:
        print(finan[key])