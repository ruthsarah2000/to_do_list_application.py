print("Welcome to the To-Do-List APP!:")
tasks = ['jog', 'walk the dog', 'take out the trash', 'attend PTA meeting',]
def to_do_list():
    while True:
        print("\n MENU")
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Mark a Task as Complete")
        print("4. Delete a Task")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task = input("Enter a new task: ")
            tasks.append(add_task)
            print(f"{add_task} has been added to the to-do list!")
        elif choice == "2":
            print("\nView Tasks: ")
            for task in tasks[:7]:
                print(task)
            if len(task) > 7:
                print(".... loading more!")
        elif choice == "3":
            completed_task = input("Mark a task as complete: ")
            tasks.append(completed_task)
            print(f"{completed_task} has been marked as complete on the to-do list!")
        elif choice == "4":
            delete_task = input("Delete a Task: ")
            tasks.append(delete_task)
            print(f"{delete_task} deleted from the to-do list!")
        elif choice == "5":
            print("Quit")
            break
        else:
            print("Invalid selection, please try again.")
to_do_list()
