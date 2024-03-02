from tkinter import *
from PIL import ImageTk, Image

window=Tk()
window.title("Home Page")
window.config(bg='#82a67d')
window.maxsize(width=760,height=490)
window.minsize(width=760,height=490)

#creating and placing frame inside window
frame1=Frame(window,width=200,height=440)
frame1.config(bg="white")
frame1.place(x=20,y=20)

#creating and placing frame inside window
frame2=Frame(window,width=500,height=440)
frame2.config(bg="white")
frame2.place(x=240,y=20)

def resize_image(image_path, width, height):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height)) #resizes width and height
    return ImageTk.PhotoImage(resized_image)
resized_image = resize_image("penny.png",40,40) #calls resize_image function with width and height value

#image placement
image_label=Label(window,image=resized_image)
image_label.place(x=80,y=50)

#creating widgets,
name_label=Label(frame2,text="HELLO FIRSTNAME",font=('Hubballi',25),fg='dark green', bg='white')
name_label2=Label(frame1,text='PENNY PATROL',font=('Hubballi',15),fg='dark green',bg='white')
name_label3=Label(frame2,text='Saving money today secures your tomorrow',font=('Hubballi',15),fg='green',bg='white')
add_expense_button=Button(frame1,text="Add expense",bg='white',borderwidth='0')
add_expense_button.place(x=20,y=140)
add_income_button=Button(frame1,text="Add income",bg='white',borderwidth='0')
add_income_button.place(x=20,y=180)
view_report_button = Button(frame1, text="View Report",bg='white',borderwidth='0')
view_report_button.place(x=20, y=220)
logout_button = Button(frame1, text="logout",bg='lightgrey',borderwidth='0')
logout_button.place(x=40, y=400)

name_label.place(x=100,y=80)
name_label2.place(x=10,y=100)
name_label3.place(x=80,y=180)

window.mainloop()
