class BankAccount:
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def display(self):
        print("\nAccount Number:", self.acc_no)
        print("Name:", self.name)
        print("Account Type:", self.acc_type)
        print("Balance:", self.balance)


acc = None
while True:
    print("\n--- BANK MENU ---")
    print("1. Account Creation")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        acc_no = input("Enter account number: ")
        name = input("Enter name: ")
        acc_type = input("Enter account type: ")
        balance = float(input("Enter initial balance: "))
        if balance < 0:
            print("Initial balance cannot be negative.")
        else:
            acc = BankAccount(acc_no, name, acc_type, balance)
            print("Account created successfully.")
    elif choice == 2:
        if acc is None:
            print("Please create an account first.")
        else:
            amount = float(input("Enter amount to deposit: "))
            acc.deposit(amount)
    elif choice == 3:
        if acc is None:
            print("Please create an account first.")
        else:
            amount = float(input("Enter amount to withdraw: "))
            acc.withdraw(amount)
    elif choice == 4:
        if acc is None:
            print("Please create an account first.")
        else:
            acc.display()
    elif choice == 5:
        print("Thank you for using the bank.")
        break
    else:
        print("Invalid choice. Please try again.")
