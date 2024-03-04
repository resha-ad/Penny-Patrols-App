# Function to retrieve user data from the database
from tkinter import *
from tkinter import messagebox
import sqlite3
temporary_data = {}
import threading
import json

#to change page
def report():
    root.destroy()
    import report

#create expense table
def create_expense_table():
    conn = sqlite3.connect('expense_tracker.db')
    c = conn.cursor()
    
    c.execute("DELETE FROM expenses") #old values are deleted and table is empty

    c.execute('''CREATE TABLE IF NOT EXISTS expenses
                 (id INTEGER PRIMARY KEY, expense REAL, expense_type TEXT)''')
    conn.commit()
    conn.close()

#add expense values in the database
def add_expense():
    income= entry_income.get()
    expense = entry_expense.get()
    expense_type = var_expense_type.get()

    if not all([expense, expense_type]):
        messagebox.showerror("Error", "All fields are required")
        return
    else:
        try:
            expense = float(expense)
        except ValueError:
            messagebox.showerror("Error", "Expense amount must be a number")
            return
        try:
            income = float(income)
        except ValueError:
            messagebox.showerror("Error", "Income amount must be a number")
            return
        else:
            conn = sqlite3.connect('expense_tracker.db')
            c = conn.cursor()
            c.execute("INSERT INTO expenses (expense, expense_type) VALUES (?, ?)",
                      (expense, expense_type))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Expense added successfully")

#delete expense value from database
def delete_expense():
    expense_id = entry_delete_expense_id.get()

    conn = sqlite3.connect('expense_tracker.db')
    c = conn.cursor()
    c.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Expense deleted successfully")

#calculates total saving, expenses and income
def calculate_totals():
    conn = sqlite3.connect('expense_tracker.db')
    c = conn.cursor()

    # Total Expense
    c.execute("SELECT SUM(expense) FROM expenses")
    total_expense = c.fetchone()[0]
    if total_expense is None:
        total_expense = 0

# Calculate Savings
    try:
        income = float(entry_income.get())
    except ValueError:
        messagebox.showerror("Error", "Income amount must be a number")
        return
    
    savings = income - total_expense
    balance = savings

# Display totals in GUI
    label_total_expense.config(text="Total Expense: $" + str(total_expense))
    if savings < 0:
        label_savings.config(text="Savings: 0")
    else:
        label_savings.config(text="Savings: $" + str(savings))

# Total Expense by Type
    c.execute("SELECT expense_type, SUM(expense) FROM expenses GROUP BY expense_type")
    total_expense_by_type = c.fetchall()
    data = {
        "total_expense": total_expense,
        "savings": savings,
        "balance": balance,
        "income" : income
    }
#saves above data in json
    with open('totals.json', 'w') as outfile:
        json.dump(data, outfile)

    conn.close()


# Create main window
root = Tk()
root.title("Add Income and Expense")
root.config(bg="#82a67d")
root.maxsize(width=760,height=410)
root.minsize(width=760,height=410)

# Create database table
create_expense_table()

# Frames
income_frame = Frame(root, bg="white", padx=20, pady=20)
income_frame.grid(row=1, column=2, padx=20, pady=30)

expense_frame = Frame(root, bg="white", padx=20, pady=20)
expense_frame.grid(row=1, column=3, padx=20, pady=30)

totals_frame = Frame(root, bg="white", padx=20, pady=20)
totals_frame.grid(row=1, column=4, padx=20, pady=30)


# Add Income Widgets
label_income_title = Label(income_frame, text="Total Income", bg="white")
label_income_title.grid(row=0, column=1, padx=5, pady=5)
entry_income = Entry(income_frame)
entry_income.grid(row=1, column=1, padx=5, pady=5)


# Add Expense Widgets
label_expense = Label(expense_frame, text="Expense:", bg="white")
label_expense.grid(row=0, column=0, padx=5, pady=5)
entry_expense = Entry(expense_frame)
entry_expense.grid(row=0, column=1, padx=5, pady=5)

label_expense_type = Label(expense_frame, text="Expense Type:", bg="white")
label_expense_type.grid(row=1, column=0, padx=5, pady=5)
var_expense_type = StringVar()
expense_type_options = ["Essentials", "Entertainment", "Food", "Transportation", "Other"]
expense_type_dropdown = OptionMenu(expense_frame, var_expense_type, *expense_type_options)
expense_type_dropdown.grid(row=1, column=1, padx=5, pady=5)

button_add = Button(expense_frame, text="Add Expense", command=add_expense)
button_add.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Delete Expense Widgets
label_delete_expense_id = Label(expense_frame, text="Expense ID to Delete:",bg="white")
label_delete_expense_id.grid(row=3, column=0, padx=5, pady=5)
entry_delete_expense_id = Entry(expense_frame)
entry_delete_expense_id.grid(row=3, column=1, padx=5, pady=5)

button_delete = Button(expense_frame, text="Delete Expense", command=delete_expense)
button_delete.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Display Totals Widgets
button_calculate_totals = Button(totals_frame, text="Calculate Totals", command=calculate_totals)
button_calculate_totals.pack(pady=5)

label_total_expense = Label(totals_frame, text="Total Expense: $0",bg="white")
label_total_expense.pack(pady=5)

label_savings = Label(totals_frame, text="Savings: $0",bg="white")
label_savings.pack(pady=5)

report_button = Button(totals_frame,text="View Report",bg="white",command=report)
report_button.pack(pady=5)

root.mainloop()
