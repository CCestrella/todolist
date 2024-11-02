import customtkinter as ctk
from tkinter import messagebox, Listbox

# Initialize the main app window with appearance and theme settings
ctk.set_appearance_mode("dark")  # Options: "light", "dark", "system"
ctk.set_default_color_theme("dark-blue")  # Options: "blue", "dark-blue"

root = ctk.CTk()
root.title("To-Do List Application")
root.geometry("400x400")

# Lists to store tasks
todos = []
completed = []

# Function to update the task list display
def update_listbox():
    listbox.delete(0, "end")
    for idx, task in enumerate(todos):
        listbox.insert("end", f"{idx + 1}. {task}")

# Function to add a new task
def add_task():
    task = task_entry.get().strip()
    if task:
        todos.append(task)
        update_listbox()
        task_entry.delete(0, "end")
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to mark a task as completed
def complete_task():
    try:
        idx = listbox.curselection()[0]  # Get selected task index
        completed_task = todos.pop(idx)
        completed.append(completed_task)
        update_listbox()
        messagebox.showinfo("Task Completed", f"'{completed_task}' marked as completed.")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

# Function to delete a task
def delete_task():
    try:
        idx = listbox.curselection()[0]  
        deleted_task = todos.pop(idx)
        update_listbox()
        messagebox.showinfo("Task Deleted", f"'{deleted_task}' has been deleted.")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to show a summary of completed tasks
def show_completed_tasks():
    if completed:
        completed_message = "\n".join(f"* {task}" for task in completed)
        messagebox.showinfo("Completed Tasks", f"Tasks completed today:\n\n{completed_message}")
    else:
        messagebox.showinfo("No Completed Tasks", "No tasks have been marked as completed today.")

# Custom Listbox class wrapped in a CTkFrame for rounded corners and modern styling
class RoundedListbox(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.listbox = Listbox(
            self,
            font=("Verdana", 12),
            height=10,
            width=40,
            selectmode="single",
            bg="#333333",  
            fg="white",    
            bd=0,
            highlightthickness=0
        )
        self.listbox.pack(padx=10, pady=10, fill="both", expand=True)

    def delete(self, first, last=None):
        self.listbox.delete(first, last)

    def insert(self, index, *elements):
        self.listbox.insert(index, *elements)

    def curselection(self):
        return self.listbox.curselection()

# Layout for main app window
title_label = ctk.CTkLabel(root, text="To-Do List", font=("Arial", 24, "bold"))
title_label.pack(pady=10)

task_entry = ctk.CTkEntry(root, placeholder_text="Enter a new task", font=("Arial", 14), width=300)
task_entry.pack(pady=5)

add_task_button = ctk.CTkButton(root, text="Add Task", command=add_task)
add_task_button.pack(pady=5)

# Rounded Listbox to display tasks
listbox_frame = RoundedListbox(root, corner_radius=5)
listbox_frame.pack(pady=10)
listbox = listbox_frame.listbox  

# Frame for Complete and Delete buttons
button_frame = ctk.CTkFrame(root)
button_frame.pack(pady=5)

complete_button = ctk.CTkButton(button_frame, text="Complete Task", command=complete_task)
complete_button.grid(row=0, column=0, padx=5)

delete_button = ctk.CTkButton(button_frame, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=1, padx=5)

completed_button = ctk.CTkButton(root, text="Show Completed Tasks", command=show_completed_tasks)
completed_button.pack(pady=10)

# Start the application
root.mainloop()
