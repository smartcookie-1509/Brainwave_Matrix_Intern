class ATM:
    def __init__(self):
        self.users = {
            "123456": {"pin": "1234", "balance": 1000.0},
            "654321": {"pin": "4321", "balance": 500.0}
        }
        self.current_user = None

    def authenticate_user(self):
        account = input("Enter your account number: ")
        pin = input("Enter your PIN: ")

        user = self.users.get(account)

        if user and user['pin'] == pin:
            print("Login successful!\n")
            self.current_user = account
            return True
        else:
            print("Invalid account number or PIN.\n")
            return False

    def check_balance(self):
        balance = self.users[self.current_user]["balance"]
        print(f"Your current balance is:{balance:.2f} Rupees\n")

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                raise ValueError
            self.users[self.current_user]["balance"] += amount
            print(f"{amount:.2f} Rupees deposited successfully.\n")
        except ValueError:
            print("Invalid amount.\n")

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                raise ValueError

            if self.users[self.current_user]["balance"] >= amount:
                self.users[self.current_user]["balance"] -= amount
                print(f"{amount:.2f} Rupees withdrawn successfully.\n")
            else:
                print("Insufficient balance.\n")
        except ValueError:
            print("Invalid amount.\n")

    def show_menu(self):
        while True:
            print("====== ATM MENU ======")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                print("Thank you for using our ATM. Goodbye!\n")
                break
            else:
                print("Invalid choice. Please try again.\n")

    def run(self):
        print("===== Welcome to the ATM System =====\n")
        if self.authenticate_user():
            self.show_menu()



if __name__ == "__main__":
    atm = ATM()
    atm.run()
