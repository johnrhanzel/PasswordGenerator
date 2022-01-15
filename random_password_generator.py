import random
import pyperclip
from tkinter import *
from tkinter.ttk import *
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1) #calling DPI function


# Function for joining for password
def join_pass():
    entry.delete(0, END)
 
    # Get the length of password
    pass_length = combo_var.get()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""

    #Combine the alpha to generate the password as many as possible
    if main_var.get() == 0:
        for i in range(0, pass_length):
            password = password + random.choice(alpha)
        return password
    else:
        print("Error Generating...")
 
 
# Function for generation of password
def generate():
    generated_pass = join_pass()
    entry.insert(10, generated_pass)
 
 
# Function for copying password to clipboard
def copy():
    random_password = entry.get()
    pyperclip.copy(random_password)
 
 
# Main Function
 
#Store data
root = Tk()
main_var = IntVar()
combo_var = IntVar()
root.iconbitmap('D:\Free Icons\ico files\lockpass.ico')

#Window Size
root.geometry('380x150+50+50')
 
#App Title
root.title("Password Generator")
 
#Password Label and Position
Random_password = Label(root, text="Generated Password")
Random_password.grid(row=0)
entry = Entry(root, width=27)
entry.grid(row=0, column=1)
 
#Label for Password
password_label = Label(root, text="Password Length")
password_label.grid(row=1)

#Copy Button
copy_button = Button(root, text="Copy", command=copy)
copy_button.grid(row=2, column=1)

#Generate Button
generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=3, column=1)

#Combo Button for TextVariable and Value for if-else
combo_button = Combobox(root, textvariable=combo_var, values=0, width=24)

#Length of the Generated Password
combo_button['values'] = (4 ,5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
combo_button.current(0)
combo_button.bind('<<ComboboxSelected>>')
combo_button.grid(row=1, column=1)

#Label Credits
credits_label = Label(root, text="By @John Rhanzel")
credits_label.grid(row=5, column=0)
 
#Maintaining the window
root.mainloop()