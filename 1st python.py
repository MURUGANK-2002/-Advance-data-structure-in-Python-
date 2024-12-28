import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

def execute_db(query, params=()):
    with sqlite3.connect("students.db") as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        if query.strip().upper().startswith("SELECT"): return cursor.fetchall()

execute_db("CREATE TABLE IF NOT EXISTS students (rollno INTEGER PRIMARY KEY, name TEXT, department TEXT)")

def manage_student(action):
    rollno, name, dept = entry_rollno.get(), entry_name.get(), entry_department.get()
    if action != "delete" and (not rollno or not name or not dept):
        return messagebox.showerror("Error", "All fields are required.")
    try: rollno = int(rollno)
    except ValueError: return messagebox.showerror("Error", "Roll No must be an integer.")
    if action == "add":
        try: execute_db("INSERT INTO students VALUES (?, ?, ?)", (rollno, name, dept))
        except sqlite3.IntegrityError: return messagebox.showerror("Error", "Roll No must be unique.")
    elif action == "update":
        execute_db("UPDATE students SET name=?, department=? WHERE rollno=?", (name, dept, rollno))
    elif action == "delete":
        if not tree.selection(): return messagebox.showerror("Error", "No student selected.")
        execute_db("DELETE FROM students WHERE rollno=?", (tree.item(tree.selection()[0], "values")[0],))
    refresh_tree()

def refresh_tree():
    for row in tree.get_children(): tree.delete(row)
    for row in execute_db("SELECT * FROM students"): tree.insert("", "end", values=row)
    entry_rollno.delete(0, tk.END), entry_name.delete(0, tk.END), entry_department.delete(0, tk.END)

root = tk.Tk(); root.title("Student Management")
tk.Label(root, text="Roll No").grid(row=0, column=0); entry_rollno = tk.Entry(root); entry_rollno.grid(row=0, column=1)
tk.Label(root, text="Name").grid(row=1, column=0); entry_name = tk.Entry(root); entry_name.grid(row=1, column=1)
tk.Label(root, text="Department").grid(row=2, column=0); entry_department = tk.Entry(root); entry_department.grid(row=2, column=1)
tk.Button(root, text="Add", command=lambda: manage_student("add")).grid(row=3, column=0)
tk.Button(root, text="Update", command=lambda: manage_student("update")).grid(row=3, column=1)
tk.Button(root, text="Delete", command=lambda: manage_student("delete")).grid(row=3, column=2)
tree = ttk.Treeview(root, columns=("Roll No", "Name", "Department"), show="headings")
for col in ("Roll No", "Name", "Department"): tree.heading(col, text=col); tree.column(col, width=100)
tree.grid(row=4, column=0, columnspan=3)
refresh_tree(); root.mainloop()
