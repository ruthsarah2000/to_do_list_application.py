class ToDoList:
    def __init__(self):
        self.tasks = [{'title': 'jog', 'status': 'Incomplete'}, 
                      {'title': 'walk the dog', 'status': 'Incomplete'}, 
                      {'title': 'take out the trash', 'status': 'Incomplete'}, 
                      {'title': 'attend PTA meeting', 'status': 'Incomplete'}]

    def add_task(self, title="Incomplete"):
        self.tasks.append({'title': title, 'status': 'Incomplete'})

    def view_tasks(self):
        print("\nTasks in the To-Do List:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task['title']} - {task['status']}")

    def mark_task_complete(self, task_number):
        try:
            index = int(task_number) - 1
            if 0 <= index < len(self.tasks):
                self.tasks[index]['status'] = 'Complete'
                print(f"Task '{self.tasks[index]['title']}' marked as complete.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")

    def delete_task(self, task_number):
        try:
            index = int(task_number) - 1
            if 0 <= index < len(self.tasks):
                del self.tasks[index]
                print("Task deleted successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")

    def run(self):
        print("Welcome to the To-Do List App!")
        while True:
            print("\nMenu:")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Mark a task as complete")
            print("4. Delete a task")
            print("5. Quit")
            choice = input("Enter your choice: ")

            if choice == "1":
                title = input("Enter the title of the task: ")
                self.add_task(title)
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                task_number = input("Enter the number of the task to mark as complete: ")
                self.mark_task_complete(task_number)
            elif choice == "4":
                task_number = input("Enter the number of the task to delete: ")
                self.delete_task(task_number)
            elif choice == "5":
                print("Exiting the To-Do List App. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a number from the menu.")

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()
