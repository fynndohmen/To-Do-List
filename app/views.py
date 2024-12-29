import tkinter as tk
from app.controllers import handle_add_task, handle_show_tasks, handle_delete_task, handle_mark_task_completed

def main():
    root = tk.Tk()
    root.title("To-Do List")
    root.geometry("610x760")
    root.configure(bg="white")

    frame = tk.Frame(root, bg="white")
    frame.pack(pady=10)

    task_entry = tk.Entry(frame, width=30)
    task_entry.grid(row=0, column=0, padx=5)

    add_button = tk.Button(frame, text="Add task",bg="#DBE1FC", command=lambda: add_task(task_entry, tasks_listbox))
    add_button.grid(row=0, column=1)

    tasks_listbox = tk.Listbox(root, width=50, height=20)
    tasks_listbox.pack(pady=20)

    button_frame = tk.Frame(root, bg="white")
    button_frame.pack()

    delete_button = tk.Button(button_frame, text="Delete task",bg="#FFDDDD", command=lambda: delete_task(tasks_listbox))
    delete_button.grid(row=0, column=0, padx=5)

    complete_button = tk.Button(button_frame, text="Mark as completed", command=lambda: mark_task_completed(tasks_listbox))
    complete_button.grid(row=0, column=1, padx=5)

    refresh_task_list(tasks_listbox)

    root.mainloop()

def refresh_task_list(listbox=None):
    if listbox is not None:
        listbox.delete(0, tk.END)
        tasks = handle_show_tasks()
        for task in tasks.split("\n"):
            listbox.insert(tk.END, task)


def add_task(entry, listbox):
    task_name = entry.get()
    if task_name.strip():  # Prüfen, ob nicht leer
        handle_add_task(task_name)
        entry.delete(0, tk.END)  # Eingabefeld leeren
        refresh_task_list(listbox)

def delete_task(listbox):
    try:
        selected_task = listbox.get(listbox.curselection())
        task_id = int(selected_task.split(":")[0])
        handle_delete_task(task_id)
        refresh_task_list(listbox)
    except IndexError:
        print("No task selected!")

def mark_task_completed(listbox):
    try:
        selected_task = listbox.get(listbox.curselection())
        task_id = int(selected_task.split(":")[0])
        handle_mark_task_completed(task_id)
        refresh_task_list(listbox)
    except IndexError:
        print("No task selected!")

if __name__ == "__main__":
    main()
