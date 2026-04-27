import tkinter as tk
from tkinter import messagebox

expenses = []

def add_expense():
    item = entry_item.get()
    amount = entry_amount.get()

    if item and amount:
        expenses.append((item, amount))
        listbox.insert(tk.END, f"{item} - ₹{amount}")
        entry_item.delete(0, tk.END)
        entry_amount.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Fill all fields")

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("400x400")

tk.Label(root, text="Item").pack()
entry_item = tk.Entry(root)
entry_item.pack()

tk.Label(root, text="Amount").pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

tk.Button(root, text="Add Expense", command=add_expense).pack(pady=10)

listbox = tk.Listbox(root, width=50)
listbox.pack()

root.mainloop()
