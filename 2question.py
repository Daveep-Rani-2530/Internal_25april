class ToDoList:
    def _init_(self):
        self.tasks = []

    def display_menu(self):
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added!")

    def view_tasks(self):
        if self.tasks:
            print("Tasks:")
            for i in range(len(self.tasks)):
                print(f"{i + 1}. {self.tasks[i]}")
        else:
            print("No tasks.")

    def delete_task(self, index):
        try:
            del self.tasks[index - 1]
            print("Task deleted!")
        except IndexError:
            print("Invalid task!")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter choice: ")

            if choice == '1':
                task = input("Enter task: ")
                self.add_task(task)
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                if self.tasks:
                    index = int(input("Enter task number to delete: "))
                    self.delete_task(index)
                else:
                    print("No tasks to delete.")
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice.")


# Usage
to_do = ToDoList()
to_do.run()
