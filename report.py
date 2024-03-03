from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from data import expense_data
import json

# Load data from JSON file
with open('totals.json', 'r') as infile:
    data = json.load(infile)

# Access values and store in variables
total_expense = data['total_expense']
savings = data['savings']
balance = data['balance']
income = data ['income']

plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#7FFFD4", "#2F4F4F", "#7FFF00", "#006400", "#B4EEB4"])

fig1, ax3 = plt.subplots(figsize=(5, 5))
ax3.pie(expense_data.values(), labels=expense_data.keys(), autopct='%1.1f%%')
ax3.set_title("Expenses By Type")

window = Tk()
window.title("View Report Page")
window.config(bg="white")
window.maxsize(width=1300, height=900)
window.minsize(width=1300, height=900)

def log():
    window.destroy()
    import signin

logout_button = Button(window, text="Logout", bg='lightgrey', borderwidth=0, command=log)
logout_button.place(x=30, y=850)

frame2 = Frame(window, width=660, height=600, bg="white")
frame2.place(x=230, y=20)

PieChart = FigureCanvasTkAgg(fig1, master=frame2)
PieChart.draw()
PieChart.get_tk_widget().place(relx=0.5, rely=0.5, anchor=CENTER)
  

frame3 = Frame(window, bg="#bcecac", width=220, height=150)
frame3.place(x=980, y=80)
bl = Label(frame3, text="Balance", borderwidth=0, bg="#bcecac", font=("Arial", 15))
bl.place(x=50, y=30)
balance = Label(frame3,text=savings, bg="grey", width=20)
balance.place(x=30, y=70)


frame4 = Frame(window, bg="#bcecac", width=220, height=150)
frame4.place(x=50, y=670)
il = Label(frame4, text="+Income", borderwidth=0, bg="#bcecac", font=("Arial", 15))
il.place(x=50, y=30)
income = Label(frame4, text=income, bg="grey", width=20)
income.place(x=30, y=70)

frame5 = Frame(window, bg="#bcecac", width=220, height=150)
frame5.place(x=980, y=670)
el = Label(frame5, text="-Expenses", borderwidth=0, bg="#bcecac", font=("Arial", 15))
el.place(x=50, y=30)
expense = Label(frame5, text=total_expense, bg="grey", width=20)
expense.place(x=30, y=70)

frame6 = Frame(window, bg="#bcecac", width=220, height=150)
frame6.place(x=40, y=80)
sl = Label(frame6, text="Saving", borderwidth=0, bg="#bcecac", font=("Arial", 15))
sl.place(x=50, y=30)
saving = Label(frame6, text=savings, bg="grey", width=20)
saving.place(x=30, y=70)


window.mainloop()

