def display_menu():
    print("To-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Exit")

def view_todo_list(todo_list):
    if len(todo_list) == 0:
        print("Your To-Do List is empty.")
    else:
        print("Your To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append(task)
    print("Task added to the To-Do List.")

def complete_task(todo_list):
    view_todo_list(todo_list)
    task_index = int(input("Enter the task number to complete: ")) - 1

    if task_index < 0 or task_index >= len(todo_list):
        print("Invalid task number. Try again.")
    else:
        task = todo_list.pop(task_index)
        print(f"Task '{task}' completed and removed from the To-Do List.")

def todo_list_app():
    todo_list = []

    while True:
        display_menu()
        choice = input("Input your choice (1-4): ")

        if choice == '1':
            view_todo_list(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            complete_task(todo_list)
        elif choice == '4':
            print("Thank you for using the To-Do List!")
            break
        else:
            print("Invalid choice. Try again.")

# Start the To-Do List app
todo_list_app()
