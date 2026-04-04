import tkinter as tk
from tkinter import messagebox
import json
import os

DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_expense():
    amount = amount_entry.get()
    category = category_var.get()
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
    date_entry.delete(0, tk.END)

def show_expenses():
    data = load_data()
    listbox.delete(0, tk.END)

    for item in data:
        text = f"{item['date']} | {item['category']} | {item['amount']}"
        listbox.insert(tk.END, text)

def show_total():
    data = load_data()
    total = sum(item["amount"] for item in data)
    messagebox.showinfo("Total Expense", f"Total = {total}")

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("400x500")

frame_top = tk.Frame(root)
frame_top.pack(pady=20)

tk.Label(frame_top, text="Amount").pack()
amount_entry = tk.Entry(frame_top)
amount_entry.pack(pady=5)

tk.Label(frame_top, text="Category").pack()

category_var = tk.StringVar()
category_var.set("Select Category")

categories = ["Bills", "Electricity", "Outings", "Grocery", "Extra"]
category_menu = tk.OptionMenu(frame_top, category_var, *categories)
category_menu.pack(pady=5)

tk.Label(frame_top, text="Date").pack()
date_entry = tk.Entry(frame_top)
date_entry.pack(pady=5)

tk.Button(frame_top, text="Add Expense", command=add_expense).pack(pady=10)
tk.Button(frame_top, text="Show Expenses", command=show_expenses).pack(pady=5)
tk.Button(frame_top, text="Show Total", command=show_total).pack(pady=5)

frame_bottom = tk.Frame(root)
frame_bottom.pack(pady=30)

listbox = tk.Listbox(frame_bottom, width=45)
listbox.pack()

root.mainloop()