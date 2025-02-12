

# Everything above this should be a function 
# if__name__ == "__main__":
#   main()


"""
function main()
    ** Remember to define it! 
    display "Welcome to the Budget Planner and Expense Tracker!"  
    monthlyIncome = getMonthlyIncome()
    expenses = empty dictonary 
loop forever: (A while loop)
        display menu:
            1.) Add an expense
            2.) View budget summary
            3.) Exit 
***---[]
        userChoice = read input 
        if userChoice == 1: 
            addExpense(expenses) 
        elif userChoice == 2:
            displaySummary(monthlyIncome, expenses)
        elif userChoice == 3: 
            display "Goodbye." 
            break
        else:
            display "Invalid choice. Try again."

 function getMonthlyIncome():
        loop forever: (while loop)
           monthlyIncome = read user input 
           if monthlyIncome is a valid float and >= 0:
                return monthlyIncome 
          else:
                display "Invalid input. Please enter a non-negative number." 

function addExpense(expenses):
        category = read category input 
        while loop:
            amount = read input 

            if amount is a valid float and >= 0:
                expenses[category] = expenses.get(category, 0) + amount 
                display "Expense added!" 
                break (sends back to menu)
            else:
                display "Invalid expense amount. Try again."


 function displaySummary(monthlyIncome, expenses):
        totalExpenses = sum of all values in expenses 
        remainingBudget = monthlyIncome - totalExpenses

        display total income / monthlyIncome 
        display each category and amount, plus percentage 
        display total expenses 
        display remainingBudget 
"""


# monthlyIncome = input("Please enter your monthly income!: ")

def getMonthlyIncome():
   while True:
        monthlyIncome = input(float())
        if monthlyIncome >= 0: 
            return 
        else: 
            print("Invalid input, please enter a non-negative number.")

def addExpense(expenses):
        expenseAdd = input("Please input the category you'd like to add the expense of: ")
        print("Total Expense Total:" + expenseAdd)
        
        amountTotal = input("Please input the amount you'd like to add to the expense: ")
        print = ("Total amount entered in: ")
        
        while True: 
            if amount >= "0":
                expenses[category] = expenses.get(category, "0") + amount 
                print("Expense added!") 
                break 
            else:
                print("Invalid expense amount. Try again.")



def displaySummary(monthlyIncome, expenses):
    # category = input("Please input a category: ")  
    # amount = float(input("Please input the correct amount: "))
    expenses[category] = expenses.get(category, 0) + amount 
    # expenses = {category}
    print("Total expenses: $", monthlyIncome)
    print("Expenses:") 
    for category, amount in expenses.items():
        percentage = (amount/monthlyIncome) * 100 
        print(category,":", amount, "(",percentage,").")
        print("This is a test to make sure this works.")
    

    
    
# print(monthlyIncome) 
# print                              
# print(total expenses) 
# print(remainingBudget) 





##------------------------------ Main Function ----------------------------------------------->
def main():
    print("Welcome to the Budget and Expense Planner!")
    print("##########################################")
    monthlyIncome = input("Please enter your monthly income!: ")
    print("$",monthlyIncome)
    # monthlyIncome == getMonthlyIncome()
    expenses = {} 
    while True: 
        print("################################") 
        print("################################")
        print("1.) Add an expense budget.")
        print("2.) View budget summary.")
        print("3.) Exit") 
        print("################################")
        print("################################")
        
        userChoice = input()
        if userChoice == "1": 
            addExpense(expenses)
            print(addExpense)
        elif userChoice == "2":
            displaySummary(monthlyIncome, expenses)
        elif userChoice == "3": 
            print("Goodbye.") 
            break
        else:
            print("Invalid choice. Try again.")
            return

if __name__ == '__main__':
    main()

