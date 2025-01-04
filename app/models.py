import json

# Global variable to store tasks and the next unique ID
tasks = []
next_id = 1  # Separate variable to keep track of the next unique ID

def add_task(name):
    """
    Adds a new task to the task list with a unique ID.

    Args:
        name (str): The name of the task to be added.
    """
    global tasks, next_id
    if not tasks:  # If the task list is empty, reset next_id to 1
        next_id = 1
    task = {
        "id": next_id,  # Use the next available unique ID
        "name": name,
        "completed": False
    }
    tasks.append(task)
    next_id += 1  # Increment the ID for the next task

def get_all_tasks():
    """
    Returns the list of all tasks.

    Returns:
        list: List of task dictionaries.
    """
    global tasks
    return tasks

def delete_task(task_id):
    """
    Deletes a task by its unique ID and adjusts the next_id.

    Args:
        task_id (int): The unique ID of the task to be deleted.
    """
    global tasks, next_id
    # Filter out the task with the given ID
    tasks = [task for task in tasks if task["id"] != task_id]
    # Adjust `next_id` based on the remaining tasks
    if tasks:
        next_id = max(task["id"] for task in tasks) + 1  # Set to one more than the max ID
    else:
        next_id = 1  # Reset to 1 if no tasks remain

def update_task(task_id, completed=None):
    """
    Updates a task's name or completion status by its ID.

    Args:
        task_id (int): The unique ID of the task to be updated.
        completed (bool, optional): The new completion status for the task.
    """
    for task in tasks:
        if task["id"] == task_id:
            if completed is not None:
                task["completed"] = completed

def save_to_storage(filepath="data/database.json"):
    """
    Saves the current tasks and the next ID to a JSON file.

    Args:
        filepath (str): Path to the JSON file where tasks are saved.
    """
    global tasks, next_id
    try:
        with open(filepath, "w") as file:
            # Save both tasks and the next available ID to avoid conflicts
            json.dump({"tasks": tasks, "next_id": next_id}, file, indent=4)
    except Exception as e:
        print(f"ERROR: Failed to save tasks: {e}")

def load_from_storage(filepath="data/database.json"):
    """
    Loads tasks and the next ID from a JSON file.

    Args:
        filepath (str): Path to the JSON file from which tasks are loaded.
    """
    global tasks, next_id
    try:
        with open(filepath, "r") as file:
            data = json.load(file)
            # Assume data is always a dictionary
            tasks = data.get("tasks", [])  # Load tasks
            next_id = data.get("next_id", 1)  # Load next_id

            # Reset next_id if the task list is empty
            if not tasks:
                next_id = 1
    except FileNotFoundError:
        tasks = []
        next_id = 1
    except Exception as e:
        print(f"ERROR: Failed to load tasks: {e}")
        tasks = []
        next_id = 1


def get_task_names_and_mapping(status):
    """
    Returns task names for the specified status and a mapping of names to IDs.

    Args:
        status (str): "open" or "completed".

    Returns:
        tuple: (list of task names, dictionary mapping names to IDs)

    Raises:
        ValueError: If the provided status is not "open" or "completed".
    """
    global tasks

    if status == "open":
        filtered_tasks = [task for task in tasks if not task["completed"]]
    elif status == "completed":
        filtered_tasks = [task for task in tasks if task["completed"]]
    else:
        raise ValueError("Invalid status. Expected 'open' or 'completed'.")

    names = [task["name"] for task in filtered_tasks]
    mapping = {task["name"]: task["id"] for task in filtered_tasks}
    return names, mapping

