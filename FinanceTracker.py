import json

# Global list to store transactions
transactions = []

# File handling functions
def load_transactions():
    try:
        with open('finance-tracker.json', 'r') as f: #Opening the file in read-only mode
            data = json.load(f) #Loading the file data in to the variable 'data'
            transactions.extend(data) #Adding the elements inside 'data' to transactions list
        print("Loaded transactions successfully")
    except FileNotFoundError: #Error Handling 
        print("We can't find a 'finance-tracker.json' file")

def save_transactions():
    with open('finance-tracker.json', 'w') as f:
        json.dump(transactions, f) #Adding transactions list to the file as a string
    print("Transactions saved successfully!")

# Feature implementations
def add_transaction():
    print("Add a new transaction: ")
    amount = int(input("Enter an Amount: "))
    category = input("Enter Transaction Name: ")
    transaction_type = input("Enter Transaction Type( Income or Expense ): ")
    date = input("Enter date (YYYY-MM-DD): ")
    transaction = {"amount": amount, "category": category, "type": transaction_type, "date": date}
    transactions.append(transaction)
    print("Transaction Added Successfully!")

def view_transactions():
    if not transactions:
        print("No transactions available.")
        return
    print("Transactions:")
    for i in range(len(transactions)):
        transaction = transactions[i]
        print(f"{i}. Amount: {transaction['amount']}, Category: {transaction['category']}, Type: {transaction['type']}, Date: {transaction['date']}")


def update_transaction():
    if not transactions:
        print("No transactions available.")
        return
    else:
        print("Select a transaction to update: ")
        for i in range(len(transactions)):
            transaction = transactions[i]
            print(f"{i}. Amount: {transaction['amount']}, Category: {transaction['category']}, Type: {transaction['type']}, Date: {transaction['date']}")

            try:
                selection = int(input("Enter the number of the transaction to update: "))
                if selection <= len(transactions):
                    transaction = transactions[selection]
                    print("Update transaction details:")
                    amount = int(input(f"Enter new amount (current: {transaction['amount']}): "))
                    category = input(f"Enter new category (current: {transaction['category']}): ")
                    transaction_type = input(f"Enter new transaction type (current: {transaction['type']}): ")
                    date = input(f"Enter new date (YYYY-MM-DD) (current: {transaction['date']}): ")
                    transactions[selection] = {"amount": amount, "category": category, "type": transaction_type, "date": date}
                    save_transactions()
                    print("Transaction updated successfully!")
                else:
                    print("Invalid selection. Please choose a valid transaction number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

def delete_transaction():
    # Placeholder for delete transaction logic
    # Remember to use save_transactions() after deleting
    pass

def display_summary():
    # Placeholder for summary display logic
    pass

def main_menu():
    load_transactions()  # Load transactions at the start
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Display Summary")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            update_transaction()
        elif choice == '4':
            delete_transaction()
        elif choice == '5':
            display_summary()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

# if you are paid to do this assignment please delete this line of comment 
