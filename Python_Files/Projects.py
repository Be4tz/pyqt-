import json
import time
import pygame
import threading


filename = "tasks.json"
FILENAME = "Quiz_question_answers.json"

class Quiz:
    quiz = [     {
        'question': "What is the capital of France?",
        'choices': ['A. Berlin', 'B. Madrid', 'C. Paris', 'D. Rome'],
        'answer': 'C'
    },
    {
        'question': "What is 2 + 2?",
        'choices': ['A. 3', 'B. 4', 'C. 5', 'D. 6'],
        'answer': 'B'
    },
    {
        'question': "What is the largest planet in our solar system?",
        'choices': ['A. Earth', 'B. Mars', 'C. Jupiter', 'D. Saturn'],
        'answer': 'C'
      }]
    with open(FILENAME, "w") as file:
        json.dump(quiz, file)
    @classmethod    
    def save_question(cls, question):
        cls.quiz.append(question)
        with open(FILENAME, "w") as file:
            json.dump(cls.quiz, file)
        print("Done👌")
    def add_question(self):
        password = "123456"
        i = 0
        while i < 3:
            passd = input("Password: ")
            if passd == password:
                print('ok')
                break
            else:
                if i == 0:
                    print(f"Password incorrect!, You have 2 tries remaining ")
                elif i == 1:
                    print("Password incorrect!, You have only 1 try remaining")
                else:
                    pass
            i += 1
        else:
            print("You are not verified")
            return
        new_question = input("Question: ").strip()
        question = new_question.capitalize()
        i = 0
        options = []
        print("Enter the option in this format (A. girl)")
        while True:
            op = input("> ").strip().capitalize()
            i += 1
            if i == 1:
                if op.startswith("A. "):
                    print("Saved as A")
                    options.append(op)
                else:
                    i -= 1
                    print("You're answer must be in this kind of format (A., B., C., D.)")
            if i == 2:
                if op.startswith("B. "):
                    print("Saved as B")
                    options.append(op)
                else:
                    i -= 1
                    print("You're answer must be in this kind of format (A., B., C., D.)")
            if i == 3:
                if op.startswith("C. "):
                    print("Saved as C")
                    options.append(op)
                else:
                    i -= 1
                    print("You're answer must be in this kind of format (A., B., C., D.)")
            if i == 4:
                if op.startswith("D. "):
                    print("Saved as D")
                    options.append(op)
                    break
                else:
                    i -= 1
                    print("You're answer must be in this kind of format (A., B., C., D.)")
        answerclone = input("What is the answer: ")
        answer = answerclone[0].capitalize()
        ques = {
            'question' : question,
            'choices' : options,
            'answer' : answer
        }
        return self.save_question(question=ques)
    @staticmethod
    def play():
        sound = 'my song.mp3'
        pygame.mixer.init()
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(1)
    @staticmethod
    def stop_music():
        pygame.mixer.music.stop()
    @classmethod
    def start(cls):
        with open(FILENAME, 'r') as filer:
            cls.quiz = json.load(filer)
        score = 0
        num_of_question = 0
        for num, q in enumerate(cls.quiz, start=1):
            print(f"{num}. {q['question']}")
            num_of_question += 1
            for option in q['choices']:
                print(option)
            of_answer = input("Enter your answer (A, B, C, D): ")
            check_of_answer = of_answer[0].upper()
            if check_of_answer == q['answer']:
                score += 1
            else:
                pass
        print("Done" ) 
        if score == num_of_question:
            print("Well done you're smart👏😜")
            print(f"""Your score is {score}/{num_of_question}""")
        else:
            print(f"""Your score is {score}/{num_of_question}""")
    @staticmethod
    def begining():
            print("""
Add question : Admin password needed
Start : To start the quiz
""")  
    def __getitem__(self, key):
        if key == "add question":
            return self.add_question()
        if key == "start":
            # cl = threading.Thread(target=self.play)
            # cl.start()
            self.start()
            # self.stop_music()
            # cl.join()
        else:
            print(f"'{key}' not found ")






























class TodoList:
    tasks = {}
    @classmethod
    def search_tasks(cls):
        vali = input("Enter the task you want to search for: ").capitalize().strip()
        if vali in cls.tasks:
            print(f"{vali} was found ")
        else:
            print(f"Key: {vali} was not found" "\n" "Try making a task using the add task")

    @classmethod
    def change_time(cls):
        try:

            with open(filename, "r") as filu:
                data = json.loads(filu.read())
            tn = input("Enter the name of the task: ").strip()
            if tn in data:
                while True:
                    new_time = input("Enter your new time: ")
                    tasktime = new_time.split()
                    try:
                        if ":" not in tasktime:
                            print("Use your brain ")
                        if float(tasktime[0]) > 24 :
                            print("Use your brain ")
                        if float(tasktime[2]) > 60 :
                            print("Use your brain ")
                        else:
                            break
                    except Exception:
                        print("Your time must be in this kind of format (20 : 30)")
                    data[tn] = new_time
            with open(filename, "w") as firt:
                json.dump(data, firt, indent=7)
        except FileNotFoundError:
            print("No task found please add task")


    @classmethod
    def store_task(cls, taskname, time):
        if taskname in cls.tasks:
            print(f"There already a task named {taskname}")
            return
        cls.tasks[taskname] = time
        with open(filename, "w") as fol:
            json.dump(cls.tasks, fol, indent=7)    
        print("You have sucessfully added your task 😎🎉")


    @classmethod
    def add_task(cls):
        is_done = False
        while is_done == False:
            while True:
                taskname = input("Enter the task you want to perform: ").capitalize().strip()
                if taskname.isdigit():
                    print("Taskname must be alphabetical or alphanumerical")
                else:
                    break
            print("Your time must be in this kind of format (20 : 30)")
            while True:
                time = input("Enter the time you want to perform the task : ")
                tasktime = time.split()
                try:
                    if ":" not in tasktime:
                        print("Use your brain ")
                    if float(tasktime[0]) > 24 :
                        print("Use your brain ")
                    if float(tasktime[2]) > 60 :
                        print("Use your brain ")
                    else:
                        break
                except Exception:
                    print("Your time must be in this kind of format (20 : 30)")
            while True:
                choice = input("Are you done Yes/No: ").lower().strip()
                if choice == "yes":
                    is_done = True
                    break
                elif choice == "no":
                    print("You will be taken back to enter a new taskname")
                    break
                else:
                    print("invalid respnse, please enter Yes or No")
        cls.store_task(taskname, time)


    @classmethod
    def view_task(cls):
        try:
            with open(filename) as fila:
                data = json.load(fila)  
            for dict, values in data.items():
                print(f"{dict} by {values}")
        except FileNotFoundError:
            print("No task found please add task")
    @classmethod
    def del_task(cls):
        try:
            with open(filename, "r")as dl:
                tas = json.load(dl)  
            ke = input("Enter the name of the task you want to delete: ").capitalize()
            if ke in tas:
                    del tas[ke]
                    with open(filename, "w") as fiy:
                        f = json.dump(tas, fiy, indent=7)
                    cls.task = f
                    print(f"You have sucessfully deleted '{ke}'")

            else:
                print(f"'{ke}' not found")
        except FileNotFoundError:
            print("You have not added any task ")
            
    @classmethod
    def __getitem__(cls, key):
        if key == "add task":
            return cls.add_task()
        if key == "view tasks":
            return cls.view_task()
        if key == "del task":
            return cls.del_task()
        if key == "search tasks":
            return cls.search_tasks()
        if key == "change time":
            return cls.change_time()

        else:
            print(f"Key:{key} was not found ")
    def begining(self):
       print("""
Add task : to add task
View tasks : to view task
Search tasks : to search for a task
Del task : to delete task
Change time : to update the time of a specific task
""")
       









class file_manager:
    file_explorer = {
        'pictures' : [],
        'video' : [],
        'music' : []
    }
    def input_file(self):
        file_name = input("Enter the name of file you want to save: ").strip().capitalize()
        while True:
            extension = input("Enter the extension: ")
            etbu = [".jpg", ".mp3", ".mp4"]
            if extension[0:5] in etbu:
                print("ok")
                break
            else:
                print("Enter (.jpg, .mp3, .mp4) as the extension")
        file_name += extension
        self.store_file(file=file_name)
    @classmethod
    def store_file(cls, file):
        if file[-4:] == ".jpg":
            cls.file_explorer['pictures'].append(file)
            fi = 'Pictures'
        if file[-4:]  == ".mp3":
            cls.file_explorer['music'].append(file)
            fi = 'Music'
        if file[-4:]  == ".mp4":
            cls.file_explorer['video'].append(file)
            fi = 'Videos'
        print(f"{file} is stored in {fi} ")
    @classmethod
    def search(cls):
        print("""
Videos : to view files in videos
Pictures : to view pictures 
Music : to view the music
Done : to finish""")
        lidt = ["videos", "pictures", "music"]
        while True:
            choice = input("> ").lower()
            if choice == "done":
                break
            if choice == "videos":
                if cls.file_explorer['video']:
                    for files in cls.file_explorer['video']:
                        print(files)
                else:
                    print("There are no files in Videos")
            if choice == "music":
                if cls.file_explorer['music']:
                    for files in cls.file_explorer['music']:
                        print(files)
                else:
                    print("There are no files in Music")
            if choice == "pictures":
                if cls.file_explorer['pictures']:
                    for files in cls.file_explorer['pictures']:
                        print(files)
                else:
                    print("There are no files in Pictures")
            elif choice not in lidt:
                print("invalid response")
            
            

    def del_file(cls):
        lidt = ["videos", "pictures", "music"]
        choice = input("""
What kind of file do you want to delete
Video, Pictures, Music
: """).lower().strip()
        if choice == "video":
            if cls.file_explorer['video']:
                file = input("Enter the name of the file you want to delete: ")
                for files in cls.file_explorer['video']:
                    if file == files:
                        while True:
                            choices = input(f"Are you sure you want to delete {file} (yes/no): ").lower().strip()
                            if choices == "yes":
                                del files
                                break
                            if choices == "no":
                                return
                            else:
                                print("Invalid response")
            else:
                print("There are no files in Videos")
        if choice == "pictures":
            if cls.file_explorer['pictures']:
                file = input("Enter the name of the file you want to delete: ")
                for files in cls.file_explorer['pictures']:
                    if file == files:
                        while True:
                            choices = input(f"Are you sure you want to delete {file} (yes/no): ").lower().strip()
                            if choices == "yes":
                                del files
                                break
                            if choices == "no":
                                return
                            else:
                                print("Invalid response")
            else:
                print("There are no files in Pictures")
        if choice == "music":
            if cls.file_explorer['music']:
                file = input("Enter the name of the file you want to delete: ")
                for files in cls.file_explorer['music']:
                    if file == files:
                        while True:
                            choices = input(f"Are you sure you want to delete {file} (yes/no): ").lower().strip()
                            if choices == "yes":
                                del files
                                break
                            if choices == "no":
                                return
                            else:
                                print("Invalid response")
            else:
                print("There are no files in music")
        elif choice not in lidt:
            print("invalid response")
            
    
    @staticmethod
    def begining():
        print("""
Add file : to add a file
Search : to search
Delete : to delete a file""")

    def __getitem__(self, key):
        if key == "add file":
            return self.input_file()
        if key == "search":
            return self.search()
        if key == "delete":
            return self.del_file()
        else:
            print(f"'{key}' was not found")

