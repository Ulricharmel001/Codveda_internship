import os
import json
import time

JSON_FILE = "todo_list_data.json"

class ToDoApp:
    def __init__(self):
        self.tasks = self._load_tasks()

    # --- Private methods ---
    def _load_tasks(self):
        if os.path.exists(JSON_FILE):
            with open(JSON_FILE, "r") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []
        return []

    def _save_tasks(self):
        with open(JSON_FILE, "w") as file:
            json.dump(self.tasks, file, indent=4)
        print("\n[INFO] Data saved successfully.")

    def _generate_id(self):
        return 1 if not self.tasks else max(task['id'] for task in self.tasks) + 1

    def _find_task_by_id(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                return task
        return None

    # --- Core functionality ---
    def view_tasks(self, task_list=None):
        task_list = task_list or self.tasks
        print("\n--- YOUR TO-DO LIST ---")
        if not task_list:
            print("No tasks found.")
            return
        for task in sorted(task_list, key=lambda x: x['id']):
            print(f"\nID: {task['id']} | Status: {task['status'].upper()}")
            print(f"  Title: {task['title']}")
            print(f"  Description: {task['description']}")
            print(f"  Due Date: {task['due_date']}")
            print("-" * 25)

    def add_task(self):
        print("\n--- Add a New Task ---")
        title = input("Enter the task title: ")
        description = input("Enter the task description: ")
        due_date = input("Enter the due date (YYYY-MM-DD): ")

        new_task = {
            'id': self._generate_id(),
            'title': title,
            'description': description,
            'due_date': due_date,
            'status': 'pending'
        }

        self.tasks.append(new_task)
        self._save_tasks()
        print(f"\n[SUCCESS] Task '{title}' was added.")

    def edit_task(self):
        self.view_tasks()
        if not self.tasks: return
        try:
            task_id = int(input("\nEnter the ID to edit: "))
            task = self._find_task_by_id(task_id)
            if task:
                print("\nPress Enter to keep current value.")
                title = input(f"New title ({task['title']}): ")
                desc = input(f"New description ({task['description']}): ")
                due_date = input(f"New due date ({task['due_date']}): ")
                if title: task['title'] = title
                if desc: task['description'] = desc
                if due_date: task['due_date'] = due_date
                self._save_tasks()
                print(f"\n[SUCCESS] Task ID {task_id} updated.")
            else:
                print(f"\n[ERROR] Task with ID {task_id} not found.")
        except ValueError:
            print("\n[ERROR] Invalid ID.")

    def delete_task(self):
        self.view_tasks()
        if not self.tasks: return
        try:
            task_id = int(input("\nEnter the ID to delete: "))
            task = self._find_task_by_id(task_id)
            if task:
                self.tasks.remove(task)
                self._save_tasks()
                print(f"\n[SUCCESS] Task ID {task_id} deleted.")
            else:
                print(f"\n[ERROR] Task with ID {task_id} not found.")
        except ValueError:
            print("\n[ERROR] Invalid ID.")

    def mark_as_completed(self):
        self.view_tasks()
        if not self.tasks: return
        try:
            task_id = int(input("\nEnter the ID to mark completed: "))
            task = self._find_task_by_id(task_id)
            if task:
                task['status'] = 'completed'
                self._save_tasks()
                print(f"\n[SUCCESS] Task ID {task_id} completed.")
            else:
                print(f"\n[ERROR] Task with ID {task_id} not found.")
        except ValueError:
            print("\n[ERROR] Invalid ID.")

    def search_tasks(self):
        keyword = input("\nEnter a keyword to search in titles: ").lower()
        results = [t for t in self.tasks if keyword in t['title'].lower()]
        if results:
            print(f"\nFound {len(results)} matching task(s):")
            self.view_tasks(results)
        else:
            print("\nNo matching tasks.")

    def run(self):
        while True:
            print("\n========== TO-DO LIST MENU ==========")
            print("1. View All Tasks\n2. Add New Task\n3. Edit a Task\n4. Delete a Task\n5. Mark Task Completed\n6. Search Task\n7. Exit")
            choice = input("Enter your choice (1-7): ")
            if choice == '1': self.view_tasks()
            elif choice == '2': self.add_task()
            elif choice == '3': self.edit_task()
            elif choice == '4': self.delete_task()
            elif choice == '5': self.mark_as_completed()
            elif choice == '6': self.search_tasks()
            elif choice == '7': 
                print("\nGoodbye!")
                break
            else:
                print("\n[ERROR] Invalid choice.")
            time.sleep(1)

if __name__ == "__main__":
    ToDoApp().run()
