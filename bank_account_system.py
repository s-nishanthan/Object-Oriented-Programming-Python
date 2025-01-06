class BankAccount:
    # Constructor to initialize the account details
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    # Method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: ${amount}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    # Method to check account balance
    def check_balance(self):
        print(f"Account balance: ${self.balance}")

# Main function to interact with the BankAccount class
def main():
    # Create a BankAccount object for the user
    account = BankAccount("Alice", 500)
    
    # Display initial account information
    print(f"Account owner: {account.owner}")
    account.check_balance()
    
    # Perform some operations
    account.deposit(200)
    account.check_balance()
    
    account.withdraw(100)
    account.check_balance()
    
    account.withdraw(700)  # This should show an error message

if __name__ == "__main__":
    main()
