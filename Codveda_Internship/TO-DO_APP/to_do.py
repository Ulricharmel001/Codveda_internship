import os
import json
import time

JSON_FILE = "todo_list_data.json"

class ToDoApp:
    def __init__(self):
        self.tasks = self.load_tasks()  

    def load_tasks(self):
        """Load tasks from the JSON file."""
        if os.path.exists(JSON_FILE):
            with open(JSON_FILE, "r") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []
        return []

    def save_tasks(self):
        """Save tasks to the JSON file."""
        with open(JSON_FILE, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def generate_id(self):
        """Create a new ID for each task."""
        if not self.tasks:
            return 1
        ids = [task["id"] for task in self.tasks]
        return max(ids) + 1

    def find_task(self, task_id):
        """Find a task by its ID."""
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None

    def view_tasks(self, task_list=None):
        """Show all tasks."""
        if task_list is None:
            task_list = self.tasks

        print("\n--- YOUR TO-DO LIST ---")
        if not task_list:
            print("No tasks found.")
            return

        # Sort manually 
        task_list = sorted(task_list, key=self.sort_by_id)

        for task in task_list:
            print(f"\nID: {task['id']} | STATUS: {task['status'].upper()}")
            print(f"Title: {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Due Date: {task['due_date']}")
            print("-" * 25)

    def sort_by_id(self, task):
        return task["id"]

    def add_task(self):
        print("\n--- ADD NEW TASK ---")
        title = input("Title: ")
        description = input("Description: ")
        due_date = input("Due date (YYYY-MM-DD): ")

        new_task = {
            "id": self.generate_id(),
            "title": title,
            "description": description,
            "due_date": due_date,
            "status": "pending"
        }

        self.tasks.append(new_task)
        self.save_tasks()
        print(f"\nTask '{title}' added successfully!")

    def edit_task(self):
        self.view_tasks()
        if not self.tasks:
            return

        try:
            task_id = int(input("\nEnter the ID to edit: "))
            task = self.find_task(task_id)
            if not task:
                print("Task not found.")
                return

            print("\nPress Enter to keep current value.")
            title = input(f"New title ({task['title']}): ")
            description = input(f"New description ({task['description']}): ")
            due_date = input(f"New due date ({task['due_date']}): ")

            if title:
                task["title"] = title
            if description:
                task["description"] = description
            if due_date:
                task["due_date"] = due_date

            self.save_tasks()
            print(f"\nTask {task_id} updated successfully!")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def delete_task(self):
        self.view_tasks()
        if not self.tasks:
            return

        try:
            task_id = int(input("\nEnter the ID to delete: "))
            task = self.find_task(task_id)
            if task:
                self.tasks.remove(task)
                self.save_tasks()
                print(f"\nTask {task_id} deleted.")
            else:
                print("Task not found.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def mark_as_completed(self):
        self.view_tasks()
        if not self.tasks:
            return

        try:
            task_id = int(input("\nEnter the ID to mark completed: "))
            task = self.find_task(task_id)
            if task:
                task["status"] = "completed"
                self.save_tasks()
                print(f"\nTask {task_id} marked as completed!")
            else:
                print("Task not found.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def search_tasks(self):
        keyword = input("\nEnter a keyword to search: ").lower()
        results = [task for task in self.tasks if keyword in task["title"].lower()]

        if results:
            print(f"\nFound {len(results)} matching task(s):")
            self.view_tasks(results)
        else:
            print("No matching tasks found.")

    def run(self):
        while True:
            print("\n========== TO-DO LIST MENU ==========")
            print("1. View All Tasks")
            print("2. Add Task")
            print("3. Edit Task")
            print("4. Delete Task")
            print("5. Mark as Completed")
            print("6. Search Task")
            print("7. Exit")

            choice = input("Choose an option (1-7): ")

            if choice == "1":
                self.view_tasks()
            elif choice == "2":
                self.add_task()
            elif choice == "3":
                self.edit_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.mark_as_completed()
            elif choice == "6":
                self.search_tasks()
            elif choice == "7":
                print("\nGoodbye!")
                break
            else:
                print("Invalid option.")
            time.sleep(1)


if __name__ == "__main__":
    app = ToDoApp()
    app.run()
