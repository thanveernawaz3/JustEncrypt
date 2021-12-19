from tkinter import *
from tkinter import font
import tkinter as tk

top=tk.Tk()

top.geometry('500x500')

top.title("Just Encrypt")

# label = Label(top,text="Hey there,Welcome to Just Encrypt").pack()


# # label = Label(top,text="Choose your option").pack()


# button = Button(top,text="Close",bd = '2',
#                           command = top.destroy).pack()


user_name = Label(top, 
                  text = "Username").place(x = 40,
                                           y = 60) 

user_password = Label(top,text="Password").place(x = 40,y = 100)

submit = Button(top,text="Submit").place(x = 40,
                                              y = 130)


# name_input = Entry(top,width=30).place(x = 110,
#                                                y = 60) 

# password_input = Entry(top,width=30).place(x = 110,
#                                                    y = 100)



name_var = tk.StringVar()
pass_var = tk.StringVar()


def submit():
    name = name_var.get()
    password = pass_var.get()

    print(f'The name is {name}')
    print(f'The password is {password}')

    name_var.set('')
    pass_var.set('')


name_label=tk.Label(top,text="Username",font=('calibre',10,'bold'))

name_entry=tk.Entry(top,textvariable=name_var,font=('calibre',10,'normal'))


pass_label=tk.Label(top,text="Password",font=('calibre',10,'bold'))

pass_entry=tk.Entry(top,textvariable=pass_var,font=('calibre',10,'normal'),show='*')

submitBtn = tk.Button(top,command=submit,text="Login")


name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
pass_label.grid(row=1,column=0)
pass_entry.grid(row=1,column=1)
submitBtn.grid(row=2,column=1)









# button = Button(top,text="Decrypt the password file").pack()








top.mainloop()