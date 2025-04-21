import json
import os.path

# A global list to store tasks
task_collection = []


# Function to load tasks from a JSON file
def load_task(file_name):
    global task_collection
    # Ensure the file has a .json extension
    if not file_name.endswith('.json'):
        file_name += '.json'
    # If the file exists, load the tasks from it
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            task_collection = json.load(f)
    else:
        # If file doesn't exist, create a new one with an empty list
        with open(file_name, 'w') as f:
            json.dump([], f)
            print(f"File {file_name} created successfully.")


# Function to save the current tasks to the JSON file
def save_tasks(file_name):
    if not file_name.endswith('.json'):
        file_name += '.json'
    with open(file_name, 'w') as f:
        json.dump(task_collection, f)


# Function to display all tasks
def show_contents():
    for task in task_collection:
        print("{:<10} {:<30} {:<10}".format(task['task_id'], task['task_name'], task['status']))


# Function to display only completed tasks
def print_done_task():
    for task in task_collection:
        if task['status'].lower() == 'done':
            print("{:<10} {:<30} {:<10}".format(task['task_id'], task['task_name'], task['status']))


# Function to display only pending tasks
def print_pending_task():
    for task in task_collection:
        if task['status'].lower() != 'done':
            print("{:<10} {:<30} {:<10}".format(task['task_id'], task['task_name'], task['status']))


# Main loop for user interaction
while True:
    print("1. Open Task Tracker \n2. Exit program")
    try:
        user_choice = int(input("Enter '1' to open task tracker or '2' to exit the program: "))
    except ValueError:
        print("Enter only numbers ")
        continue

    # If user chooses to open the task tracker
    if user_choice == 1:
        file_name = input("Enter the name of your file: ").lower()
        load_task(file_name)

        # Submenu for task management
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

                # Add a new task
                if command == 1:
                    task_name = input("Enter the task: ")
                    status = "pending"
                    task_id = len(task_collection) + 1
                    task_collection.append({'task_id': task_id, 'task_name': task_name, 'status': status})
                    save_tasks(file_name)
                    print("Task added. Task ID", task_id)

                # Delete a task by ID
                elif command == 2:
                    task_id_to_delete = int(input("Enter task Id: "))
                    for task in task_collection:
                        if task['task_id'] == task_id_to_delete:
                            task_collection.remove(task)
                            break
                    save_tasks(file_name)

                # Mark a task as done
                elif command == 3:
                    task_id_to_mark = int(input("Enter task Id: "))
                    for task in task_collection:
                        if task['task_id'] == task_id_to_mark:
                            task['status'] = "Done"
                            break
                    save_tasks(file_name)

                # View all tasks
                elif command == 4:
                    show_contents()

                # View only done tasks
                elif command == 5:
                    print("Completed task:")
                    print_done_task()

                # View only pending tasks
                elif command == 6:
                    print("Pending tasks: ")
                    print_pending_task()

                # Exit the task tracker menu
                elif command == 7:
                    break

                else:
                    print("Enter numbers between 1 to 7 ")

            except ValueError:
                print("Enter only numbers ")

    # Exit the main program
    elif user_choice == 2:
        break
    else:
        print("Enter only 1 or 2")
