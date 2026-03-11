# Simple Student Calculator with Greeting

import tkinter as tk
from tkinter import messagebox

# -------- Functions --------

def greet():
    name = entry_name.get()
    if name == "":
        messagebox.showwarning("Warning", "Please enter your name!")
    else:
        label_greet.config(text="Hello " + name + " ")

def add_numbers():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 + num2
        label_result.config(text="Result: " + str(result))
    except:
        messagebox.showerror("Error", "Please enter valid numbers!")

def subtract_numbers():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 - num2
        label_result.config(text="Result: " + str(result))
    except:
        messagebox.showerror("Error", "Please enter valid numbers!")

# -------- Main Window --------

root = tk.Tk()
root.title("Student Calculator App")
root.geometry("400x400")
root.config(bg="lightblue")

# -------- Name Section --------

tk.Label(root, text="Enter Your Name:", bg="lightblue").pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

tk.Button(root, text="Greet Me", command=greet).pack(pady=5)

label_greet = tk.Label(root, text="", bg="lightblue", font=("Arial", 12))
label_greet.pack(pady=10)

# -------- Calculator Section --------

tk.Label(root, text="Enter First Number:", bg="lightblue").pack(pady=5)
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

tk.Label(root, text="Enter Second Number:", bg="lightblue").pack(pady=5)
entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

tk.Button(root, text="Add", command=add_numbers).pack(pady=5)
tk.Button(root, text="Subtract", command=subtract_numbers).pack(pady=5)

label_result = tk.Label(root, text="Result: ", bg="lightblue", font=("Arial", 12))
label_result.pack(pady=20)

root.mainloop()