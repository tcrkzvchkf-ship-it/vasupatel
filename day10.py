# Fie I/O and JSON

# What I will learn
# Reading and writing files, 
# JSON- the most common data format in software, 
# Making my TodoList save and load automatically
 # with open() patten automatically closes the file when done
    # this is also creating a file called "test.txt" in the folder path
    # The next argument "w", "r", "a"
    # " w " --> write(creates file, overwrites if exists)
    # " r " --> reads the file
    # " a " --> append(adds to end without overwriting the file)

    # Also " as f " as you see multiple times, is just a nickname for the file
    # you can use it to call the file with in that with Open
    # f.read() means it will read from that file
    # f is just a convention or short for file. you can call it anything


import json


class TodoList: # This is the blueprint for what the todo list is gonna work like
    def __init__(self): 
        # so this def is using the __initi__ method where it will be called everytime you call TodoList
        self.tasks = [] 
        #this is just calling the tasks!

    def add_task(self, task_name): 
        # Here I am creating a new function where we are adding tasks with self and tasK_name as the parameters
    
        self.tasks.append({"task": task_name, "done": False})

        # this is appending or adding the tasks in this specific format

    def view_tasks(self):
        if len(self.tasks) == 0: #this will count the amount of takss you have
            print("No tasks yet!")
        for index, task in enumerate(self.tasks):
            if task["done"]:
                status = "[x]"
            else:
                status = "[ ]"
            print(f"{index + 1}. {task['task']} - {status}")

    def complete_task(self, index):
        self.tasks [index - 1]["done"] = True

    def delete_task(self, index):
        self.tasks.pop(index- 1)

    def task_count(self):
       return len(self.tasks)
    
    def save(self, filename):
        with open(filename, "w") as f:
            json.dump(self.tasks, f, indent=4)
        print(f"Tasks saved to {filename}")

    def load(self, filename):
        with open(filename, "r") as f:
            self.tasks = json.load(f)
        print(f"Tasks loaded from {filename}")

    

todo = TodoList()
todo.add_task("Buy groceries")
todo.add_task("Call piyu")
todo.add_task("Call mom")
todo.view_tasks()
todo.complete_task(1)
todo.view_tasks()
todo.save("tasks.json")

todo2 = TodoList()
todo2.load("tasks.json")
todo2.view_tasks()

print(f"Total tasks: {todo.task_count()}")

import os

todo = TodoList()

# os.path.exists() checks if the file exists before trying to load it 
# — without this check the app would crash on first run when there's no file yet.

if os.path.exists("tasks.json"):
    todo.load("tasks.json")
else:
    print("starting fresh!")

todo.add_task("new Task")
todo.view_tasks()
todo.save("tasks.json")