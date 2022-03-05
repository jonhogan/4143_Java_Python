'''
Author      Jonathan Hogan
Class       Dr.Das - CMPS 4143 Contemporary Programming Languages
Due         11/10/21 

(30points)Write the OOP program in pythonusing class.Assuming you have four
classes: Bank account which is theparent class and it has two child classes Saving
Account class and Checking account class. Customer is another class who has a bank
account; either saving or checking or both. Implement the scenario using python OOP
and make sure you have covered those OOP concepts on your code: inheritance(any),
polymorphism (runtime and compile time), abstraction and encapsulation.
'''
class BankingAccount: #Bank Account super class
    
    balance = 0.00
        
    def __init__(self, _balance = 0):
        self.balance = int(_balance)

    def withdraw(self, amount = 0):
        if amount > self.balance:
            print('Insufficient funds')
        else:
            self.balance -= amount

    def deposit(self, amount = 0):
        self.balance += float(amount)

    def getbal(self):
        print('Balance is ${:.2f}'.format(float(self.balance)))

#Savings derived from BankingAccount
class Savings(BankingAccount):

    def __init__(self, _balance):
        super().__init__(_balance)

    def withdraw(self, amount=0):
        flag = True
        while flag:
            print('This is a Savings account\nPlease confirm if you wish to withdraw:')
            confirm = input('Yes/No')
            if confirm.lower == 'no':
                flag = False
                print('Canceled')
            elif confirm.lower == 'yes':
                flag = False
                return super().withdraw(amount=amount)
            else:
                print('Invalid selection, please try again.')
        
#Checking derived from Checking
class Checking(BankingAccount):

    def __init__(self, _balance):
        super().__init__(_balance)

class Customer:
    name = ''

    def __init__(self, name,_balance):
        self.checkacct = Checking(_balance)
        self.name = name

    def getbal(self):
        self.checkacct.getbal()

    def deposit(self, amount):
        self.checkacct.deposit(amount)

    def withdraw(self, amount):
        self.checkacct.withdraw(amount)


def menu():
    print("Please make a selection:\n1. Deposit\n2. Withdraw\n3. Get Balance\n4. Exit")

#Driver/Main code

flag = True #Flag used for while loops

name = input("Enter your name: ")
while flag: #Verify balance amount
    bal = input("Enter your starting balance: ")

    if bal.isnumeric():
        bal = int(bal)
        flag = False

    else:
        print('Invalid amount')

flag = True

person = Customer(name, bal)
    
#Menu
menu()

#while loops used for input validation
while flag: 

    option = int(input('Please select the number: '))

    if option == 1: #Deposit loop

        while flag:
            amount = input('Please enter the amount to deposit: ')

            if amount.isnumeric():
                amount = int(amount)
                person.deposit(amount)
                flag = False

            else:
                print('Invalid amount')

        flag = True
        menu()
    elif option == 2:  #Withdraw loop

        while flag:
            amount = input('Please enter the amount to withdraw: ')

            if amount.isnumeric():
                amount = int(amount)
                person.withdraw(amount)
                flag = False

            else:
                print('Invalid amount')
                
        flag = True
        menu()

    elif option == 3: #Check Balance

        person.getbal()
        print('\n')
        menu()

    elif option == 4: #Exit

        print('Goodbye')
        flag = False

    else: #Invalid selection clause
        print('Invalid selection\n\n')
        menu()