import tkinter as tk
import tkinter.font as tkFont
from app.controllers import handle_add_task, handle_show_tasks, handle_delete_task, handle_mark_task_completed, get_tasks_for_display
from app.models import load_from_storage

def main():
    """
    Main function to initialize the GUI and load tasks from storage.
    """
    load_from_storage()  # Load tasks from the saved JSON file
    root = tk.Tk()
    root.title("To-Do List")  # Set the window title
    root.geometry("850x1060")  # Set the window size
    root.configure(bg="#F5F5F5")  # Set the background color

    # Define fonts for the entry field and listboxes
    entry_font = tkFont.Font(family="Helvetica", size=14)
    listbox_font = tkFont.Font(family="Helvetica", size=12)

    # Create a frame for the entry field and add button
    frame = tk.Frame(root, bg="#E0E0E0")
    frame.pack(pady=10)

    # Create an entry field for adding tasks
    task_entry = tk.Entry(frame, width=45, bg="#FFFFFF", fg="#000000", font=entry_font)
    task_entry.grid(row=0, column=0, padx=5)

    # Create an "Add task" button
    add_button = tk.Button(frame, text="Add task", bg="#B0BEC5", fg="#000000", command=lambda: add_task(task_entry, open_listbox))
    add_button.grid(row=0, column=1)

    # Label for the open tasks listbox
    open_label = tk.Label(root, text="Open Tasks", bg="#F5F5F5", fg="#000000", font=entry_font)
    open_label.pack(pady=(10, 0))

    # Create a listbox for displaying open tasks
    open_listbox = tk.Listbox(root, width=70, height=15, bg="#FFFFFF", fg="#000000", font=listbox_font)
    open_listbox.pack(pady=10)

    # Label for the completed tasks listbox
    completed_label = tk.Label(root, text="Completed Tasks", bg="#F5F5F5", fg="#000000", font=entry_font)
    completed_label.pack(pady=(10, 0))

    # Create a listbox for displaying completed tasks
    completed_listbox = tk.Listbox(root, width=70, height=13, bg="#FFFFFF", fg="#000000", font=listbox_font)
    completed_listbox.pack(pady=10)

    # Create a frame for the "Mark as completed" and "Delete task" buttons
    button_frame = tk.Frame(root, bg="#E0E0E0")
    button_frame.pack()

    # Create a "Mark as completed" button
    complete_button = tk.Button(button_frame, text="Mark as completed", bg="#B0BEC5", fg="#000000",
                                 command=lambda: mark_task_completed(open_listbox, completed_listbox))
    complete_button.grid(row=0, column=0, padx=5)

    # Create a "Delete task" button
    delete_button = tk.Button(
        button_frame,
        text="Delete task",
        bg="#FFABAB",
        fg="#000000",
        command=lambda: delete_task(open_listbox, completed_listbox)
    )
    delete_button.grid(row=0, column=1, padx=5)

    # Initial refresh to display tasks in the listboxes
    refresh_task_list(open_listbox, completed_listbox)

    root.mainloop()  # Start the main event loop

def refresh_task_list(open_listbox=None, completed_listbox=None):
    """
    Refreshes the content of the open and completed task listboxes.

    Args:
        open_listbox (tk.Listbox, optional): The listbox displaying open tasks.
        completed_listbox (tk.Listbox, optional): The listbox displaying completed tasks.
    """
    global task_id_map
    task_id_map = {}  # Reset the global task ID map

    if open_listbox is not None:
        open_listbox.delete(0, tk.END)  # Clear all items in the open tasks listbox
        names, mapping = get_tasks_for_display(status="open")  # Get open tasks
        task_id_map.update(mapping)  # Update the global map with task names and IDs
        for name in names:
            open_listbox.insert(tk.END, name)  # Add each task name to the open tasks listbox

    if completed_listbox is not None:
        completed_listbox.delete(0, tk.END)  # Clear all items in the completed tasks listbox
        names, mapping = get_tasks_for_display(status="completed")  # Get completed tasks
        task_id_map.update(mapping)  # Update the global map with task names and IDs
        for name in names:
            completed_listbox.insert(tk.END, name)  # Add each task name to the completed tasks listbox

def add_task(entry, open_listbox):
    """
    Handles adding a new task.

    Args:
        entry (tk.Entry): The entry widget containing the task name.
        open_listbox (tk.Listbox): The listbox displaying open tasks.
    """
    task_name = entry.get()  # Get the task name from the entry field
    if task_name.strip():  # Check if the task name is not empty
        handle_add_task(task_name)  # Add the task using the controller
        entry.delete(0, tk.END)  # Clear the entry field
        refresh_task_list(open_listbox, None)  # Refresh the open tasks listbox

def delete_task(open_listbox, completed_listbox):
    """
    Handles deleting a selected task from either listbox.

    Args:
        open_listbox (tk.Listbox): The listbox displaying open tasks.
        completed_listbox (tk.Listbox): The listbox displaying completed tasks.
    """
    try:
        # Check if a task is selected in either listbox
        if open_listbox.curselection():
            selected_name = open_listbox.get(open_listbox.curselection())  # Get the selected task name from open listbox
        elif completed_listbox.curselection():
            selected_name = completed_listbox.get(completed_listbox.curselection())  # Get the selected task name from completed listbox
        else:
            print("No task selected!")
            return

        # Retrieve the task ID using the global task_id_map
        task_id = task_id_map[selected_name]
        handle_delete_task(task_id)  # Delete the task using the controller
        refresh_task_list(open_listbox, completed_listbox)  # Refresh both listboxes
    except Exception as e:
        print(f"Error while deleting task: {e}")

def mark_task_completed(open_listbox, completed_listbox):
    """
    Handles marking a selected task as completed.

    Args:
        open_listbox (tk.Listbox): The listbox displaying open tasks.
        completed_listbox (tk.Listbox): The listbox displaying completed tasks.
    """
    try:
        # Check if a task is selected in the open listbox
        if open_listbox.curselection():
            selected_name = open_listbox.get(open_listbox.curselection())  # Get the selected task name from open listbox
        else:
            print("No task selected!")
            return

        # Retrieve the task ID using the global task_id_map
        task_id = task_id_map[selected_name]
        handle_mark_task_completed(task_id)  # Mark the task as completed using the controller
        refresh_task_list(open_listbox, completed_listbox)  # Refresh both listboxes
    except Exception as e:
        print(f"Error while marking task as completed: {e}")

if __name__ == "__main__":
    main()
