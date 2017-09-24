def main():
    endProgram='no'
    integerchoice=0
    totalBudget=1000
    while endProgram=='no':
        print
        print'Welcome to my budget manager'
        print'Menu: '
        print'1-Add Income'
        print'2-Remove Expenses'
        print'3-Check the available balance:'
        print'4-Exit '
        print
        choice=int(raw_input('Please select an option: '))
        if choice== 1:
                totalBudget = addIncome(totalBudget)
        elif choice== 2:
                totalBudget = removeExpenses(totalBudget)
        elif choice== 3:
                print'Your available balance is:',totalBudget
        elif choice== 4:
                endProgram ='yes'
                print'Thank you for using my budget manager'
        elif choice>=4:
                 print'Invalid! please try again'

def addIncome(totalBudget):
    income=input('Enter the income received:$')
    rent=input('Enter the rent amount received:$')
    interest=input('Enter the interest amount received:$')
    totalIncome=income+rent+interest
    totalBudget=totalIncome+totalBudget
    print('Your Current balance is:$%2f')%totalBudget
    return totalBudget    
    
def removeExpenses(totalBudget):
    loan=input('Amount paid towards loan: $ ')
    bills=input('Amount paid towards utility bills: $')
    grocery= input('Amount paid towards groceries:')
    transport=input('Amount paid towards transport:$')
    childrenexpenses=input('Amount paid towards children expenses:$')
    medical=input('Amount paid towards medical: $')
    tax=input('Amount paid towards tax: $')
    totalExpenses=loan+bills+grocery+transport+childrenexpenses+medical+tax
    totalBudget=totalExpenses-totalBudget
    print('Your current balance is :$%2f')%totalBudget
    return totalBudget 
    
  main()  
