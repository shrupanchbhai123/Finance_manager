from user import register, login
from finance import add_transaction, delete_transaction, set_budget, check_budget
from report import generate_report

def main():
    print("Welcome to Personal Finance Manager!")
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            register(username, password)
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_id = login(username, password)

            if user_id:
                user_menu(user_id)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")

def user_menu(user_id):
    while True:
        print("\n1. Add Transaction")
        print("2. Delete Transaction")
        print("3. Set Budget")
        print("4. Check Budget")
        print("5. Generate Report")
        print("6. Logout")

        choice = input("Choose an option: ")

        if choice == "1":
            trans_type = input("Type (income/expense): ")
            category = input("Category: ")
            amount = float(input("Amount: "))
            date = input("Date (YYYY-MM-DD): ")
            add_transaction(user_id, trans_type, category, amount, date)
        elif choice == "2":
            trans_id = int(input("Transaction ID: "))
            delete_transaction(trans_id)
        elif choice == "3":
            category = input("Category: ")
            amount = float(input("Budget Amount: "))
            set_budget(user_id, category, amount)
        elif choice == "4":
            category = input("Category: ")
            check_budget(user_id, category)
        elif choice == "5":
            period = input("Report period (monthly/yearly): ")
            generate_report(user_id, period)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
     

     
