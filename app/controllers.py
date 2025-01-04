from app.models import add_task, get_all_tasks, delete_task, update_task, save_to_storage, get_task_names_and_mapping

def handle_add_task(name):
    """
    Handles adding a new task.

    Args:
        name (str): The name of the task to be added.

    Actions:
        - Adds the task to the task list.
        - Saves the updated task list to storage.
    """
    add_task(name)
    save_to_storage()

def handle_show_tasks(status=None):
    """
    Prepares tasks for display based on their status.

    Args:
        status (str, optional): "open" or "completed". If None, all tasks are returned.

    Returns:
        str: A formatted string of tasks with their IDs, names, and completion status.

    Actions:
        - Filters tasks based on the provided status.
        - Formats the tasks for display.
    """
    tasks = get_all_tasks()

    # Filter tasks based on their status
    if status == "open":
        tasks = [task for task in tasks if not task["completed"]]
    elif status == "completed":
        tasks = [task for task in tasks if task["completed"]]

    # Format tasks for display
    return "\n".join(
        [f"{task['id']}: {task['name']} - {'✔️' if task['completed'] else '❌'}" for task in tasks]
    )

def handle_delete_task(task_id):
    """
    Handles deleting a task by its ID.

    Args:
        task_id (int): The unique ID of the task to be deleted.

    Returns:
        str: A confirmation message or an error message.

    Actions:
        - Deletes the task from the task list.
        - Saves the updated task list to storage.
    """
    try:
        delete_task(task_id)
        save_to_storage()
        return f"Task with ID {task_id} has been deleted."
    except Exception as e:
        return f"Error: {str(e)}"

def handle_mark_task_completed(task_id):
    """
    Handles marking a task as completed by its ID.

    Args:
        task_id (int): The unique ID of the task to be marked as completed.

    Returns:
        str: A confirmation message.

    Actions:
        - Updates the task's completion status.
        - Saves the updated task list to storage.
    """
    update_task(task_id, completed=True)
    save_to_storage()
    return f"Task with ID {task_id} has been marked as completed."

def get_tasks_for_display(status=None):
    """
    Prepares tasks for display in the GUI.

    Args:
        status (str): "open" or "completed". If None, return all tasks.

    Returns:
        tuple: (list of task names, dictionary mapping names to IDs)

    Actions:
        - Delegates the task filtering and mapping to the model function.
    """
    return get_task_names_and_mapping(status)
