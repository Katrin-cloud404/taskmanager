import json
import os

FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task():
    task = input("Enter task: ")
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print("Task added.")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for i, t in enumerate(tasks, 1):
        status = "✔️" if t["done"] else "❌"
        print(f"[{i}] {t['task']} {status}")

def complete_task():
    tasks = load_tasks()
    view_tasks()
    idx = int(input("Task number to complete: ")) - 1
    if 0 <= idx < len(tasks):
        tasks[idx]["done"] = True
        save_tasks(tasks)
        print("Task marked complete.")

def delete_task():
    tasks = load_tasks()
    view_tasks()
    idx = int(input("Task number to delete: ")) - 1
    if 0 <= idx < len(tasks):
        tasks.pop(idx)
        save_tasks(tasks)
        print("Task deleted.")

def main():
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1": add_task()
        elif choice == "2": view_tasks()
        elif choice == "3": complete_task()
        elif choice == "4": delete_task()
        elif choice == "5": break
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()
