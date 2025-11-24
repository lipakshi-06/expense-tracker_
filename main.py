import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

DB = "expenses.db"

def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""
       CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT,
            amount REAL,
            category TEXT,
            date TEXT
                )
     """)
    conn.commit()
    conn.close()

def add_expense():
    desc = desc_entry.get().strip()
    amount = amount_entry.get().strip()
    category = category_entry.get().strip()
    date = date_entry.get().strip() or datetime.now().strftime("%Y-%m-%d")

    if not desc or not amount: 
        messagebox.showerror("Error", "description and amount is required!")
        return

    try:
        float(amount)
    except:
        messagebox.showerror("error", "amount should be a number!")
        return
    
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("INSERT INTO expenses (description, amount, category, date) VALUES (?,?,?,?)",
                (desc, amount, category, date))
    conn.commit()
    conn.close()

    desc_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    load_data()

def load_data():
    for row in table.get_children():
        table.delete(row)

    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT * FROM expenses ORDER BY date DESC, id DESC")
    rows = cur.fetchall()
    conn.close()

    total= 0
    cat_sum = {}

    for r in rows:
        table.insert("", tk.END, values=r)

        #fixed type error here - force float conversion
        amount_float = float(r[2])
        total += amount_float
        cat_sum[r[3]] = cat_sum.get(r[3], 0) + amount_float

    text = f"total expenses: ${total:.2f}\n"
    text += "Category-wise:\n" + "\n".join([f"  {c}: ₹{v:.2f}" for c, v in cat_sum.items()])
    summary_label.config(text=text)

def delete_entry():
    sel =  table.selection()
    if not sel:
        messagebox.showwaring("warning", "select any entry to delete!")
        return

    id_ =  table.ite,(sel)["values"][0]
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("DELETE FROM exoenses WHERE id = ?", (id_,))
    conn.commit()
    conn.close()
    load_data()


#...................UI.................#
init_db()

app = tk.Tk()
app.title("expense tracker (python)")

tk.Label(app, text="description").grid(row=0, column=0)
tk.Label(app, text="amount").grid(row=0, column=1)
tk.Label(app, text="category").grid(row=0, column=2)
tk.Label(app, text="date (YYYY-MM-DD)").grid(row=0, column=3)

desc_entry = tk.Entry(app); desc_entry.grid(row=1, column=0)
amount_entry = tk.Entry(app); amount_entry.grid(row=1, column=1)
category_entry = tk.Entry(app); category_entry.grid(row=1, column=2)
date_entry = tk.Entry(app); date_entry.grid(row=1, column=3)

tk.Button(app, text="Add Expense", command=add_expense, bg="lightgreen").grid(row=1, column=4, padx=10)
tk.Button(app, text="delete selected", command=delete_entry, bg="lightblue").grid(row=2, column=4,pady=5)

cols = ("ID", "description", "amount", "category", "date")
table = ttk.Treeview(app, column=cols, show="headings", height=13)
for col in cols:
    table.heading(col, text=col)
    table.column(col, width=120)

table.grid(row=3, column=0, columnspan=5, pady=10)

summary_label = tk.Label(app, text="", justify="left", font=("arial", 11), anchor="w")
summary_label.grid(row=4, column=0, columnspan=5, sticky="w")

load_data()
app.mainloop()




    

     
    
    

    
