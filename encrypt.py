from tkinter import *
from tkinter import font
from PIL import ImageTk,Image

top=Tk()

canvas = Canvas(top,width=600,height=500)
canvas.grid(columnspan=3,rowspan=3)

#Logo
logo=Image.open('Justencrypt.png')
logo = ImageTk.PhotoImage(logo)
logo_label=Label(image=logo)
logo_label.image=logo
logo_label.grid(column=1,row=0)

#Slogan
slogan=Label(text="Your Mini password manager",font=("Raleway",12),width=100,fg="#244c7c")
slogan.grid(column=1,row=1)



#Options Buttons
manage_password = Button(text="Manage Passowrd")
manage_password.grid(column=0,row=2)

decrypt_file=Button(text="Decrypt File")
decrypt_file.grid(column=1,row=2)


top.mainloop()