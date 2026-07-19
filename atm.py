class ATM:
    def __init__(self, account_holder, pin, balance):
        self.is_logged_in = False
        self.account_holder = account_holder
        self.__pin = pin
        self.balance = balance

    def login(self, entered_pin):
     if entered_pin == self.__pin:
        self.is_logged_in = True
        print("Login Successful")
        print(f"Welcome, {self.account_holder}!")
        return True
     else:
        self.is_logged_in = False
        print("Invalid PIN")
        return False

    def check_balance(self):
        print(f"Your current balance is: {self.balance}")

    def deposit(self, amount):
        if self.is_logged_in:
            if amount > 0:
                self.balance += amount
                print(f"Deposit Successful. Current Balance: {self.balance}")
            else:
              print("Invalid amount")
        else:
             print("Please login first")
             
    def withdraw(self, amount):
        if self.is_logged_in:
            if amount <= 0:
                print("Invalid amount")
            elif amount > self.balance:
                print("Insufficient Balance")
            else:
                self.balance -= amount
                print(f"Withdraw Successful. Remaining Balance: {self.balance}")
        else:
            print("Please login first")
    def logout(self):
       self.is_logged_in = False
       print("Logged out successfully")
       print("Thank you for using our ATM.")
       print("Please collect your card.")
       print("Have a nice day!")


a1 = ATM("Amna", 2006, 50000)

print("========================")
print("     WELCOME TO ATM")
print("========================")

while True:
    entered_pin = int(input("Please enter your PIN: "))
    if a1.login(entered_pin):
        while True: 
           print("\n====== ATM MENU ======")
           print("1. Check Balance")
           print("2. Deposit")
           print("3. Withdraw")
           print("4. Logout")
           choice = input("Enter your choice: ") 
           if choice == "1":
              a1.check_balance()

           elif choice == "2":
              amount = int(input("Enter deposit amount: "))
              a1.deposit(amount)

           elif choice == "3":
             amount = int(input("Enter withdraw amount: "))
             a1.withdraw(amount)

           elif choice == "4":
            a1.logout()
            break
           else:
            print("Invalid choice. Please try again.")
        break
    





