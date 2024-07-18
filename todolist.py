import os

# Global list to store tasks
tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)
    print("Task added successfully!")

# Function to list all tasks
def list_tasks():
    if tasks:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks.")

# Function to update a task
def update_task(index, updated_task):
    if 1 <= index <= len(tasks):
        tasks[index - 1] = updated_task
        print("Task updated successfully!")
    else:
        print("Invalid task index.")

# Function to delete a task
def delete_task(index):
    if 1 <= index <= len(tasks):
        del tasks[index - 1]
        print("Task deleted successfully!")
    else:
        print("Invalid task index.")

# Function to save tasks to a file
def save_tasks(filename):
    with open(filename, 'w') as f:
        for task in tasks:
            f.write(task + '\n')
    print(f"Tasks saved to {filename}.")

# Function to load tasks from a file
def load_tasks(filename):
    global tasks
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            tasks = [line.strip() for line in f.readlines()]
        print(f"Tasks loaded from {filename}.")
    else:
        print(f"File {filename} not found.")

# Main function to run the application
def main():
    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Save Tasks")
        print("6. Load Tasks")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            add_task(task)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            index = int(input("Enter task index to update: "))
            updated_task = input("Enter updated task: ")
            update_task(index, updated_task)
        elif choice == '4':
            index = int(input("Enter task index to delete: "))
            delete_task(index)
        elif choice == '5':
            filename = input("Enter filename to save tasks: ")
            save_tasks(filename)
        elif choice == '6':
            filename = input("Enter filename to load tasks: ")
            load_tasks(filename)
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

# Entry point of the program
if __name__ == "__main__":
    main()
