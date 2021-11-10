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
import random

class BankAccount:
    #, CheckingAccount, SavingsAccount
    def __init__(self, name, _acctNum, _balance):
        self.name = name
        self._balance = _balance
        self._acctNum = _acctNum

    def get_info(self):
        print("Name:\t{}".format(self.name))
        self.print_balance()

    def get_balance(self):
        return self._balance

    def print_balance(self):
        print("Current Balance:\t{0:.2f}".format(self.get_balance()))


def deposit_money(self, amount):
    if(type(amount) == int and amount > 0):
        self._balance += amount
        print("Deposit amount:\t{0:.2f} ".format(amount))

    else:
        print("Please enter valid data for amount")


class SavingAccount(BankAccount):

    def __init__(self, name, balance, interest_rate):
        BankAccount.__init__(self, name, balance)
        self._interest_rate = interest_rate

    def get_info(self):
        print("Account Type: Savings")
        print("Name:\t{}".format(self.name))
        self.print_balance()
        self.print_interest_rate()

    def print_interest_rate(self):

        print("Current rate of interest = {0:.2f}".format(self.get_interest_rate()))

    def set_interest_rate(self, rate):

        if(type(rate) == int and rate > 0):
            self._interest_rate = rate

        else:
            print("Please enter valid data for interest rate")

    def get_interest(self, years):
        return self.get_interest_rate()*years*self.get_balance()/100

    def get_interest_rate(self):
        return self._interest_rate


class CheckingAccount(BankAccount):

    def __init__(self, name, balance, checks_issued):
        BankAccount.__init__(self, name, balance)
        self._checks_issued = checks_issued

    def get_info(self):
        print("Account Type: Current")
        print("Name:\t{}".format(self.name))
        self.print_balance()
        self.print_checks()

    def print_checks(self):
        print("Total number of checks issued: {}".format(self.get_checks_issued()))

    def get_checks_issued(self):
        return self._checks_issued

    def issue_checks(self, n):
        if(type(n) == int and n > 0):
            self._checks_issued += n

        else:
            print("enter valid data for number of checks")


class Customer(SavingAccount, CheckingAccount):

    def __init__(self, name, balance, type):
        self.type = type

        if(type == "s"):
            interest_rate = int(input("Enter interest rate: "))
            SavingAccount.__init__(self, name, balance, interest_rate)

        if(type == "c"):
            checks_issued = int(input("Enter number of checks: "))
            CheckingAccount.__init__(self, name, balance, checks_issued)

        if(type == "s+c" or type == "c+s"):
            rate = int(input("Enter interest rate: "))
            checks_issued = int(input("Enter number of checks: "))
            SavingAccount.__init__(self, name, balance, rate)
            CheckingAccount.__init__(self, name, balance, checks_issued)

    def get_info(self):

        if(self.type == "s"):
            SavingAccount.get_info(self)

        elif(self.type == "c"):
            CheckingAccount.get_info(self)

        else:
            print("Account Type: Savings + Checking")
            print("Name:\t{}".format(self.name))
            self.print_balance()
            self.print_interest_rate()
            self.print_checks()


Selection = ""
while Selection != 8:

    print("MAIN MENU")
    print("1. NEW ACCOUNT")
    print("2. DEPOSIT AMOUNT")
    print("3. WITHDRAW AMOUNT")
    print("4. BALANCE ENQUIRY")
    print("5. ALL ACCOUNT HOLDER LIST")
    print("6. CLOSE AN ACCOUNT")
    print("7. MODIFY AN ACCOUNT")
    print("8. EXIT")
    print("Select Your Option (1-8) ")

    Selection = input()
    if Selection == '1':
        n = input('Please enter your name: ')
        accountNum = random.randint(0, 999999)
        print("Your new account number is {0:06}".format(accountNum))
        b = input('Enter your deposit amount: ')
        b = int(b)
        print('You are depositing: {0:.2f}'.format(b))
        BankAccount(n, accountNum, b)

    elif Selection == '2':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num, 1)

    elif Selection == '3':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num, 2)

    elif Selection == '4':
        num = int(input("\tEnter The account No. : "))
        displaySp(num)

    elif Selection == '5':
        displayAll()

    elif Selection == '6':
        print("\tThank you for banking with me")
        break

    else:
        print("Invalid Selection")
        Selection = input("Enter your Selection 1-8 : ")