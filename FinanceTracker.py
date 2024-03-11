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
    amount = float(input("Enter an Amount: "))
    pass

def view_transactions():
    pass

def update_transaction():
    # Placeholder for update transaction logic
    # Remember to use save_transactions() after updating
    pass

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
