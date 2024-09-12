from Projects import TodoList

todolist = TodoList()
todolist.begining()
while True: 
    key = input("> ").lower() 
    if key == "done":
        break
    else:
        print(todolist[key])
    