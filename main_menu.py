from tkinter import *
import transaction 
import goal 
import assessment_mainpage

#go to transaction page
def open_transaction_page():
    main_menu.withdraw() #withdraw the main menu page
    transaction.transaction_screen(main_menu) #pass the main_menu page to the transaction_screen function

#go to goal page
def open_goal_page():
    main_menu.withdraw() #withdraw the main menu page
    goal.goal_page(main_menu) #pass the main menu page to the goal_page function in the goal file

#go back to log in page
def open_login_screen(main_menu, main_login_page):
    main_menu.destroy() #destroy main menu page
    main_login_page.deiconify() #redraw the login page (show the login page)

#main menu window
def main_menu_page(main_login_page):
    global main_menu 
    #create main menu window
    main_menu = Tk()
    main_menu.geometry("500x400")
    
    #show title
    Label(main_menu, text="MAIN MENU", font=("Times New Roman", 25)).pack()
    Label(main_menu, text="").pack()

    #3 buttons which are add transaction, set goal and log out
    Label(main_menu, text="").pack()
    #when click this button, go to transaction page
    Button(main_menu, text="Add transactions", height = "3", width="45", command=open_transaction_page).pack()

    Label(main_menu, text="").pack()
    #when click this button, go to goals page
    Button(main_menu, text="Set goals", height = "3", width="45", command = open_goal_page).pack()

    Label(main_menu, text="").pack()
    #when click this button, go back to the login page
    Button(main_menu, text="log out", height = "3", width="45", command = lambda: open_login_screen (main_menu, main_login_page)).pack()


    main_menu.mainloop() #start tkinter event loop

if __name__=="__main__": #if called call this function
    main_menu_page() #end function



