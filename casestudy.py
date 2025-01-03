
import threading
import time
import csv

class Customer:
    def __init__(self, customer_id, name, account_balance, account_type='Savings'):
        self.customer_id = customer_id
        self.name = name
        self.account_balance = float(account_balance)
        self.account_type = account_type
        self.transaction_history = []
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            if amount > 0:
                self.account_balance += amount
                self.transaction_history.append(f"Deposited: {amount}")
                print(f"{self.name}: Deposited {amount}. New Balance: {self.account_balance}")
            else:
                print("Deposit amount must be positive.")

    def withdraw(self, amount):
        with self.lock:
            if amount > 0 and self.account_balance >= amount:
                self.account_balance -= amount
                self.transaction_history.append(f"Withdrew: {amount}")
                print(f"{self.name}: Withdrew {amount}. New Balance: {self.account_balance}")
            else:
                print("Insufficient balance or invalid amount.")

    def view_transaction_history(self):
        print(f"{self.name}'s Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

    def apply_interest(self, interest_rate=0.02):
        with self.lock:
            if self.account_type == 'Savings':
                interest = self.account_balance * interest_rate
                self.account_balance += interest
                self.transaction_history.append(f"Interest Applied: {interest}")
                print(f"{self.name}: Interest {interest} applied. New Balance: {self.account_balance}")

def read_customer_data(filename):
    customers = []
    try:
        with open(filename, mode='r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header
            for row in csv_reader:
                customer_id, name, account_balance = row
                customers.append(Customer(customer_id, name, account_balance))
    except FileNotFoundError:
        print("File not found. Ensure the file is in the correct directory.")
    return customers

def perform_operations(customers):
    while True:
        print("\nOperations: 1. Deposit  2. Withdraw  3. View Transactions  4. Exit")
        choice = input("Enter your choice: ")
        if choice == '4':
            break
        customer_id = input("Enter Customer ID: ")
        customer = next((c for c in customers if c.customer_id == customer_id), None)
        if not customer:
            print("Customer not found!")
            continue

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            customer.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            customer.withdraw(amount)
        elif choice == '3':
            customer.view_transaction_history()
        else:
            print("Invalid choice!")

def periodic_interest_application(customers, interval=10):
    def apply_interest_to_all():
        while True:
            for customer in customers:
                customer.apply_interest()
            time.sleep(interval)

    thread = threading.Thread(target=apply_interest_to_all, daemon=True)
    thread.start()

def main():
    customers = read_customer_data('Data.csv')
    if not customers:
        return

    periodic_interest_application(customers)  # Start interest application thread

    print("Welcome to the Banking System Simulation!")
    perform_operations(customers)
    print("Exiting the Banking System. Have a great day!")

if __name__ == "__main__":
    main()

