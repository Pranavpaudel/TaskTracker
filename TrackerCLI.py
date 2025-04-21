import json
import os.path

task_collection = []

def load_task(file_name):
    global task_collection
    if not file_name.endswith('.json'):
        file_name += '.json'
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            task_collection = json.load(f)
    else:
        with open(file_name, 'w') as f:
            json.dump([], f)
            print(f"File {file_name} created successfully.")

def save_tasks(file_name):
    if not file_name.endswith('.json'):
        file_name += '.json'
    with open(file_name, 'w') as f:
        json.dump(task_collection, f)

def show_contents():
    for task in task_collection:
        print("{:<10} {:<30} {:<10}".format(task['task_id'], task['task_name'], task['status']))

def print_done_task():
    for task in task_collection:
        if task['status'].lower() == 'done':
            print("{:<10} {:<30} {:<10}".format(task['task_id'], task['task_name'], task['status']))

def print_pending_task():
    for task in task_collection:
        if task['status'].lower() != 'done':
            print("{:<10} {:<30} {:<10}".format(task['task_id'], task['task_name'], task['status']))

while True:
    print("1. Open Task Tracker \n2. Exit program")
    try:
        user_choice = int(input("Enter '1' to open task tracker or '2' to exit the program: "))
    except ValueError:
        print("Enter only numbers ")
        continue

    if user_choice == 1:
        file_name = input("Enter the name of your file: ").lower()
        load_task(file_name)

        while True:
            print("\nTask Tracker Menu:")
            print("1. Add task")
            print("2. Delete task")
            print("3. Mark as done")
            print("4. View all tasks")
            print("5. View done tasks")
            print("6. View pending tasks")
            print("7. Quit")

            try:
                command = int(input("Enter your choice: "))
                if command == 1:
                    task_name = input("Enter the task: ")
                    status = "pending"
                    task_id = len(task_collection) + 1
                    task_collection.append({'task_id': task_id, 'task_name': task_name, 'status': status})
                    save_tasks(file_name)
                    print("Task added. Task ID", task_id)
                elif command == 2:
                    task_id_to_delete = int(input("Enter task Id: "))
                    for task in task_collection:
                        if task['task_id'] == task_id_to_delete:
                            task_collection.remove(task)
                            break
                    save_tasks(file_name)
                elif command == 3:
                    task_id_to_mark = int(input("Enter task Id: "))
                    for task in task_collection:
                        if task['task_id'] == task_id_to_mark:
                            task['status'] = "Done"
                            break
                    save_tasks(file_name)
                elif command == 4:
                    show_contents()
                elif command == 5:
                    print("Completed task:")
                    print_done_task()
                elif command == 6:
                    print("Pending tasks: ")
                    print_pending_task()
                elif command == 7:
                    break
                else:
                    print("Enter numbers between 1 to 7 ")

            except ValueError:
                print("Enter only numbers ")

    elif user_choice == 2:
        break
    else:
        print("Enter only 1 or 2")