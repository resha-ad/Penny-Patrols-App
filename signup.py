from tkinter import*
from tkinter import messagebox
import sqlite3
root=Tk()
lbl=Label(root,text='PENNY PATROL',font=('Arial Bold',30))
lbl.place(x=200,y=0)
root.geometry('1000x1000')
root.resizable(1,1)

con=sqlite3.connect('user_database.db')
cursor=con.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS user(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    fname           TEXT,
    lname            TEXT,
    eml              TEXT,
    pw               INT
    cpw              INT                      
)''')
con.commit()
con.close()

def add():
    con=sqlite3.connect('user_database.db')
    c=con.cursor()
    c.execute('INSERT INTO user(fname,lname,eml,pw,cpw) VALUES(?,?,?,?,?)',
              (firstname.get(),lastname.get(),email.get(),password.get(),confirmpassword()))
    con.commit()
    con.close()
    firstname.delete(0,END)
    lastname.delete(0,END)
    email.delete(0,END)
    password.delete(0,END)
    confirmpassword.delete(0,END)


def retrieve():
    con=sqlite3.connect('user_database.db')
    c=con.cursor()
    c.execute("SELECT * FROM user")
    records=c.fetchall()
    print(records)
    print_records=''
    for record in records:
        print_records+=str(record[0])+' '+str(record[1])+' '+str(record[2])+' '+str(record[3])+' '+str(record[4])+' '+str(record[5])+'\n'
    query_label=Label(root,text=print_records)
    query_label.place(x=450,y=100)
    con.close()

def delete():
    con=sqlite3.connect('user_database.db')
    c=con.cursor()
    c.execute('DELETE FROM user WHERE ID='+deletebox.get())
    con.commit()
    con.close()
    deletebox.delete(0,END)
    retrieve()

def edit():
    global editor
    editor=Tk()
    editor.title('Update Data')
    editor.geometry('300x400')
    con=sqlite3.connect('user_database.db')
    c=con.cursor()
    record_id=updatebox.get()
    c.execute('SELECT * FROM user WHERE ID=?',(record_id,))
    records=c.fetchall()
    global  firstname_editor
    global lastname_editor
    global  email_editor
    global password_editor
    global confirmpassword_editor

    firstname_editor=Entry(editor,width=30)
    firstname_editor.grid(row=0,column=1,padx=20,pady=(10,0))

    lastname_editor=Entry(editor,width=30)
    lastname_editor.grid(row=1,column=1)

    email_editor=Entry(editor,width=30)
    email_editor.grid(row=2,column=1)

    password_editor=Entry(editor,width=30)
    password_editor.grid(row=3,column=1)

    confirmpassword_editor=Entry(editor,width=30)
    confirmpassword_editor.grid(row=4,column=1)
    
    firstname_label=Label(editor,text="Username")
    firstname_label.grid(row=0,column=0,pady=(10,0))

    lastname_label=Label(editor,text="Address")
    lastname_label.grid(row=1,column=0)

    email_label=Label(editor,text="Email")
    email_label.grid(row=2,column=0)

    password_label=Label(editor,text="Password")
    password_label.grid(row=3,column=0)

    confirmpassword_label=Label(editor,text="Confirmpassword")
    confirmpassword_label.grid(row=4,column=0)


    for record in records:
        firstname_editor.insert(0,record[1])
        lastname_editor.insert(0,record[2])
        email_editor.insert(0,record[3])
        password_editor.insert(0,record[4])
        confirmpassword_editor.insert(0,record[5])

    updatebox.delete(0,END)
    btn_save=Button(editor,text='SAVE',command=lambda:update(record_id))
    btn_save.grid(row=5,column=0,columnspan=2, pady=10,padx=10,ipadx=125)
    

def update(record_id):
    con=sqlite3.connect('emp_database.db')
    c=con.cursor()
    c.execute('''
        UPDATE employee SET 
              fname=:f,
              lname=:l,
              eml=:e,
              pw=:p,
              cpw=:c,
               WHERE ID = :id''',
               {
                   'f': firstname_editor.get(),
                   'l': lastname_editor.get(),
                   'e': email_editor.get(),
                   'p': password_editor.get(),
                   'c': confirmpassword_editor.get(),
                   'id': record_id
               }
    )
    con.commit()
    con.close()
    editor.destroy()
    retrieve()







label_firstname=Label(root,text="Firstname",font=("Arial Bold",20))
label_firstname.place(x=0,y=90)

label_lastname=Label(root,text="Lastname",font=("Arial Bold",20))
label_lastname.place(x=0,y=140)

label_email=Label(root,text="Email",font=("Arial Bold",20))
label_email.place(x=0,y=190)

label_password=Label(root,text="Password",font=("Arial Bold",20))
label_password.place(x=0,y=240)

label_confirmpassword=Label(root,text="Confirmpassword",font=("Arial Bold",20))
label_confirmpassword.place(x=0,y=290)

label_delete=Label(root,text="DeleteRecord",font=("Arial Bold",20))
label_delete.place(x=0,y=350)

label_update=Label(root,text="UpdateRecord",font=("Arial Bold",20))
label_update.place(x=0,y=480)

firstname=Entry(root,width=30)
firstname.place(x=170,y=100,height=30)

lastname=Entry(root,width=30)
lastname.place(x=170,y=150,height=30)

email=Entry(root,width=30)
email.place(x=170,y=200,height=30)

password=Entry(root,width=30)
password.place(x=170,y=250,height=30)

confirmpassword=Entry(root,width=30)
confirmpassword.place(x=170,y=300,height=30)

deletebox=Entry(root,width=30)
deletebox.place(x=190,y=350,height=30)

updatebox=Entry(root,width=30)
updatebox.place(x=210,y=480,height=30)

btn_add=Button(root,text="Add",font=('Arial Bold',20),command=add)
btn_add.place(x=0,y=400)

btn_retrieve=Button(root,text="Retrieve",font=('Arial Bold',20),command=retrieve)
btn_retrieve.place(x=100,y=400)

btn_delete=Button(root,text="Delete",font=('Arial Bold',20),command=delete)
btn_delete.place(x=250,y=400)

btn_edit=Button(root,text="Update",font=('Arial Bold',20),command=edit)
btn_edit.place(x=400,y=400)



root.mainloop()
