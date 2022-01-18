try:
    import Tkinter as tk
    
except:
    import tkinter as tk
from lib2to3.pgen2.grammar import opmap_raw
from PIL import ImageTk,Image
from tkinter import filedialog
from functions import browseFile
import uuid





class SampleApp(tk.Tk):



    def __init__(self):
        tk.Tk.__init__(self)
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

        btn1 = tk.Button(self,text="Manage Password",command=lambda: master.switch_frame(ManagePassword)).grid(column=0,row=2,padx=(0,140),pady=(25,0))
        btn2  =tk.Button(self,text="Decrypt File",command=lambda: master.switch_frame(DecryptFile)).grid(column=0,row=2,padx=(180,0),pady=(25,0))


class ManagePassword(tk.Frame):

    

 


    # def submit(self):
    #     print("Hai hello")

    def __init__(self, master):
        self.sitename_var=tk.StringVar()
        self.username_var=tk.StringVar()
        self.password_var=tk.StringVar()



        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="Manage your passwords here", font=('Helvetica', 18, "bold")).grid(row=0,column=1)
        title_label = tk.Label(self,text="Site Name").grid(row = 1, column = 0, pady = 2)
        title = tk.Entry(self,textvariable=self.sitename_var).grid(row = 2, column = 0, pady = 2)
        username_label = tk.Label(self,text="Username or Email").grid(row = 1, column = 1, pady = 2)
        username= tk.Entry(self,textvariable=self.username_var).grid(row = 2, column = 1, pady = 2)
        password_label = tk.Label(self,text="Password").grid(row = 1, column = 2,pady = 2)
        password = tk.Entry(self,textvariable=self.password_var).grid(row = 2, column = 2, pady = 2)
        add=tk.Button(self,text="Add another field").grid(row=3,column=0,pady=2)
        process= tk.Button(self,text="Start Process",command=self.submit).grid(row=3,column=0,padx=(250,0))
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).grid()
       
       
    def submit(self):
            sitename = self.sitename_var.get()
            username=self.username_var.get()
            password=self.password_var.get()

            print("The name is : " + sitename)
            print("The password is : " + username+password)

            

            self.sitename_var.set("")
            self.username_var.set("")
            self.password_var.set("")

            try:
                filename =input("Enter the name for your file")
                with open(f'{filename}.txt','w') as f:
                    f.write(sitename)
            except FileNotFoundError:
                    print("File check pannu vro")


         


    

class DecryptFile(tk.Frame):
    def __init__(self, master): 
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Decrypt the password file", font=('Helvetica', 18, "bold")).grid(row=0,column=1)
        tk.Label(self,text="Choose the file").grid(row=1,column=0)
        filename= tk.Button(self,text="Browse File",command=browseFile).grid(row = 1, column = 1, pady = 2)

        tk.Label(self,text="Enter the Password").grid(row=2,column=0)
        file_password= tk.Entry(self).grid(row = 2, column = 1, pady = 2)

        tk.Button(self,text="Start").grid(row=3,column=1)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).grid()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
