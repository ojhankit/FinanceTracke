from finance import FinanceManager
import sys

def print_menu():
    print("\nPersonal Finance Manager")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Generate Category Pie Chart")
    print("4. Generate Total Expenses Bar Chart")
    print("5. Exit")

def main():
    manager = FinanceManager()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            manager.add_expense(date, category, description, amount)
            print("Expense added successfully.")
        elif choice == '2':
            df = manager.get_expenses()
            print(df)
        elif choice == '3':
            manager.generate_category_pie_chart()
        elif choice == '4':
            manager.generate_total_expenses_bar_chart()
        elif choice == '5':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
