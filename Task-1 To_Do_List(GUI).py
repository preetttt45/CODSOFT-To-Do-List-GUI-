import tkinter as tk
from tkinter import messagebox

def update_progress():
    total = task_listbox.size()
    done = sum(1 for i in task_listbox.get(0, tk.END) if i.startswith("✔️"))
    progress_label.config(text=f"Progress: {done}/{total} tasks done")

def add_task():
    task = task_entry.get()
    priority = priority_var.get()
    if task:
        task_listbox.insert(tk.END, f"{task} [{priority}]")
        task_entry.delete(0, tk.END)
        update_progress()
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

def delete_task():
    try:
        selected = task_listbox.curselection()
        task_listbox.delete(selected)
        update_progress()
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete!")

def mark_done():
    try:
        selected = task_listbox.curselection()
        task = task_listbox.get(selected)
        if not task.startswith("✔️"):
            task_listbox.delete(selected)
            task_listbox.insert(tk.END, f"✔️ {task}")
            update_progress()
    except:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done!")

def toggle_theme():
    if root["bg"] == "white":
        root.configure(bg="black")
        title.config(bg="black", fg="white")
        progress_label.config(bg="black", fg="white")
        task_listbox.config(bg="gray20", fg="white", selectbackground="gray")
    else:
        root.configure(bg="white")
        title.config(bg="white", fg="black")
        progress_label.config(bg="white", fg="black")
        task_listbox.config(bg="white", fg="black", selectbackground="lightgray")

root = tk.Tk()
root.title("To-Do List")
root.geometry("450x480")
root.configure(bg="white")

title = tk.Label(root, text="📝 My Smart To-Do List", font=("Helvetica", 16, "bold"), bg="white")
title.pack(pady=10)

task_entry = tk.Entry(root, width=30, font=("Helvetica", 12))
task_entry.pack(pady=10)

priority_var = tk.StringVar(value="Importance")
priority_menu = tk.OptionMenu(root, priority_var, "Most important", "Important", "Not so important")
priority_menu.config(width=10)
priority_menu.pack()

button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=5)

add_btn = tk.Button(button_frame, text="Add Task", width=12, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

delete_btn = tk.Button(button_frame, text="Delete Task", width=12, command=delete_task)
delete_btn.grid(row=0, column=1, padx=5)

done_btn = tk.Button(button_frame, text="Mark Done", width=12, command=mark_done)
done_btn.grid(row=0, column=2, padx=5)

theme_btn = tk.Button(root, text="Toggle Dark Mode", command=toggle_theme)
theme_btn.pack(pady=5)

task_listbox = tk.Listbox(root, width=45, height=10, font=("Helvetica", 12))
task_listbox.pack(pady=10)

progress_label = tk.Label(root, text="Progress: 0/0 tasks done", font=("Arial", 10), bg="white")
progress_label.pack()

update_progress()
root.mainloop()