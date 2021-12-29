from tkinter import *


def run():
    wd = Tk()
    wd.geometry("300x325")
    wd.title("ToDo: Sign Up")

    title = Label(wd, text="ToDo", font=("Arial-Black", 15))

    email_lbl = Label(wd, text="Email")
    email_entry = Text(wd, font=("Calibri", 10), width=30, height=1)

    username_lbl = Label(wd, text="Username")
    username_entry = Text(wd, font=("Calibri", 10), width=30, height=1)

    password_lbl = Label(wd, text="Password")
    password_entry = Entry(wd, font=("Calibri", 10), show="•")

    submit_btn = Button(wd, text="Submit")

    email_lbl.place(x=10, y=40)
    email_entry.place(x=10, y=60)
    username_lbl.place(x=10, y=90)
    username_entry.place(x=10, y=110)
    password_lbl.place(x=10, y=140)
    password_entry.place(x=10, y=170)

    submit_btn.place(x=50, y=200)

    title.place(x=125, y=0)

    wd.mainloop()


run()
