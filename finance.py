from database import create_connection, create_table, add_expenses, fetch_all
import pandas as pd
import matplotlib.pyplot as plt

class FinanceManager:
    def __init__(self):
        self.conn = create_connection()
        create_table(self.conn)

    def add_expense(self, date, category, description, amount):
        expense = (category, description, date, amount)
        add_expenses(self.conn, expense)

    def get_expenses(self):
        expenses = fetch_all(self.conn)
        df = pd.DataFrame(expenses, columns=["ID", "Category", "Description", "Date", "Amount"])
        return df

    def generate_category_pie_chart(self):
        df = self.get_expenses()
        category_expenses = df.groupby('Category')['Amount'].sum()
        plt.figure(figsize=(8, 8))
        plt.pie(category_expenses, labels=category_expenses.index, autopct='%1.1f%%', startangle=140)
        plt.title('Expense Distribution by Category')
        plt.axis('equal')
        plt.show()

    def generate_total_expenses_bar_chart(self):
        df = self.get_expenses()
        total_expenses = df['Amount'].sum()
        plt.figure(figsize=(10, 6))
        plt.bar("Total Expenses", total_expenses)
        plt.ylabel('Amount Spent')
        plt.title('Total Expenses')
        plt.show()
