try:
    import Tkinter as tk
    
except:
    import tkinter as tk
from cProfile import label
from cgitb import text
from doctest import master
from fileinput import filename
from lib2to3.pgen2.grammar import opmap_raw
from os import popen
from tabnanny import check, filename_only
from PIL import ImageTk,Image
from tkinter import Toplevel, filedialog

from matplotlib.pyplot import margins, title
import pyAesCrypt
import uuid
import os


#Bay of Many

#264d7d
#Picton Blue

#4db4e3
#Nepal

#8caac4
#Hoki

#6884a4


class SampleApp(tk.Tk):

    

    def __init__(self):
       
        tk.Tk.__init__(self,className="Just Encrypt - Your Mini Password Manager")
        self._frame = None
       
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()




class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        logo=Image.open('Justencrypt.png')
        logo = ImageTk.PhotoImage(logo)
        logo_label=tk.Label(self,image=logo)
        logo_label.image=logo
        logo_label.grid()

        #Slogan
        slogan=tk.Label(self,text="Your Mini password manager",font=("Raleway",12),width=100,fg="#244c7c")
        slogan.grid()

        btn1 = tk.Button(self,text="Manage Password",fg="white",bg="#4db4e3",padx=15,pady=10,borderwidth=0,command=lambda: master.switch_frame(ManagePassword)).grid(column=0,row=2,padx=(0,140),pady=(25,0))
        btn2  =tk.Button(self,text="Decrypt File",fg="white",bg="#4db4e3",padx=15,pady=10,borderwidth=0,command=lambda: master.switch_frame(DecryptFile)).grid(column=0,row=2,padx=(180,0),pady=(25,0))
        slogan=tk.Label(self,text="")
        slogan.grid()


class ManagePassword(tk.Frame):

    
    def __init__(self, master):
        self.sitename_var=tk.StringVar()
        self.username_var=tk.StringVar()
        self.password_var=tk.StringVar()
        self.filename_var=tk.StringVar()
        self.filepass_var=tk.StringVar()



        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="Manage your passwords here", font=('Helvetica', 18, "bold")).grid(row=0,column=1)
        title_label = tk.Label(self,text="Site Name").grid(row = 1, column = 0, pady = 2)
        title = tk.Entry(self,textvariable=self.sitename_var).grid(row = 2, column = 0, pady = 2)
        username_label = tk.Label(self,text="Username or Email").grid(row = 1, column = 1, pady = 2)
        username= tk.Entry(self,textvariable=self.username_var).grid(row = 2, column = 1, pady = 2)
        password_label = tk.Label(self,text="Password").grid(row = 1, column = 2,pady = 2)
        password = tk.Entry(self,textvariable=self.password_var).grid(row = 2, column = 2, pady = 2)
        
        add=tk.Button(self,text="Add another field",command=self.openTab).grid(row=3,column=0,pady=2)
        process= tk.Button(self,text="Start Process",command=self.validate).grid(row=3,column=0,padx=(250,0))
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).grid()


    def choice(self,option):
        pop.destroy()
        if option == "yes":
            label.config(text="Haii")
        else:
            label.config(text="Noo")


    def openTab(self):
         title_label = tk.Label(self,text="Site Name").grid(row = 3, column = 0, pady = 2)
         title = tk.Entry(self,textvariable=self.sitename_var).grid(row = 4, column = 0, pady = 2)
 

    def validate(self):
        sitename = self.sitename_var.get()
        username = self.username_var.get()
        password=self.password_var.get()
        msg=''

        if (sitename=='') or (username=='') or (password == ''):
            msg="Empty Values not allowed"

        else:
            self.click_fun()




    def click_fun(self):
        global pop
        pop = Toplevel(master)
        pop.title("Confirmation")
        pop.geometry("400x300")
        label=tk.Label(pop,text="Py is overrated").grid(row=0,column=2)
       
        filename_label =tk.Label(pop,text="Enter a name for your file").grid(row=1,column=0)
        filename=tk.Entry(pop,textvariable=self.filename_var).grid(row=1,column=1)
        filepassword_label=tk.Label(pop,text="A Password to encrypt your file").grid(row=2,column=0)
        filepass=tk.Entry(pop,textvariable=self.filepass_var).grid(row=2,column=1)
        done=tk.Button(pop,text="Done",command=self.submit).grid(row=3,column=1)

    

       
    def submit(self):
            sitename = self.sitename_var.get()
            username=self.username_var.get()
            password=self.password_var.get()
            filename=self.filename_var.get()
            filepass=self.filepass_var.get()



            with open(f'{filename}.txt','w') as file:
                writing=file.write(f'{sitename} and {username} and {password}')

            
            
            pyAesCrypt.encryptFile(f'{filename}.txt',f'{filename}',filepass)
            os.remove(f'{filename}.txt')

            self.sitename_var.set("")
            self.username_var.set("")
            self.password_var.set("")



    

class DecryptFile(tk.Frame):
    filename=''
    def __init__(self, master): 
        self.decfilepass_var=tk.StringVar()
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Decrypt the password file", font=('Helvetica', 18, "bold")).grid(row=0,column=1)
        tk.Label(self,text="Choose the file").grid(row=1,column=0)
        filename= tk.Button(self,text="Browse File(.enc file only)",command=self.browseFile,fg="white",bg="#4db4e3").grid(row = 1, column = 1, pady = 2)

        tk.Label(self,text="Enter the Password").grid(row=2,column=0)
        file_password= tk.Entry(self,textvariable=self.decfilepass_var).grid(row = 2, column = 1, pady = 2)

        tk.Button(self,text="Start",fg="white",bg="#4db4e3",command=self.stuffDone).grid(row=3,column=1)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).grid()


        

    def browseFile(self):
        global filename
        actualFile = filedialog.askopenfilename(initialdir='/',title="Select a file",filetypes=(("Enc files","*.enc"),("all files","*.*")))
        filename = actualFile
        

    def stuffDone(self):
        print(filename)




    

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
