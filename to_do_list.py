class Task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print(" | Title     | Description     | Due Date   | Priority | Status    |")
            for index, task in enumerate(self.tasks, start=1):
                status = "Done" if task.completed else "Not Done"
                print(f" {task.title} | {task.description} | {task.due_date} | {task.priority} | {status})")

    def mark_task_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.completed = True
            print(f"Marked '{task.title}' as completed!")
        else:
            print("Invalid task index.")

    def clear_tasks(self):
        self.tasks = []
        print("All tasks cleared!")

    def delete_first_task(self):
        if self.tasks:
            deleted_task = self.tasks.pop(0)
            print(f"Deleted '{deleted_task.title}' from the list.")
        else:
            print("No tasks to delete.")

def main():
    todo_list = ToDoListManager()

    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Clear All Tasks")
        print("5. Delete First Task")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            priority = input("Enter task priority: ")
            task = Task(title, description, due_date, priority)
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.list_tasks()
        elif choice == '3':
            task_index = int(input("Enter the task index to mark as completed: "))
            todo_list.mark_task_completed(task_index)
        elif choice == '4':
            todo_list.clear_tasks()
        elif choice == '5':
            todo_list.delete_first_task()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()