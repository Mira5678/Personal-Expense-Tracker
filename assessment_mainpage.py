

from tkinter import *
from tkinter import messagebox
import main_menu
import os

#Create register page
def register_page():
    registration = Toplevel(login_page) #create the register page on top of the login page
    registration.title("Register") #window titled register
    registration.geometry("400x200") #window size

    #set the variables to be global 
    global new_username
    global new_password
    global register_username
    global register_password

    #variable to store new username as string
    new_username = StringVar()
    new_password = StringVar()

    #Show on the top that this is a registration page
    Label(registration, text="Register: ", font= ("Verdana", 25)).pack()
    Label(registration, text="").pack()
    Label(registration, text = "Please type in a username and password that you want", fg="blue").pack()

    #Register username
    Label(registration, text="Username: ").pack() #put label
    register_username = Entry(registration, textvariable=new_username) #for the user to enter their username
    register_username.pack()

    Label(login_page, text="").pack() #add a space

    #Register password
    Label(registration, text="Password: ").pack() #add label
    register_password = Entry(registration, textvariable=new_password) #for the user to enter their password
    register_password.pack()

    Label(login_page, text="").pack() #add a space
    Button(registration, text="Register", command=register_new_user).pack() #add button 

#save the user's new username and password
def register_new_user():
    get_username = new_username.get() #get the inputted new username
    get_password = new_password.get() #get the inputted new password

    #create and open a new file with the new username
    user_file = open(get_username, "w")

    user_file.write(get_username + "\n") #write the new username in the file
    user_file.write(get_password) #in a new line, write the new password
    user_file.close() #close the file

    #clear the entry boxes
    register_username.delete(0, END) 
    register_password.delete(0, END)

    #show a messagebox when successfully registered
    messagebox.showinfo("Register successful!", "This user have been added successfully on the register")

#validate login
def login_validation():
    login_username = username.get() #get the inputted username
    login_password = password.get() #get the inputted password

    #clear the entry fields
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    user_file_list = os.listdir() #list of the files in this folder

    if login_username in user_file_list: #if the username entered is in the list of files
        login_file = open(login_username, "r") #open the file
        verification = login_file.read() #read the file

        if login_password in verification: #if the inputted password match with the file read
            messagebox.showinfo("Login successful!", "Logging in...") #show this message box
            access_main_menu() #call this function (this function allows you to go to the main menu page)
        
        else: #if inputted password doesn't match
            messagebox.showwarning("Wrong password", "The password does not match. Please enter again.") #show this messagebox

    else: #if the username is not in the list of files
        messagebox.showwarning("Cannot find username", "This username does not exist, please register if you want to create a new one.") #show this messagebox

#function to access main menu
def access_main_menu():
    login_page.withdraw() #hide the window login_page
    main_menu.main_menu_page(login_page) #open the main menu page

#Login page
def log_in_screen():
    global login_page #set the login_page to be global
    #create window for login
    login_page = Tk()
    login_page.geometry("1000x500")
    login_page.title("Budget tracker")

    #put these texts into the window
    Label(login_page, text="Hello! Welcome to my budget tracker!", font = ("Arial", 30)).pack()
    Label(login_page, text = "Please log in!", font=("Arial", 20)).pack()
    Label(login_page, text="").pack() #add a space

    #set username and password to be global (can use this variable everywhere, inside and outside the function)
    global username
    global password

    #Set the vaiables to strings
    username = StringVar()
    password = StringVar()

    #set variables to be global
    global username_entry
    global password_entry

    #username login
    Label(login_page, text = "Username: ").pack()
    username_entry = Entry(login_page, textvariable = username) #create entry field to enter in username
    username_entry.pack()

    #password login
    Label(text = "Password: ").pack()
    password_entry = Entry(login_page, textvariable=password) #create entry field to enter in password
    password_entry.pack()

    Label(login_page, text="").pack() #add a space

    Button(login_page, text="Login", command= login_validation).pack() #create a button, when clicked validate the login information entered
    Label(login_page, text="").pack()

    #show the example username and password that have already been created
    Label(login_page, text="Example: Username = John, Password = 2007 ", fg="Blue").pack() 

    #Create a register button. When click, will go to registration page
    Label(login_page, text="").pack()
    Label(login_page, text="Do not have an account yet?").pack()
    Button(login_page, text="Register", command=register_page).pack() #when press this button, open the register page

    Label(login_page, text="").pack() #add space
    Button(login_page, text="Quit", command = login_page.destroy).pack() #when click this button, quit the program (destroy the window)


    login_page.mainloop() # Start the Tkinter event loop

if __name__ == "__main__": #if called call this function
    log_in_screen() #end function








