import json
import os

# path of json file
file_path = os.path.join(os.path.dirname(__file__), "data.json")


# load json file
def load_json():
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r") as file:
        data = json.load(file)
        return data


# save json file
def save_json(data):
    with open(file_path, "w") as file:
        json.dump(
            data, file, indent=4
        )  # indent is used to format the json file with indentation for better readability


# add data to json file
def add_task(data):
    task_name = input("Enter task name: ")

    task = {"id": len(data) + 1, "name": task_name, "status": "pending", "done": False}

    data.append(task)
    save_json(data)
    print("Task added successfully!")


# view data from json file
def view_task(data):
    if not data:
        print("No tasks found.")
        return

    for task in data:
        status = "✓" if task["status"] == "done" else "✗"
        print(f"ID: {task['id']}, Task: {task['name']}, Status: {status}")


# mark task as done
def mark_task_done(data):

    task_id = int(input("Enter task ID to mark as done: "))
    for task in data:
        if task["id"] == task_id:
            task["status"] = "done"
            save_json(data)
            print("Task marked as done!")
            return
    print("Task not found.")


# delete task
def delete_task(data):
    task_id = int(input("Enter task ID to delete: "))
    for task in data:
        if task["id"] == task_id:
            data.remove(task)
            save_json(data)
            print("Task deleted successfully!")
            return
    print("Task not found.")


# clear screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# main function
def main():
    tasks = load_json()

    print("\n" * 2)

    print("========== To-Do List CLI 📋 ==========")

    while True:
        print("\n" * 2)

        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        print("\n")

        choice = input("Enter your choice: ")

        clear_screen()  # Clear the screen after each user input for better readability

        if choice == "1":
            print("\n")
            add_task(tasks)
        elif choice == "2":
            print("\n")
            view_task(tasks)
        elif choice == "3":
            print("\n")
            mark_task_done(tasks)
        elif choice == "4":
            print("\n")
            delete_task(tasks)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
