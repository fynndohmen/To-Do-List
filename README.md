To-Do List Application

This is a simple To-Do List application built with Python and Tkinter. The app allows users to manage tasks by adding, deleting, and marking tasks as completed. Tasks are saved persistently using a JSON file for storage.

Features:

    Add new tasks with a single click.
    Mark tasks as completed, which moves them to a separate list.
    Delete tasks from both open and completed task lists.
    Persistent storage of tasks in a JSON file (database.json).

Project Structure

To-Do-List/
│
├── main.py               # Entry point of the application
├── requirements.txt      # Dependencies for the project
├── README.md             # Project documentation
│
├── app/                  # Application logic and GUI components
│   ├── __init__.py       # Initializes the app package
│   ├── views.py          # GUI layout and event handling
│   ├── controllers.py    # Control logic for managing tasks
│   ├── models.py         # Data model and storage handling
│
└── data/
    └── database.json     # JSON file for storing tasks persistently

Installation:
Prerequisites:

Make sure you have the following installed:

    Python 3.10 or later
    pip (Python package manager)
    Tkinter (For GUI)

To install Tkinter on Arch Linux, use the following command:

sudo pacman -S tk

Steps

    Clone the repository:

git clone https://github.com/fynndohmen/To-Do-List.git

cd To-Do-List

Install the required dependencies:

pip install -r requirements.txt

Run the application:

    python main.py

Usage

    Adding a Task:
    Enter a task in the input field and click the "Add task" button. The task will appear in the "Open Tasks" list.

    Marking a Task as Completed:
    Select a task from the "Open Tasks" list and click the "Mark as completed" button. The task will move to the "Completed Tasks" list.

    Deleting a Task:
    Select a task from either the "Open Tasks" or "Completed Tasks" list and click the "Delete task" button. The task will be permanently deleted.

Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.