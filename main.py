import tkinter as tk
from tkinter import messagebox
import json
import os

DATA_FILE = "data.json"

# Load data
def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

# Save data
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Add expense
def add_expense():
    amount = amount_entry.get()
    category = category_entry.get()
    date = date_entry.get()

    if amount == "" or category == "" or date == "":
        messagebox.showerror("Error", "All fields required!")
        return

    try:
        amount = float(amount)
    except:
        messagebox.showerror("Error", "Amount must be number!")
        return

    data = load_data()
    data.append({
        "amount": amount,
        "category": category,
        "date": date
    })
    save_data(data)

    messagebox.showinfo("Success", "Expense added!")

    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)

# Show expenses
def show_expenses():
    data = load_data()
    listbox.delete(0, tk.END)

    for item in data:
        text = f"{item['date']} | {item['category']} | {item['amount']}"
        listbox.insert(tk.END, text)

# Show total
def show_total():
    data = load_data()
    total = sum(item["amount"] for item in data)
    messagebox.showinfo("Total Expense", f"Total = {total}")

# UI
root = tk.Tk()
root.title("Expense Tracker")

tk.Label(root, text="Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Category").pack()
category_entry = tk.Entry(root)
category_entry.pack()

tk.Label(root, text="Date").pack()
date_entry = tk.Entry(root)
date_entry.pack()

tk.Button(root, text="Add Expense", command=add_expense).pack()
tk.Button(root, text="Show Expenses", command=show_expenses).pack()
tk.Button(root, text="Show Total", command=show_total).pack()

listbox = tk.Listbox(root, width=50)
listbox.pack()

root.mainloop()