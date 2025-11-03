# To-Do List in Python (Console)

tasks = []

def show_menu():
    print("\n----- TO-DO LIST -----")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print("\nYour Tasks:")
        if not tasks:
            print("No tasks yet!")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == '2':
        task = input("Enter new task: ")
        tasks.append(task)
        print(f"Task '{task}' added!")

    elif choice == '3':
        if not tasks:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            task_no = int(input("Enter task number to remove: "))
            if 0 < task_no <= len(tasks):
                removed = tasks.pop(task_no - 1)
                print(f"Task '{removed}' removed!")
            else:
                print("Invalid number.")

    elif choice == '4':
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice! Please try again.")
