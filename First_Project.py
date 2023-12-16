import csv
import os
def todo_display():
    print('ran it')
    try:
        with open('todo.csv') as f:
            todo_reader = csv.reader(f)
            for x, line in enumerate(todo_reader, 1):
                print(f'\n{x}){line[0]}')
    except FileNotFoundError:
        print('File not found.')

def todo_add(user_task):
        todo_task.append(user_task)
        with open('todo.csv','a',newline='') as f:
                writer = csv.writer(f)
                writer.writerow(todo_task)

def todo_del(x):
    i = 1
    with open('todo.csv') as f:
        todo_reader = csv.reader(f)
        todo_task_save = []
        for i, line in enumerate(todo_reader, 1): 
            if i != 1:
                todo_task_save.append(line)
            else:
                print(f'Deleted {line[0]} sucessfully.')

    with open('todo.csv','w',newline='') as f:
        writer = csv.writer(f)
        writer.writerows(todo_task_save)

todo_exists = os.path.exists('todo.csv')
if todo_exists != True:
    with open('todo.csv','w') as f:
        pass

while True: 
    todo_task = []
    user_option = int(input('\n1. Display tasks\n2. Add tasks\n3. Delete tasks\n4. Quit\n'))

    if user_option == 1:
        todo_display()

    elif user_option == 2:

        user_task = input('Enter a todo task:')
        todo_add(user_task)

    elif user_option == 3:
        todo_display()
        user_input = int(input('Enter the index of task you want to delete:'))
        todo_del(user_input)

    elif user_option == 4:
        break
