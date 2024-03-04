from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3

root=Tk()
root.title("Login")
root.config(bg='#658d6d')
root.maxsize(width=760,height=490)
root.minsize(width=760,height=490)

#function for resizing image
def resize_image(image_path, width, height):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height)) #resizes width and height
    return ImageTk.PhotoImage(resized_image)
resized_image = resize_image("Rectangle 4.png", 350, 490) #calls resize_image function with width and height value

#image placement
image_label=Label(root,image=resized_image)
image_label.place(x=0,y=0)

def homep():
    root.destroy()
    import homepage

def reg():
    root.destroy()
    import signup

#function to verify login and check credentials
def login():
#fetch email and password value from tkinter entries
    email = email_entry.get()
    password = password_entry.get()

    conn = sqlite3.connect("UserDB.db")
    c = conn.cursor()
#method to retrieve the data
    c.execute('''SELECT * FROM users WHERE email=? AND password=?''', (email, password))
#returns single record
    user = c.fetchone()
    conn.close()

    if user:
        messagebox.showinfo("Success", "You have successfully logged in")
        homep()
    else:
        messagebox.showerror("Error", "Invalid Login")
   
#creating widgets
name_label=Label(root,text="PENNY PATROL",bg='#658d6d',font=('Hubballi',35),fg='dark green')
email_entry=Entry(root,font=('Arial,10'),fg='grey',width=25)
email_entry.insert(0,"Email Address")
password_entry=Entry(root,font=('Arial,10'),fg='grey',width=25)
password_entry.insert(0, "Password")
login_button=Button(root,text="LOGIN",bg='dark green',fg="white",font=('Hubbali',12),activebackground="peach puff",command=login,borderwidth=3)
login_button.config(width=12)
signup_button=Button(root,text="SIGN UP", bg="dark green",fg='white',font=('Hubbali',12),borderwidth=3,command=reg)
signup_button.config(width=12)


#placing widgets on screen
name_label.place(x=386,y=80)
email_entry.place(x=428,y=170,height=40)
password_entry.place(x=428,y=230,height=40)
login_button.place(x=490,y=300)
signup_button.place(x=490,y=350)

root.mainloop()
