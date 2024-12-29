import json

tasks = []

def add_task(name):
    global tasks
    task = {
        "id": len(tasks) + 1,
        "name": name,
        "completed": False
    }
    tasks.append(task)

def get_all_tasks():
    return tasks

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]

def update_task(task_id, new_name=None, completed=None):
    for task in tasks:
        if task["id"] == task_id:
            if new_name:
                task["name"] = new_name
            if completed is not None:
                task["completed"] = completed

def save_to_storage(filepath="data/database.json"):
    global tasks
    try:
        with open(filepath, "w") as file:
            json.dump(tasks, file, indent=4)
        print(f"DEBUG: Tasks saved to {filepath}: {tasks}")  # Debug-Ausgabe
    except Exception as e:
        print(f"ERROR: Failed to save tasks: {e}")  # Fehlerausgabe


def load_from_storage(filepath="data/database.json"):
    global tasks
    try:
        with open(filepath, "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
