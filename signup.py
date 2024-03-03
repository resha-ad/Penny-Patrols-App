import sqlite3
from tkinter import *
from tkinter import messagebox

# Function to create the database table
def create_table():
    conn = sqlite3.connect('expense_tracker.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    fullname TEXT NOT NULL,
                    lastname TEXT NOT NULL,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Function to add user to the database
def add_user():
    fullname = fullname_entry.get()
    lastname = lastname_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if fullname == '' or lastname == '' or email == '' or password == '' or confirm_password == '':
        messagebox.showerror("Error", "Please fill in all fields")
    elif not (email.endswith("@gmail.com") or email.endswith("@yahoo.com")):
             messagebox.showerror("Error", "Invalid email address")
    elif len(password)<8:
            messagebox.showerror("Error","Password is less than 8 characters")
    elif password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match")
    else:
        try:
            conn = sqlite3.connect('expense_tracker.db')
            c = conn.cursor()
            c.execute("INSERT INTO users (fullname, lastname, email, password) VALUES (?, ?, ?, ?)",
                    (fullname, lastname, email, password))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "User added successfully!")
        except sqlite3.IntegrityError: #ensures email remains unique
               messagebox.showerror("Error", "Email address already exists!")

# Function to retrieve user data from the database
def retrieve_users():
    conn = sqlite3.connect('expense_tracker.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    conn.close()

    if not rows:
        messagebox.showinfo("Info", "No users found")
    else:
        user_list.delete(0, END)
        for row in rows:
            user_list.insert(END, row)

# Function to delete selected user from the database
def delete_user():
    selected_user = user_list.curselection()
    if selected_user:
        conn = sqlite3.connect('expense_tracker.db')
        c = conn.cursor()
        user_id = user_list.get(selected_user)[0]
        c.execute("DELETE FROM users WHERE id=?", (user_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "User deleted successfully!")
        retrieve_users()
    else:
        messagebox.showerror("Error", "Please select a user to delete")

# Function to update selected user's data in the database
def update_user():
    selected_user = user_list.curselection()
    if selected_user:
        user_id = user_list.get(selected_user)[0]
        fullname = fullname_entry.get()
        lastname = lastname_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        if fullname == '' or lastname == '' or email == '' or password == '' or confirm_password == '':
            messagebox.showerror("Error", "Please fill in all fields")
        elif not (email.endswith("@gmail.com") or email.endswith("@yahoo.com")):
             messagebox.showerror("Error", "Invalid email address")
        elif len(password)<8:
            messagebox.showerror("Error","Password is less than 8 characters")
        elif password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
        else:
            try:
                conn = sqlite3.connect('expense_tracker.db')
                c = conn.cursor()
                c.execute("UPDATE users SET fullname=?, lastname=?, email=?, password=? WHERE id=?",
                        (fullname, lastname, email, password, user_id))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "User updated successfully!")
                retrieve_users()
            except sqlite3.IntegrityError: #ensures email remains unique
               messagebox.showerror("Error", "Email address already exists!")
    else:
        messagebox.showerror("Error", "Please select a user to update")

root = Tk()
root.title("SIGN UP")
root.maxsize(width="760",height="410")
root.config(bg="#82a67d")
create_table()

# Left Frame
left_frame = Frame(root, width=350, height=410,bg="white")
left_frame.pack(side="left")
label1=Label(left_frame,text="PENNY",font=("Hubballi",40),bg="white",fg="#82a67d")
label2=Label(left_frame,text="PATROL",font=("Hubballi",40),bg="white",fg="#82a67d")
label1.place(x=60,y=120)
label2.place(x=60,y=200)


# Right Frame for Labels, Entry fields, and Listbox
right_frame = Frame(root,width=380,height=410)
right_frame.config(bg="#82a67d")
right_frame.pack(side="left", padx=20, pady=10)

# Labels
Label(right_frame, text="First Name:", bg="#82a67d").grid(row=0, column=0, padx=5, pady=5)
Label(right_frame, text="Last Name:", bg="#82a67d").grid(row=1, column=0, padx=5, pady=5)
Label(right_frame, text="Email:", bg="#82a67d").grid(row=2, column=0, padx=5, pady=5)
Label(right_frame, text="Password:", bg="#82a67d").grid(row=3, column=0, padx=5, pady=5)
Label(right_frame, text="Confirm Password:", bg="#82a67d").grid(row=4, column=0, padx=5, pady=5)

# Entry fields
fullname_entry = Entry(right_frame)
fullname_entry.grid(row=0, column=1, padx=5, pady=5)
lastname_entry = Entry(right_frame)
lastname_entry.grid(row=1, column=1, padx=5, pady=5)
email_entry = Entry(right_frame)
email_entry.grid(row=2, column=1, padx=5, pady=5)
password_entry = Entry(right_frame, show="*")
password_entry.grid(row=3, column=1, padx=5, pady=5)
confirm_password_entry = Entry(right_frame, show="*")
confirm_password_entry.grid(row=4, column=1, padx=5, pady=5)

# Buttons
add_button = Button(right_frame, text="signup", command=add_user)
add_button.grid(row=5, column=0, padx=5, pady=5)
retrieve_button = Button(right_frame, text="Retrieve", command=retrieve_users)
retrieve_button.grid(row=5, column=1, padx=5, pady=5)
delete_button = Button(right_frame, text="Delete", command=delete_user)
delete_button.grid(row=5, column=2, padx=5, pady=5)
update_button = Button(right_frame, text="Update", command=update_user)
update_button.grid(row=5, column=3, padx=5, pady=5)

# User Listbox
user_list = Listbox(right_frame, width=40, height=10)
user_list.grid(row=6, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
