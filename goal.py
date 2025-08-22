from tkinter import *
from tkinter import messagebox

#get the current balance that was saved
def get_current_balance():
    try: #try do this
        with open('balance_info.txt', 'r') as file: #open the file
            read_line = file.readlines() #read each line
            if len(read_line) >= 2: #if the lines is greater or equal than 2
                total_income = float(read_line[0]) #total income will equal to the first line set as float
                total_expenses = float(read_line[1]) #total expenses will equal to the second line set as float
                balance = round(total_income - total_expenses, 2) #calculate the balance
                return balance #return the value
        
    except FileNotFoundError: #if the file doesn't exist (not found)
        pass #skip

#handles what is entered in the entry box and also save data
def handling_input():
    my_goal = goal_entry.get() #get the inputted target amount
    my_month = month_entry.get() #get the inputted target month
    get_balance = get_current_balance() #get the current balance from the function above


    if not my_goal and not my_month: #if the entry fields for the amount and month are empty
        messagebox.showwarning("Nothing entered", "Please enter in your target amount and your target month") #show this messagebox
        return #return to the window
        
    if not my_goal: #if there's nothing entered for the target amount
        messagebox.showwarning("Goal not entered", "Please enter in your target amount")#show this messagebox
        return #return to the window
        
    if not my_month: #if there's nothing entered for the target month
        messagebox.showwarning("Month not entered", "Please enter in your target month")#show this messagebox
        return #return to the window
    
    
    if float(my_goal) <= 0: #if the target amount is less than 0
        messagebox.showwarning("Goal less then 0", "Are you even trying? You can't set your goal to be a negative amount!") #show this messagebox
        return
    

    try:
        my_goal = float(my_goal) #target amount is float

    except: #if target amount is not float
        messagebox.showwarning("Wrong variable", "Please enter your target amount in numbers only") #show this messagebox
        return


    try:
        my_month = float(my_month) #target month is float
    except: #if target month is not float
        messagebox.showwarning("Wrong variable", "Please enter the months in numbers only") #show this messagebox
        return
    


    with open("setting_goal.txt", "a") as txt_file: #open this file as txt_file
        txt_file.write(f"Amount: £{my_goal} in {my_month} months" + "\n") #write the goal and month is this format into the file

    amount_needed = round(my_goal - get_balance,2) #calculate amount needed to reach goal
    amount_each_month = round(amount_needed/my_month, 2) #calculate amount needed each month
    show_amount_needed.config(text=f"You need £{amount_needed} to reach your target") #change the text to this
    saved_each_month.config(text=f"£{amount_each_month} per month") #change the text to this

    #clear entry fields
    goal_entry.delete(0,END)
    month_entry.delete(0,END)

    #show this messagebox when everything is entered in correctly
    messagebox.showinfo("Goals saved", "your target have been saved successfully") 



    
#the goal page window
def goal_page(main_menu_screen):
    #create the goal page
    goal = Tk()
    goal.title(" My Goal page ")
    goal.geometry("500x500")

    #set the variables to be global
    global goal_entry
    global month_entry
    global show_amount_needed
    global saved_each_month

    Label(goal, text="Target", font=("Times New Roman", 25)).pack()

    Label(goal, text="Please enter the amount you want to achieve").pack()

    #user enter in target amount
    Label(goal, text = "Set target amount: £").pack()
    goal_entry = Entry(goal) #create entry field to enter in target amount
    goal_entry.pack()

    #user enter in target month
    Label(goal, text="Month(s) you want to achieve in: ").pack()
    month_entry = Entry(goal) #create entry field to enter in target month
    month_entry.pack()

    Button(goal, text="Save goal", command= handling_input).pack() #button when clicked will validate the entries

    Label(goal, text="").pack() #add space
    #initially say this. When you save your goal, this text will change.
    show_amount_needed = Label(goal, text="You need £ 0.00 to reach your goal", fg="red")
    show_amount_needed.pack()

    Label(goal, text="").pack() #add space

    Label(goal, text="That means you will need to save").pack()
    #initially say this. When you save your goal, this text will change
    saved_each_month = Label(goal, text="£0.00 per month", fg="green")
    saved_each_month.pack()

    #button when clicked will go back to the main menu page
    Button(goal, text = "Back to main menu", command = lambda: back_to_mainmenu (goal, main_menu_screen)).pack()

    goal.mainloop() #Start the Tkinter event loop

#function to go back to main menu page
def back_to_mainmenu(goal, main_menu_screen):
    goal.destroy() #destroy the goal page (this page)
    main_menu_screen.deiconify() #redraw the window (show the main menu window again)

if __name__ == "__main__": #if called call this function
    goal_page() #end function
