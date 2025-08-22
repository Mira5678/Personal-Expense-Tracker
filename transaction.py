
from tkinter import *
from tkinter import messagebox
import csv
import matplotlib.pyplot as plt

#initialse total income and total expenses to be equal to 0
total_income = 0.00
total_expenses = 0.00 


#if there's a balance that was calculated before, you have to retrieve it
def retrieve_current_balance():
    #set variables as global
    global total_income
    global total_expenses

    try: #try opening this file
        with open("balance_info.txt", 'r') as file:
            read_line = file.readlines() #read each line
            if len(read_line) <= 2: #if line is greater than or equal to 2
                total_income = float(read_line[0]) #total income is equal to the first line set as float
                total_expenses = float(read_line[1]) #total expenses is equal to the second line set as float
    except FileNotFoundError: #if cannot find file
        pass #skip

#save the current balance in a text file.
def save_current_balance():
    with open('balance_info.txt' , 'w') as file: #open this file
        file.write(f"{total_income} \n {total_expenses}") #write the total income and expenses into it


def save_transactions(): #does most of the validation
    #set variables as global
    global total_income
    global total_expenses

    transaction_type = transaction_options.get()  # Get the selected transaction type (Income or Expense)
    amount = amount_entered.get()  # Get the entered amount
    description = label_transaction.get()  # Get the entered description
    expense_category = category_choices.get() #get the selected expense category

    if not amount and not description: #if the entry field for amount and description is empty
        messagebox.showwarning("Nothing entered", "Please enter in an amount and its description") #show warning message
        return #return to the window

    if not amount:  # if entry field for amount is empty
        messagebox.showwarning("No amount entered", "Please enter an amount and the label for that amount")  # Show warning message
        return
    
    if not description: #if entry field for description is empty
        messagebox.showwarning("No description entered", "Please enter a description for your income or expenses") #show warning message
        return

    try:
        amount = float(amount)  #amount is float
    except ValueError:  #if amount is not float
        messagebox.showwarning("Invalid amount data type", "Please enter a number only for your amount")  # Show warning message
        return
    

    transaction = [transaction_type, description, amount]  # Create a list of transaction details

    if transaction_type == "Add expense": #if the selected transaction type is add expese
        transaction.append(expense_category) #add the selected expense category into the transaction list
    elif transaction_type == "Add income": #if the selected transaction type is add income
        pass #skip(do nothing)

    with open("expenses.csv", 'a', newline='') as csv_file:  # Open the CSV file in append mode
        writer = csv.writer(csv_file)
        writer.writerow(transaction)  # Write the transaction details to the CSV file

    #calculate the current balance
    if transaction_type == "Add income":
        total_income += amount #add the amount in the add income category to the total income
    elif transaction_type == "Add expense":
        total_expenses += amount #add the amount in the add expense category to the toal expenses

    save_current_balance() #save current balance

    transaction_options.set("Add income")  # Reset the transaction type to "income"
    amount_entered.delete(0, END)  # Clear the amount entry field
    label_transaction.delete(0, END)  # Clear the description entry field
    messagebox.showinfo("Transaction saved", "This transaction has been saved successfully")  # Show info message

    #call these functions
    update_list() #update transaction list
    current_balance() #update current balance


#update the list
def update_list():
    list_transaction.delete(0, END) #clear the listbox
    with open("expenses.csv", "r")as csv_file: #open this csv file in read mode
        reader=csv.reader(csv_file) 
        for row in reader: #read each line in the csv file
            if len(row) >= 3 and row[0] == "Add income": #if the row is greater than or equal to 3(this is to avoid error) and the 1st row is add income
                list_transaction.insert(END, f"{row[0]} - {row[1]} : £{row[2]}") #insert this into the listbox
            elif len(row) >= 4 and row[0] == "Add expense": #if the row is greater than or equal to 4 and the 1st row is add expenses
                list_transaction.insert(END, f"{row[0]} (category: {row[3]}) - {row[1]} : £{row[2]}") #insert this into the listbox
            else: #if nothing else
                pass #skip
    current_balance() #update current balance

#this function calculates the current balance
def current_balance():  
    balance = round(total_income - total_expenses,2) #calculte balance
    show_balance.config(text=f"Current Balance: £{balance}") #change the text in the window to this

#show or hide the expense category based on transaction type
def choosing_expense_categories(*args):
    #if add expense is selected, show the drop down box
    if transaction_options.get() == "Add expense":
        label_category.grid(row = 3, column = 0)
        category_dropdownbox.grid(row = 4, column = 0)

    #if the add income option is selected, don't show the category
    elif transaction_options.get() == "Add income":
        label_category.grid_remove()
        category_dropdownbox.grid_remove()

#update the label according to what is selected in the dropdownbox
#the dropdownbox doesn't display itself when selected, so I add this function
def dropdownbox_selection(*args):
    selected_transaction_type = transaction_options.get() #get the selected transaction type
    selected_expense_category = category_choices.get() #get the expense category choices
    if selected_transaction_type == "Add expense": #if the transaction type is add expenses
        selected_transaction_label.config(text=f"Selected: {selected_transaction_type} - {selected_expense_category}") #change the text to this
    else: #if the transaction type add income
        selected_transaction_label.config(text=f"Selected: {selected_transaction_type}") #change the text to this


#create a pie chart based on the expense categories saved
def pie_chart():

    expense_categories = {} 

    #open the csv file to get the expense categories
    with open("expenses.csv", "r")as csv_file:
        reader=csv.reader(csv_file)
        for row in reader:
            if len(row) >= 4 and row[0] == "Add expense":
                category = row[3]
                amount = float(row[2])
                if category in expense_categories:
                    expense_categories[category] += amount
                else:
                    expense_categories[category] = amount

    labels = expense_categories.keys() #the labels are the expense categories
    data = expense_categories.values() #the data is the values of the expense categories

    #draw the pie chart
    fig, ax = plt.subplots()
    ax.pie(data, labels = labels, autopct='%1.1f%%')
    ax.axis('equal')
    plt.title('Expenses chart')
    plt.legend(labels)
    plt.show()



def transaction_screen(main_menu_page):
#the main transation page
    transaction_page = Tk()  # Create the transaction window
    transaction_page.title("Transactions")  # Set the title of the window
    transaction_page.geometry("800x600")  #set the size of the window

    #create the title to show that this is the transaction page
    Label(transaction_page, text="Transaction page", font=("Arial", 20)).grid(row=0, column=1)

    #mke these variables global as we're going to use the variables outside this function as well.
    global transaction_options, amount_entered, label_transaction, label_category, category_choices, show_balance, list_transaction, category_dropdownbox, selected_transaction_label

    #retrieve_current_balance()


    # Create and place widgets
    Label(transaction_page, text="Transaction Type: ").grid(row = 1, column = 0) # Label for transaction type
    transaction_options = StringVar(value="Add income")  # Create a StringVar to hold the transaction type
    transaction_options.trace("w", choosing_expense_categories) #call this function when transaction type changes
    transaction_options.trace("w", dropdownbox_selection) #call this function when transaction type changes
    OptionMenu(transaction_page, transaction_options, "Add income", "Add expense").grid(row = 2, column = 0) #create option menu for transaction type


    Label(transaction_page, text="Amount: £").grid(row=1, column = 1)  # Label for amount
    amount_entered = Entry(transaction_page)
    amount_entered.grid(row=1, column = 2) # Create an entry field for amount

    #dropdown box for expense categories
    label_category = Label(transaction_page, text="Expense categories: ")
    category_choices = StringVar() #the category choices are set to be strings
    category_choices.trace("w", dropdownbox_selection) #call this function when category choices change
    category_dropdownbox = OptionMenu(transaction_page, category_choices, "Gas and Electricity", "Groceries", "Transportation", "Clothes", "Mortgages", "Others")
    
    Label(transaction_page, text="Description:").grid(row=1, column = 3)  # Label for description
    label_transaction = Entry(transaction_page)
    label_transaction.grid(row=1, column = 4)  # Create an entry field for description

    #show what the user selected in the dropdown box
    selected_transaction_label = Label(transaction_page, text = " Selected: - ", fg="blue")
    selected_transaction_label.grid(row=5, column = 0)


    #showing the listbox
    list_transaction = Listbox(transaction_page, width = 70, height = 20)
    list_transaction.grid(row= 6, rowspan=3, column = 1, columnspan = 3)

    # Button to save the transactions that the user entered.
    save_info = Button(transaction_page, text="Save Transaction", command=save_transactions)
    save_info.grid(row=11, column = 1)  

    #Show the pie chart (user's spending habits) based on their expense category.
    show_piechart = Button(transaction_page, text = "Show transaction chart", command = pie_chart)
    show_piechart.grid(row = 11, column = 2)

    #show the current balance
    Label(transaction_page, text="", font=(18)).grid(row=7)
    show_balance = Label(transaction_page, text="Current Balance: £0.00", font=("Times New Roman", 18)) #shows the current balance on the window (starts with £0.00)
    show_balance.grid(row=13, column = 0)

    #Button when clicked, go back to the main menu page
    Button(transaction_page, text="Back to main menu", command = lambda: go_to_mainmenu (transaction_page, main_menu_page)).grid(row=14, column=0)

    update_list() #update the list


    transaction_page.mainloop()  # Start the Tkinter event loop

def go_to_mainmenu(transaction_page, main_menu_page):
    transaction_page.destroy() #destroy the transaction page
    main_menu_page.deiconify() #redraw (show) the main menu page again


if __name__=="__main__": #if called call this function
    transaction_screen()













