from app.models import add_task, get_all_tasks, delete_task, update_task

def handle_add_task(name):
    add_task(name)

def handle_show_tasks():
    tasks = get_all_tasks()
    if not tasks:
        return "No tasks available."
    formatted_tasks = "\n".join(
        [f"{task['id']}: {task['name']} - {'✔️' if task['completed'] else '❌'}" for task in tasks]
    )
    return formatted_tasks


def handle_delete_task(task_id):
    try:
        delete_task(task_id)
        return f"Task with ID {task_id} has been deleted."
    except Exception as e:
        return f"Error: {str(e)}"

def handle_mark_task_completed(task_id):
    update_task(task_id, completed=True)
    return f"Task with ID {task_id} has been marked as completed."
