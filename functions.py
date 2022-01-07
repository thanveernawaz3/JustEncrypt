from tkinter import *
from tkinter import filedialog

def pass_test():
    print("Manage Password Clicked")


def enc_test():
    print("Encrypt Password File Clicked")



def browseFile():
    filename = filedialog.askopenfilename(initialdir="/",title="Select file",filetypes=(("Text files","*.txt"),("all files","*.*")))